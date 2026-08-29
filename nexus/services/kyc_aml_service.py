"""
NexusCRM KYC/AML Screening Service.
Runs fuzzy name and identification screening against OFAC SDN, PEP, and international sanctions catalogs.
"""

import uuid
from typing import List, Dict, Optional, Any
from datetime import datetime

from nexus.database.connection import get_db_session
from nexus.catalogs.ofac_sdn_sanctions import get_ofac_search_engine
from nexus.catalogs.pep_registry import get_pep_screening_engine
from nexus.catalogs.fatf_jurisdictions import get_country_risk, calculate_jurisdiction_risk_score

class KYCAMLService:
    @staticmethod
    def screen_entity_and_ubos(case_id: str, client_id: str) -> Dict[str, Any]:
        ofac_engine = get_ofac_search_engine()
        pep_engine = get_pep_screening_engine()

        hits_generated = []

        with get_db_session() as conn:
            cursor = conn.cursor()

            # 1. Screen Legal Entities
            cursor.execute("SELECT * FROM legal_entities WHERE client_id = ?;", (client_id,))
            entities = cursor.fetchall()
            for ent in entities:
                ent_hits = ofac_engine.search_name(ent["legal_name"], threshold=0.75)
                for h in ent_hits:
                    hit_id = f"HIT-{uuid.uuid4().hex[:8]}"
                    now_str = datetime.utcnow().isoformat()
                    cursor.execute("""
                        INSERT INTO screening_hits (
                            id, case_id, subject_name, subject_type, catalog_source,
                            hit_reference_id, matched_name, match_score, programs_or_tier,
                            disposition, created_at
                        ) VALUES (?, ?, ?, 'CORPORATE_ENTITY', 'OFAC_SDN', ?, ?, ?, ?, 'OPEN', ?);
                    """, (
                        hit_id, case_id, ent["legal_name"], str(h["sdn_id"]),
                        h["name"], h["match_score"], ", ".join(h["programs"]), now_str
                    ))
                    hits_generated.append({"hit_id": hit_id, "subject": ent["legal_name"], "source": "OFAC_SDN", "score": h["match_score"]})

            # 2. Screen Contacts and UBOs
            cursor.execute("SELECT * FROM ubo_owners WHERE client_id = ?;", (client_id,))
            ubos = cursor.fetchall()
            for u in ubos:
                # Screen against OFAC
                u_ofac = ofac_engine.search_name(u["name"], threshold=0.78)
                for h in u_ofac:
                    hit_id = f"HIT-{uuid.uuid4().hex[:8]}"
                    now_str = datetime.utcnow().isoformat()
                    cursor.execute("""
                        INSERT INTO screening_hits (
                            id, case_id, subject_name, subject_type, catalog_source,
                            hit_reference_id, matched_name, match_score, programs_or_tier,
                            disposition, created_at
                        ) VALUES (?, ?, ?, 'UBO', 'OFAC_SDN', ?, ?, ?, ?, 'OPEN', ?);
                    """, (
                        hit_id, case_id, u["name"], str(h["sdn_id"]),
                        h["name"], h["match_score"], ", ".join(h["programs"]), now_str
                    ))
                    hits_generated.append({"hit_id": hit_id, "subject": u["name"], "source": "OFAC_SDN", "score": h["match_score"]})

                # Screen against PEP
                u_pep = pep_engine.screen_individual(u["name"], country_code=u["country_of_citizenship"], threshold=0.72)
                for p in u_pep:
                    hit_id = f"HIT-{uuid.uuid4().hex[:8]}"
                    now_str = datetime.utcnow().isoformat()
                    cursor.execute("""
                        INSERT INTO screening_hits (
                            id, case_id, subject_name, subject_type, catalog_source,
                            hit_reference_id, matched_name, match_score, programs_or_tier,
                            disposition, created_at
                        ) VALUES (?, ?, ?, 'UBO', 'PEP_REGISTRY', ?, ?, ?, ?, 'OPEN', ?);
                    """, (
                        hit_id, case_id, u["name"], p["pep_id"],
                        p["full_name"], p["match_score"], f"Tier {p['tier']} - {p['role_title']}", now_str
                    ))
                    hits_generated.append({"hit_id": hit_id, "subject": u["name"], "source": "PEP_REGISTRY", "score": p["match_score"]})

            # Check if EDD trigger is required
            if any(h["score"] >= 0.85 for h in hits_generated):
                cursor.execute("UPDATE onboarding_cases SET is_edd_triggered = 1 WHERE id = ?;", (case_id,))

        return {
            "case_id": case_id,
            "total_hits_found": len(hits_generated),
            "hits": hits_generated,
            "edd_triggered": len(hits_generated) > 0
        }

    @staticmethod
    def resolve_screening_hit(
        hit_id: str,
        disposition: str,
        reviewer_id: str,
        rationale: str
    ) -> Dict[str, Any]:
        with get_db_session() as conn:
            cursor = conn.cursor()
            now_str = datetime.utcnow().isoformat()
            cursor.execute("""
                UPDATE screening_hits
                SET disposition = ?, reviewed_by = ?, reviewed_at = ?, clearance_rationale = ?
                WHERE id = ?;
            """, (disposition, reviewer_id, now_str, rationale, hit_id))
            cursor.execute("SELECT * FROM screening_hits WHERE id = ?;", (hit_id,))
            return dict(cursor.fetchone())
