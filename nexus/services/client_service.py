"""
NexusCRM Client Service.
Provides high-level business logic for managing institutional clients, corporate entities, contacts, and relationship coverage.
"""

import sqlite3
import json
import uuid
from typing import List, Dict, Optional, Any
from datetime import datetime

from nexus.database.connection import get_db_session
from nexus.models.client import Client, LegalEntity, ContactPerson

class ClientService:
    @staticmethod
    def get_all_clients(
        search_query: Optional[str] = None,
        status: Optional[str] = None,
        risk_tier: Optional[str] = None,
        rm_id: Optional[str] = None,
        limit: int = 50,
        offset: int = 0
    ) -> List[Dict[str, Any]]:
        with get_db_session() as conn:
            cursor = conn.cursor()
            query = """
                SELECT c.*, rm.name as rm_name, ob.current_stage, ob.sla_status, ob.completion_percentage, ob.case_number
                FROM clients c
                LEFT JOIN relationship_managers rm ON c.primary_relationship_manager_id = rm.id
                LEFT JOIN onboarding_cases ob ON c.id = ob.client_id
                WHERE 1=1
            """
            params = []

            if search_query:
                query += " AND (c.name LIKE ? OR c.client_number LIKE ?)"
                like = f"%{search_query}%"
                params.extend([like, like])

            if status:
                query += " AND c.onboarding_status = ?"
                params.append(status)

            if risk_tier:
                query += " AND c.risk_tier = ?"
                params.append(risk_tier)

            if rm_id:
                query += " AND c.primary_relationship_manager_id = ?"
                params.append(rm_id)

            query += " ORDER BY c.created_at DESC LIMIT ? OFFSET ?;"
            params.extend([limit, offset])

            cursor.execute(query, params)
            rows = cursor.fetchall()
            results = []
            for r in rows:
                item = dict(r)
                if item.get("tags"):
                    try:
                        item["tags"] = json.loads(item["tags"])
                    except Exception:
                        item["tags"] = []
                results.append(item)
            return results

    @staticmethod
    def get_client_by_id(client_id: str) -> Optional[Dict[str, Any]]:
        with get_db_session() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT c.*, rm.name as rm_name, rm.email as rm_email, rm.team as rm_team
                FROM clients c
                LEFT JOIN relationship_managers rm ON c.primary_relationship_manager_id = rm.id
                WHERE c.id = ?;
            """, (client_id,))
            row = cursor.fetchone()
            if not row:
                return None
            data = dict(row)
            if data.get("tags"):
                try:
                    data["tags"] = json.loads(data["tags"])
                except Exception:
                    data["tags"] = []

            # Fetch entities
            cursor.execute("SELECT * FROM legal_entities WHERE client_id = ?;", (client_id,))
            entities = []
            for erow in cursor.fetchall():
                ed = dict(erow)
                if ed.get("operating_countries"):
                    try:
                        ed["operating_countries"] = json.loads(ed["operating_countries"])
                    except Exception:
                        ed["operating_countries"] = []
                entities.append(ed)
            data["legal_entities"] = entities

            # Fetch contacts
            cursor.execute("SELECT * FROM contact_persons WHERE client_id = ?;", (client_id,))
            data["contacts"] = [dict(crow) for crow in cursor.fetchall()]

            # Fetch onboarding case
            cursor.execute("SELECT * FROM onboarding_cases WHERE client_id = ?;", (client_id,))
            case_row = cursor.fetchone()
            data["onboarding_case"] = dict(case_row) if case_row else None

            return data

    @staticmethod
    def create_client(
        name: str,
        client_segment: str,
        rm_id: str,
        jurisdiction: str,
        entity_type: str,
        naics_code: str = "522110",
        tags: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        client_id = f"CLI-{uuid.uuid4().hex[:8]}"
        client_number = f"NX-{uuid.uuid4().hex[:6].upper()}"
        now_str = datetime.utcnow().isoformat()

        with get_db_session() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO clients (
                    id, client_number, name, client_segment, primary_relationship_manager_id,
                    onboarding_status, risk_tier, composite_risk_score, kyc_refresh_frequency_months,
                    tags, created_at, updated_at
                ) VALUES (?, ?, ?, ?, ?, 'PROSPECT', 'MEDIUM', 5.0, 24, ?, ?, ?);
            """, (
                client_id, client_number, name, client_segment, rm_id,
                json.dumps(tags or [client_segment.replace("_", " ")]),
                now_str, now_str
            ))

            entity_id = f"ENT-{uuid.uuid4().hex[:8]}"
            cursor.execute("""
                INSERT INTO legal_entities (
                    id, client_id, legal_name, entity_type, jurisdiction_of_incorporation,
                    primary_naics_code, created_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?);
            """, (
                entity_id, client_id, name, entity_type, jurisdiction,
                naics_code, now_str
            ))

        return ClientService.get_client_by_id(client_id)
