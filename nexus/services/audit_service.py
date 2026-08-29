"""
NexusCRM Audit Trail Service.
Ensures tamper-evident event streaming with SHA-256 cryptographic chaining for SOC2, GDPR, and FINRA compliance.
"""

import json
import uuid
import hashlib
from typing import List, Dict, Optional, Any
from datetime import datetime

from nexus.database.connection import get_db_session

class AuditService:
    @staticmethod
    def log_event(
        entity_type: str,
        entity_id: str,
        action: str,
        actor_id: str,
        actor_name: str,
        actor_role: str,
        change_summary: str,
        previous_state: Optional[Dict[str, Any]] = None,
        new_state: Optional[Dict[str, Any]] = None,
        ip_address: str = "127.0.0.1"
    ) -> Dict[str, Any]:
        event_id = f"AUD-{uuid.uuid4().hex[:12]}"
        now_str = datetime.utcnow().isoformat()

        with get_db_session() as conn:
            cursor = conn.cursor()

            # Retrieve previous event hash
            cursor.execute("SELECT event_hash FROM audit_events ORDER BY rowid DESC LIMIT 1;")
            row = cursor.fetchone()
            prev_hash = row[0] if row else "GENESIS_ROOT_HASH_00000000000000000000000000000000"

            # Compute current event hash
            payload = {
                "id": event_id,
                "entity_type": entity_type,
                "entity_id": entity_id,
                "action": action,
                "actor_id": actor_id,
                "timestamp": now_str,
                "prev_hash": prev_hash,
                "summary": change_summary
            }
            curr_hash = hashlib.sha256(json.dumps(payload, sort_keys=True).encode("utf-8")).hexdigest()

            cursor.execute("""
                INSERT INTO audit_events (
                    id, entity_type, entity_id, action, actor_id, actor_name,
                    actor_role, ip_address, timestamp, previous_state, new_state,
                    change_summary, previous_event_hash, event_hash
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
            """, (
                event_id, entity_type, entity_id, action, actor_id, actor_name,
                actor_role, ip_address, now_str,
                json.dumps(previous_state) if previous_state else None,
                json.dumps(new_state) if new_state else None,
                change_summary, prev_hash, curr_hash
            ))

            payload["event_hash"] = curr_hash
            return payload

    @staticmethod
    def get_events(entity_type: Optional[str] = None, entity_id: Optional[str] = None, limit: int = 100) -> List[Dict[str, Any]]:
        with get_db_session() as conn:
            cursor = conn.cursor()
            query = "SELECT * FROM audit_events WHERE 1=1"
            params = []
            if entity_type:
                query += " AND entity_type = ?"
                params.append(entity_type)
            if entity_id:
                query += " AND entity_id = ?"
                params.append(entity_id)

            query += " ORDER BY timestamp DESC LIMIT ?;"
            params.append(limit)

            cursor.execute(query, params)
            return [dict(r) for r in cursor.fetchall()]
