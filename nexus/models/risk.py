"""
NexusCRM Risk Assessment & Underwriting Models.
Multi-factor composite scoring models, credit ratings, and periodic review scheduling.
"""

from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any
from datetime import datetime

@dataclass
class RiskFactorBreakdown:
    factor_name: str  # e.g., "Geographic Risk", "Industry Sector", "Entity Structure", "PEP & Sanctions"
    raw_score: float  # 0.0 to 10.0
    weight: float  # 0.0 to 1.0
    weighted_score: float  # raw_score * weight
    rationale: str

    def to_dict(self) -> Dict[str, Any]:
        return {
            "factor_name": self.factor_name,
            "raw_score": self.raw_score,
            "weight": self.weight,
            "weighted_score": round(self.weighted_score, 2),
            "rationale": self.rationale
        }

@dataclass
class RiskAssessment:
    id: str
    client_id: str
    case_id: Optional[str]
    composite_score: float  # 0.0 to 10.0
    risk_tier: str  # LOW, MEDIUM, HIGH, PROHIBITED
    review_frequency_months: int  # 36 for LOW, 24 for MEDIUM, 12 for HIGH
    factors: List[RiskFactorBreakdown] = field(default_factory=list)
    has_overrides: bool = False
    override_reason: Optional[str] = None
    overridden_by: Optional[str] = None
    assessed_by: str = "AUTOMATED_ENGINE"
    approved_by: Optional[str] = None
    created_at: str = field(default_factory=lambda: datetime.utcnow().isoformat())

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "client_id": self.client_id,
            "case_id": self.case_id,
            "composite_score": round(self.composite_score, 2),
            "risk_tier": self.risk_tier,
            "review_frequency_months": self.review_frequency_months,
            "factors": [f.to_dict() for f in self.factors],
            "has_overrides": self.has_overrides,
            "override_reason": self.override_reason,
            "overridden_by": self.overridden_by,
            "assessed_by": self.assessed_by,
            "approved_by": self.approved_by,
            "created_at": self.created_at
        }
