"""
NexusCRM Compliance & Financial Crime Models.
Screening hits, false positive clearances, PEP findings, adverse media, and EDD investigation cases.
"""

from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any
from datetime import datetime

@dataclass
class ScreeningHit:
    id: str
    case_id: str
    subject_name: str
    subject_type: str  # INDIVIDUAL, CORPORATE_ENTITY, UBO, VESSEL
    catalog_source: str  # OFAC_SDN, UN_EU_SANCTIONS, PEP_REGISTRY, ADVERSE_MEDIA
    hit_reference_id: str  # SDN ID or PEP ID
    matched_name: str
    match_score: float  # 0.0 to 1.0
    programs_or_tier: str  # e.g., "SDGT, RUSSIA-EO14024" or "Tier 1 PEP"
    disposition: str = "OPEN"  # OPEN, ESCALATED, CLEARED_FALSE_POSITIVE, CONFIRMED_TRUE_POSITIVE
    reviewed_by: Optional[str] = None
    reviewed_at: Optional[str] = None
    clearance_rationale: Optional[str] = None
    created_at: str = field(default_factory=lambda: datetime.utcnow().isoformat())

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "case_id": self.case_id,
            "subject_name": self.subject_name,
            "subject_type": self.subject_type,
            "catalog_source": self.catalog_source,
            "hit_reference_id": self.hit_reference_id,
            "matched_name": self.matched_name,
            "match_score": self.match_score,
            "programs_or_tier": self.programs_or_tier,
            "disposition": self.disposition,
            "reviewed_by": self.reviewed_by,
            "reviewed_at": self.reviewed_at,
            "clearance_rationale": self.clearance_rationale,
            "created_at": self.created_at
        }

@dataclass
class EDDInvestigationCase:
    id: str
    case_id: str
    client_id: str
    trigger_reason: str  # PEP_EXPOSURE, HIGH_RISK_JURISDICTION, ADVERSE_MEDIA, COMPLEX_UBO_STRUCTURE
    risk_level: str = "HIGH"  # HIGH, CRITICAL
    status: str = "IN_PROGRESS"  # IN_PROGRESS, APPROVED_WITH_CONDITIONS, REJECTED
    investigator_id: str = ""
    source_of_wealth_verified: bool = False
    source_of_wealth_notes: str = ""
    senior_management_approval_by: Optional[str] = None
    senior_management_approval_at: Optional[str] = None
    investigation_findings: str = ""
    mitigating_controls: List[str] = field(default_factory=list)
    created_at: str = field(default_factory=lambda: datetime.utcnow().isoformat())
    completed_at: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "case_id": self.case_id,
            "client_id": self.client_id,
            "trigger_reason": self.trigger_reason,
            "risk_level": self.risk_level,
            "status": self.status,
            "investigator_id": self.investigator_id,
            "source_of_wealth_verified": self.source_of_wealth_verified,
            "source_of_wealth_notes": self.source_of_wealth_notes,
            "senior_management_approval_by": self.senior_management_approval_by,
            "senior_management_approval_at": self.senior_management_approval_at,
            "investigation_findings": self.investigation_findings,
            "mitigating_controls": self.mitigating_controls,
            "created_at": self.created_at,
            "completed_at": self.completed_at
        }
