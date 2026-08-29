"""
Sanctions Master Registry Aggregator.
"""

from typing import Dict, Any, List, Optional, Set
import re

from nexus.catalogs.sanctions.sdgt_terrorist_entities import RECORDS_SDGT_TERRORIST_ENTITIES, SanctionedItem
from nexus.catalogs.sanctions.eastern_europe_sanctions import RECORDS_EASTERN_EUROPE_SANCTIONS, SanctionedItem
from nexus.catalogs.sanctions.middle_east_sanctions import RECORDS_MIDDLE_EAST_SANCTIONS, SanctionedItem
from nexus.catalogs.sanctions.east_asia_sanctions import RECORDS_EAST_ASIA_SANCTIONS, SanctionedItem
from nexus.catalogs.sanctions.latin_america_sanctions import RECORDS_LATIN_AMERICA_SANCTIONS, SanctionedItem
from nexus.catalogs.sanctions.maritime_vessels_sanctions import RECORDS_MARITIME_VESSELS_SANCTIONS, SanctionedItem
from nexus.catalogs.sanctions.cyber_transnational_sanctions import RECORDS_CYBER_TRANSNATIONAL_SANCTIONS, SanctionedItem
from nexus.catalogs.sanctions.global_magnitsky_sanctions import RECORDS_GLOBAL_MAGNITSKY_SANCTIONS, SanctionedItem

OFAC_SDN_RECORDS: Dict[int, Any] = {}
OFAC_SDN_RECORDS.update(RECORDS_SDGT_TERRORIST_ENTITIES)
OFAC_SDN_RECORDS.update(RECORDS_EASTERN_EUROPE_SANCTIONS)
OFAC_SDN_RECORDS.update(RECORDS_MIDDLE_EAST_SANCTIONS)
OFAC_SDN_RECORDS.update(RECORDS_EAST_ASIA_SANCTIONS)
OFAC_SDN_RECORDS.update(RECORDS_LATIN_AMERICA_SANCTIONS)
OFAC_SDN_RECORDS.update(RECORDS_MARITIME_VESSELS_SANCTIONS)
OFAC_SDN_RECORDS.update(RECORDS_CYBER_TRANSNATIONAL_SANCTIONS)
OFAC_SDN_RECORDS.update(RECORDS_GLOBAL_MAGNITSKY_SANCTIONS)

class OFACSearchEngine:
    def __init__(self, records=None):
        self.records = records or OFAC_SDN_RECORDS
        self._name_index: Dict[str, Set[int]] = {}
        self._build_indices()

    def _clean_string(self, text: str) -> str:
        if not text:
            return ""
        return re.sub(r'[^a-zA-Z0-9 ]', '', text).upper().strip()

    def _tokenize(self, text: str) -> Set[str]:
        cleaned = self._clean_string(text)
        stopwords = {"THE", "LLC", "INC", "CORP", "LTD", "LIMITED", "SA", "GMBH", "AND", "CO"}
        return {t for t in cleaned.split() if len(t) > 1 and t not in stopwords}

    def _build_indices(self):
        for sdn_id, entity in self.records.items():
            tokens = self._tokenize(entity.name)
            for alias in entity.aliases:
                tokens.update(self._tokenize(alias))
            for t in tokens:
                if t not in self._name_index:
                    self._name_index[t] = set()
                self._name_index[t].add(sdn_id)

    def _levenshtein_ratio(self, s1: str, s2: str) -> float:
        if s1 == s2:
            return 1.0
        if not s1 or not s2:
            return 0.0
        len1, len2 = len(s1), len(s2)
        dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]
        for i in range(len1 + 1):
            dp[i][0] = i
        for j in range(len2 + 1):
            dp[0][j] = j
        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                cost = 0 if s1[i - 1] == s2[j - 1] else 1
                dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + cost)
        distance = dp[len1][len2]
        return max(0.0, 1.0 - (distance / max(len1, len2)))

    def search_name(self, query: str, threshold: float = 0.75, max_results: int = 15) -> List[Dict[str, Any]]:
        clean_query = self._clean_string(query)
        tokens = self._tokenize(query)
        if not tokens:
            return []

        candidates = set()
        for t in tokens:
            if t in self._name_index:
                candidates.update(self._name_index[t])

        if len(candidates) < 5:
            candidates.update(list(self.records.keys())[:250])

        results = []
        for cid in candidates:
            entity = self.records[cid]
            names_to_check = [entity.name] + entity.aliases
            best_score = 0.0
            matched_on = entity.name

            for n in names_to_check:
                clean_target = self._clean_string(n)
                if clean_query == clean_target:
                    score = 1.0
                elif clean_query in clean_target or clean_target in clean_query:
                    score = 0.92
                else:
                    score = self._levenshtein_ratio(clean_query, clean_target)

                if score > best_score:
                    best_score = score
                    matched_on = n

            if best_score >= threshold:
                results.append({
                    "sdn_id": entity.sdn_id,
                    "name": entity.name,
                    "sdn_type": entity.sdn_type,
                    "programs": entity.programs,
                    "match_score": round(best_score, 3),
                    "matched_string": matched_on,
                    "remarks": entity.remarks
                })

        results.sort(key=lambda x: x["match_score"], reverse=True)
        return results[:max_results]

_engine_instance = None

def get_ofac_search_engine() -> OFACSearchEngine:
    global _engine_instance
    if _engine_instance is None:
        _engine_instance = OFACSearchEngine()
    return _engine_instance
