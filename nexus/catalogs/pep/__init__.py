"""
PEP Master Registry Aggregator.
"""

from typing import Dict, Any, List, Optional, Set
import re

from nexus.catalogs.pep.tier1_heads_of_state import PEP_RECORDS_TIER1_HEADS_OF_STATE, PEPProfile
from nexus.catalogs.pep.tier1_finance_ministers import PEP_RECORDS_TIER1_FINANCE_MINISTERS, PEPProfile
from nexus.catalogs.pep.tier1_central_bankers import PEP_RECORDS_TIER1_CENTRAL_BANKERS, PEPProfile
from nexus.catalogs.pep.tier1_defense_ministers import PEP_RECORDS_TIER1_DEFENSE_MINISTERS, PEPProfile
from nexus.catalogs.pep.tier2_legislative_leaders import PEP_RECORDS_TIER2_LEGISLATIVE_LEADERS, PEPProfile
from nexus.catalogs.pep.tier2_supreme_judges import PEP_RECORDS_TIER2_SUPREME_JUDGES, PEPProfile
from nexus.catalogs.pep.tier2_soe_executives import PEP_RECORDS_TIER2_SOE_EXECUTIVES, PEPProfile
from nexus.catalogs.pep.tier3_regional_associates import PEP_RECORDS_TIER3_REGIONAL_ASSOCIATES, PEPProfile

PEP_DATABASE: Dict[str, Any] = {}
PEP_DATABASE.update(PEP_RECORDS_TIER1_HEADS_OF_STATE)
PEP_DATABASE.update(PEP_RECORDS_TIER1_FINANCE_MINISTERS)
PEP_DATABASE.update(PEP_RECORDS_TIER1_CENTRAL_BANKERS)
PEP_DATABASE.update(PEP_RECORDS_TIER1_DEFENSE_MINISTERS)
PEP_DATABASE.update(PEP_RECORDS_TIER2_LEGISLATIVE_LEADERS)
PEP_DATABASE.update(PEP_RECORDS_TIER2_SUPREME_JUDGES)
PEP_DATABASE.update(PEP_RECORDS_TIER2_SOE_EXECUTIVES)
PEP_DATABASE.update(PEP_RECORDS_TIER3_REGIONAL_ASSOCIATES)

class PEPScreeningEngine:
    def __init__(self, database=None):
        self.db = database or PEP_DATABASE
        self._name_index: Dict[str, Set[str]] = {}
        self._build_index()

    def _clean(self, s: str) -> str:
        if not s:
            return ""
        return re.sub(r'[^a-zA-Z0-9 ]', '', s).upper().strip()

    def _build_index(self):
        for pid, pep in self.db.items():
            tokens = set(self._clean(pep.full_name).split())
            for a in pep.aliases:
                tokens.update(self._clean(a).split())
            for t in tokens:
                if len(t) > 1:
                    if t not in self._name_index:
                        self._name_index[t] = set()
                    self._name_index[t].add(pid)

    def screen_individual(self, name: str, country_code: Optional[str] = None, threshold: float = 0.70) -> List[Dict[str, Any]]:
        clean_name = self._clean(name)
        tokens = set(clean_name.split())
        if not tokens:
            return []

        candidates = set()
        for t in tokens:
            if t in self._name_index:
                candidates.update(self._name_index[t])

        if len(candidates) < 5:
            candidates.update(list(self.db.keys())[:200])

        hits = []
        for cid in candidates:
            pep = self.db[cid]
            clean_target = self._clean(pep.full_name)
            if clean_name == clean_target:
                score = 1.0
            elif clean_name in clean_target or clean_target in clean_name:
                score = 0.90
            else:
                target_tokens = set(clean_target.split())
                inter = tokens.intersection(target_tokens)
                union = tokens.union(target_tokens)
                score = len(inter) / len(union) if union else 0.0

            if score >= threshold:
                hits.append({
                    "pep_id": pep.pep_id,
                    "full_name": pep.full_name,
                    "country_code": pep.country_code,
                    "country_name": pep.country_name,
                    "tier": pep.tier,
                    "role_title": pep.role_title,
                    "department_or_agency": pep.department_or_agency,
                    "risk_score": pep.risk_score,
                    "match_score": round(score, 3)
                })

        hits.sort(key=lambda x: x["match_score"], reverse=True)
        return hits

_pep_engine_instance = None

def get_pep_screening_engine() -> PEPScreeningEngine:
    global _pep_engine_instance
    if _pep_engine_instance is None:
        _pep_engine_instance = PEPScreeningEngine()
    return _pep_engine_instance
