"""
NexusCRM Action Task & SLA Management Models.
Automated task dispatching, user assignments, due dates, priority levels, and breach tracking.
"""

from dataclasses import dataclass, field
from typing import Optional, Dict, Any
from datetime import datetime

@dataclass
class ActionTask:
    id: str
    case_id: str
    client_id: str
    task_type: str  # REVIEW_DOCUMENT, RESOLVE_SCREENING_HIT, CONDUCT_EDD, CREDIT_REVIEW, OBTAIN_SIGNATURE
    title: str
    description: str
    priority: str = "MEDIUM"  # LOW, MEDIUM, HIGH, URGENT
    status: str = "OPEN"  # OPEN, IN_PROGRESS, COMPLETED, CANCELLED
    assigned_to_user_id: str = ""
    assigned_role: str = "COMPLIANCE_OFFICER"
    due_date: str = ""
    is_sla_breached: bool = False
    resolution_notes: Optional[str] = None
    completed_at: Optional[str] = None
    created_at: str = field(default_factory=lambda: datetime.utcnow().isoformat())

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "case_id": self.case_id,
            "client_id": self.client_id,
            "task_type": self.task_type,
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
            "status": self.status,
            "assigned_to_user_id": self.assigned_to_user_id,
            "assigned_role": self.assigned_role,
            "due_date": self.due_date,
            "is_sla_breached": self.is_sla_breached,
            "resolution_notes": self.resolution_notes,
            "completed_at": self.completed_at,
            "created_at": self.created_at
        }
