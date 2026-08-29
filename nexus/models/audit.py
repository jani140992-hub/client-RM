"""
NexusCRM Audit Logging & Regulatory Integrity Models.
Tamper-evident audit trail entries with SHA-256 state hashing, actor attribution, and before/after diffs.
"""

from dataclasses import dataclass, field
from typing import Optional, Dict, Any
from datetime import datetime
import hashlib
import json

@dataclass
class AuditEvent:
    id: str
    entity_type: str  # CLIENT, ONBOARDING_CASE, DOCUMENT, SCREENING_HIT, RISK_ASSESSMENT
    entity_id: str
    action: str  # CREATE, UPDATE, STAGE_TRANSITION, DOCUMENT_UPLOAD, APPROVAL, REJECTION
    actor_id: str
    actor_name: str
    actor_role: str
    ip_address: str = "127.0.0.1"
    timestamp: str = field(default_factory=lambda: datetime.utcnow().isoformat())
    previous_state: Optional[Dict[str, Any]] = None
    new_state: Optional[Dict[str, Any]] = None
    change_summary: str = ""
    previous_event_hash: str = "GENESIS"
    event_hash: str = ""

    def calculate_event_hash(self) -> str:
        payload = {
            "id": self.id,
            "entity_type": self.entity_type,
            "entity_id": self.entity_id,
            "action": self.action,
            "actor_id": self.actor_id,
            "timestamp": self.timestamp,
            "prev_hash": self.previous_event_hash,
            "summary": self.change_summary
        }
        serialized = json.dumps(payload, sort_keys=True)
        self.event_hash = hashlib.sha256(serialized.encode("utf-8")).hexdigest()
        return self.event_hash

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "entity_type": self.entity_type,
            "entity_id": self.entity_id,
            "action": self.action,
            "actor_id": self.actor_id,
            "actor_name": self.actor_name,
            "actor_role": self.actor_role,
            "ip_address": self.ip_address,
            "timestamp": self.timestamp,
            "previous_state": self.previous_state,
            "new_state": self.new_state,
            "change_summary": self.change_summary,
            "previous_event_hash": self.previous_event_hash,
            "event_hash": self.event_hash or self.calculate_event_hash()
        }
