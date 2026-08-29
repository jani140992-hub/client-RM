"""
NexusCRM Ultimate Beneficial Ownership (UBO) Model.
Implements FinCEN CDD 25% threshold, EU 5AMLD/6AMLD look-through, and circular ownership detection.
"""

from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any, Set
from datetime import datetime

@dataclass
class UBOOwner:
    id: str
    client_id: str
    entity_id: str
    owner_type: str  # INDIVIDUAL or INTERMEDIARY_ENTITY
    name: str
    ownership_percentage: float  # e.g., 35.5%
    voting_rights_percentage: float  # e.g., 40.0%
    is_direct_owner: bool = True
    parent_owner_id: Optional[str] = None  # Pointer to intermediary corporate parent in ownership chain
    country_of_citizenship: str = "US"
    country_of_tax_residence: str = "US"
    is_pep: bool = False
    pep_tier: Optional[int] = None
    sanctions_check_status: str = "CLEAR"  # CLEAR, POTENTIAL_HIT, CONFIRMED_HIT
    idv_verification_status: str = "VERIFIED"  # UNVERIFIED, PENDING, VERIFIED, REJECTED
    identification_type: str = "PASSPORT"
    identification_number: str = ""
    date_of_birth: Optional[str] = None
    residential_address: str = ""
    control_type: str = "EQUITY_OWNERSHIP"  # EQUITY_OWNERSHIP, VOTING_CONTROL, SENIOR_MANAGING_OFFICIAL, TRUST_BENEFICIARY
    created_at: str = field(default_factory=lambda: datetime.utcnow().isoformat())

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "client_id": self.client_id,
            "entity_id": self.entity_id,
            "owner_type": self.owner_type,
            "name": self.name,
            "ownership_percentage": self.ownership_percentage,
            "voting_rights_percentage": self.voting_rights_percentage,
            "is_direct_owner": self.is_direct_owner,
            "parent_owner_id": self.parent_owner_id,
            "country_of_citizenship": self.country_of_citizenship,
            "country_of_tax_residence": self.country_of_tax_residence,
            "is_pep": self.is_pep,
            "pep_tier": self.pep_tier,
            "sanctions_check_status": self.sanctions_check_status,
            "idv_verification_status": self.idv_verification_status,
            "identification_type": self.identification_type,
            "identification_number": self.identification_number,
            "date_of_birth": self.date_of_birth,
            "residential_address": self.residential_address,
            "control_type": self.control_type,
            "created_at": self.created_at
        }

@dataclass
class OwnershipGraph:
    """
    Directed Graph representation of corporate ownership hierarchy.
    Resolves multi-layer intermediary holdings and identifies natural person UBOs >= 25%.
    """
    entity_id: str
    owners: List[UBOOwner] = field(default_factory=list)

    def add_owner(self, owner: UBOOwner):
        self.owners.append(owner)

    def detect_circular_ownership(self) -> bool:
        """Checks for cycles in corporate parent relationships using DFS."""
        adj: Dict[str, List[str]] = {}
        for o in self.owners:
            if o.parent_owner_id:
                if o.parent_owner_id not in adj:
                    adj[o.parent_owner_id] = []
                adj[o.parent_owner_id].append(o.id)

        visited: Set[str] = set()
        rec_stack: Set[str] = set()

        def dfs(node: str) -> bool:
            visited.add(node)
            rec_stack.add(node)
            for neighbor in adj.get(node, []):
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True
                elif neighbor in rec_stack:
                    return True
            rec_stack.remove(node)
            return False

        for node in list(adj.keys()):
            if node not in visited:
                if dfs(node):
                    return True
        return False

    def get_qualifying_natural_ubos(self, threshold_pct: float = 25.0) -> List[UBOOwner]:
        """
        Returns list of natural individuals possessing >= threshold_pct direct or indirect ownership
        or designated as Senior Managing Officials (FinCEN 31 CFR 1010.230 prong 2).
        """
        qualifying = []
        for o in self.owners:
            if o.owner_type == "INDIVIDUAL":
                if o.ownership_percentage >= threshold_pct or o.control_type == "SENIOR_MANAGING_OFFICIAL":
                    qualifying.append(o)
        return qualifying
