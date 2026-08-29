"""
NexusCRM Client Onboarding Case & Pipeline Models.
Defines the 10-stage institutional onboarding journey, SLA deadlines, milestone validations, and gate requirements.
"""

from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any
from datetime import datetime, timedelta
from enum import Enum

class OnboardingStage(Enum):
    STAGE_1_PROSPECT_LEAD = "PROSPECT_LEAD"
    STAGE_2_PRE_QUALIFICATION = "PRE_QUALIFICATION"
    STAGE_3_INFORMATION_GATHERING = "INFORMATION_GATHERING"
    STAGE_4_IDV_AND_VERIFICATION = "IDV_AND_VERIFICATION"
    STAGE_5_KYC_AML_SCREENING = "KYC_AML_SCREENING"
    STAGE_6_EDD_INVESTIGATION = "EDD_INVESTIGATION"
    STAGE_7_CREDIT_UNDERWRITING = "CREDIT_UNDERWRITING"
    STAGE_8_LEGAL_CONTRACTING = "LEGAL_CONTRACTING"
    STAGE_9_ACCOUNT_PROVISIONING = "ACCOUNT_PROVISIONING"
    STAGE_10_FINAL_APPROVAL_GATE = "FINAL_APPROVAL_GATE"
    COMPLETED = "COMPLETED"
    REJECTED = "REJECTED"

STAGE_ORDER = [
    OnboardingStage.STAGE_1_PROSPECT_LEAD,
    OnboardingStage.STAGE_2_PRE_QUALIFICATION,
    OnboardingStage.STAGE_3_INFORMATION_GATHERING,
    OnboardingStage.STAGE_4_IDV_AND_VERIFICATION,
    OnboardingStage.STAGE_5_KYC_AML_SCREENING,
    OnboardingStage.STAGE_6_EDD_INVESTIGATION,
    OnboardingStage.STAGE_7_CREDIT_UNDERWRITING,
    OnboardingStage.STAGE_8_LEGAL_CONTRACTING,
    OnboardingStage.STAGE_9_ACCOUNT_PROVISIONING,
    OnboardingStage.STAGE_10_FINAL_APPROVAL_GATE,
    OnboardingStage.COMPLETED
]

@dataclass
class MilestoneItem:
    id: str
    case_id: str
    stage: str
    title: str
    is_completed: bool = False
    completed_by: Optional[str] = None
    completed_at: Optional[str] = None
    notes: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "case_id": self.case_id,
            "stage": self.stage,
            "title": self.title,
            "is_completed": self.is_completed,
            "completed_by": self.completed_by,
            "completed_at": self.completed_at,
            "notes": self.notes
        }

@dataclass
class OnboardingCase:
    id: str
    client_id: str
    case_number: str  # e.g., "ONB-2026-00412"
    current_stage: str = OnboardingStage.STAGE_1_PROSPECT_LEAD.value
    stage_index: int = 0  # 0 to 10
    target_completion_date: str = ""
    sla_hours_budget: float = 336.0  # 14 days standard SLA
    sla_hours_elapsed: float = 0.0
    sla_status: str = "GREEN"  # GREEN, AMBER, RED (Breached)
    is_edd_triggered: bool = False
    assigned_relationship_manager_id: str = ""
    assigned_compliance_officer_id: Optional[str] = None
    assigned_credit_officer_id: Optional[str] = None
    assigned_operations_lead_id: Optional[str] = None
    completion_percentage: float = 0.0
    notes: str = ""
    milestones: List[MilestoneItem] = field(default_factory=list)
    created_at: str = field(default_factory=lambda: datetime.utcnow().isoformat())
    updated_at: str = field(default_factory=lambda: datetime.utcnow().isoformat())

    def update_completion_metrics(self):
        if not self.milestones:
            self.completion_percentage = 0.0
            return
        done = sum(1 for m in self.milestones if m.is_completed)
        self.completion_percentage = round((done / len(self.milestones)) * 100.0, 1)

    def calculate_sla_status(self, warning_threshold: float = 0.80) -> str:
        if self.sla_hours_budget <= 0:
            return "GREEN"
        ratio = self.sla_hours_elapsed / self.sla_hours_budget
        if ratio >= 1.0:
            self.sla_status = "RED"
        elif ratio >= warning_threshold:
            self.sla_status = "AMBER"
        else:
            self.sla_status = "GREEN"
        return self.sla_status

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "client_id": self.client_id,
            "case_number": self.case_number,
            "current_stage": self.current_stage,
            "stage_index": self.stage_index,
            "target_completion_date": self.target_completion_date,
            "sla_hours_budget": self.sla_hours_budget,
            "sla_hours_elapsed": self.sla_hours_elapsed,
            "sla_status": self.sla_status,
            "is_edd_triggered": self.is_edd_triggered,
            "assigned_relationship_manager_id": self.assigned_relationship_manager_id,
            "assigned_compliance_officer_id": self.assigned_compliance_officer_id,
            "assigned_credit_officer_id": self.assigned_credit_officer_id,
            "assigned_operations_lead_id": self.assigned_operations_lead_id,
            "completion_percentage": self.completion_percentage,
            "notes": self.notes,
            "milestones": [m.to_dict() for m in self.milestones],
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
