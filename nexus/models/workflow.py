"""
NexusCRM Workflow Engine Models.
State machine transitions, multi-sign-off four-eyes & six-eyes approval gates, and SLA escalations.
"""

from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any
from datetime import datetime

@dataclass
class ApprovalGate:
    id: str
    case_id: str
    stage: str
    gate_name: str  # e.g., "COMPLIANCE_SIGN_OFF", "CREDIT_COMMITTEE_APPROVAL", "FOUR_EYES_CHECK"
    required_role: str  # COMPLIANCE_OFFICER, CREDIT_ANALYST, MANAGING_DIRECTOR
    status: str = "PENDING"  # PENDING, APPROVED, REJECTED
    approver_id: Optional[str] = None
    approver_name: Optional[str] = None
    comments: Optional[str] = None
    decided_at: Optional[str] = None
    created_at: str = field(default_factory=lambda: datetime.utcnow().isoformat())

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "case_id": self.case_id,
            "stage": self.stage,
            "gate_name": self.gate_name,
            "required_role": self.required_role,
            "status": self.status,
            "approver_id": self.approver_id,
            "approver_name": self.approver_name,
            "comments": self.comments,
            "decided_at": self.decided_at,
            "created_at": self.created_at
        }

@dataclass
class WorkflowTransition:
    id: str
    case_id: str
    from_stage: str
    to_stage: str
    actor_id: str
    actor_role: str
    transition_timestamp: str = field(default_factory=lambda: datetime.utcnow().isoformat())
    reason: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "case_id": self.case_id,
            "from_stage": self.from_stage,
            "to_stage": self.to_stage,
            "actor_id": self.actor_id,
            "actor_role": self.actor_role,
            "transition_timestamp": self.transition_timestamp,
            "reason": self.reason
        }
