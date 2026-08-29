"""
NexusCRM Screening API Controller.
Handles batch and real-time KYC/AML sanctions and PEP screening requests.
"""

from typing import Dict, Any
from nexus.services.kyc_aml_service import KYCAMLService
from nexus.catalogs.ofac_sdn_sanctions import get_ofac_search_engine
from nexus.catalogs.pep_registry import get_pep_screening_engine

class ScreeningController:
    @staticmethod
    def run_check(body: Dict[str, Any]) -> Dict[str, Any]:
        case_id = body.get("case_id")
        client_id = body.get("client_id")
        raw_name = body.get("name")

        # Ad-hoc individual name screening
        if raw_name:
            ofac_engine = get_ofac_search_engine()
            pep_engine = get_pep_screening_engine()
            ofac_hits = ofac_engine.search_name(raw_name, threshold=0.75)
            pep_hits = pep_engine.screen_individual(raw_name, threshold=0.70)
            return {
                "success": True,
                "query": raw_name,
                "ofac_hits": ofac_hits,
                "pep_hits": pep_hits,
                "has_matches": len(ofac_hits) > 0 or len(pep_hits) > 0
            }

        # Case-wide screening for client and all UBOs
        if not case_id or not client_id:
            return {"success": False, "error": "Either 'name' or ('case_id' and 'client_id') must be provided"}, 400

        result = KYCAMLService.screen_entity_and_ubos(case_id, client_id)
        return {"success": True, "data": result}

    @staticmethod
    def resolve_hit(body: Dict[str, Any]) -> Dict[str, Any]:
        hit_id = body.get("hit_id")
        disposition = body.get("disposition")  # CLEARED_FALSE_POSITIVE or CONFIRMED_TRUE_POSITIVE
        reviewer_id = body.get("reviewer_id", "USR-COMPLIANCE-01")
        rationale = body.get("rationale", "Verified false positive against secondary identity documents.")

        if not hit_id or not disposition:
            return {"success": False, "error": "Missing hit_id or disposition"}, 400

        updated = KYCAMLService.resolve_screening_hit(hit_id, disposition, reviewer_id, rationale)
        return {"success": True, "data": updated}
