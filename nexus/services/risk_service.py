"""
NexusCRM Risk & Underwriting Service.
Calculates multi-factor institutional risk scores, risk tiering, and dynamic review frequencies.
"""

import json
import uuid
from typing import Dict, Any, List
from datetime import datetime

from nexus.database.connection import get_db_session
from nexus.config import get_config
from nexus.catalogs.fatf_jurisdictions import calculate_jurisdiction_risk_score
from nexus.catalogs.industry_risk_codes import evaluate_industry_risk

class RiskService:
    @staticmethod
    def calculate_client_risk(client_id: str, case_id: str = None) -> Dict[str, Any]:
        config = get_config()
        weights = config.risk_weights

        with get_db_session() as conn:
            cursor = conn.cursor()

            # 1. Fetch Legal Entities & Jurisdictions
            cursor.execute("SELECT * FROM legal_entities WHERE client_id = ?;", (client_id,))
            entities = cursor.fetchall()
            jurisdictions = [e["jurisdiction_of_incorporation"] for e in entities]
            naics_codes = [e["primary_naics_code"] for e in entities if e["primary_naics_code"]]

            # 2. Fetch UBO countries
            cursor.execute("SELECT country_of_citizenship, country_of_tax_residence, is_pep FROM ubo_owners WHERE client_id = ?;", (client_id,))
            ubos = cursor.fetchall()
            for u in ubos:
                jurisdictions.append(u["country_of_citizenship"])
                jurisdictions.append(u["country_of_tax_residence"])

            # 3. Calculate Geographic Risk
            geo_score, geo_tier, geo_edd = calculate_jurisdiction_risk_score(jurisdictions)

            # 4. Calculate Industry Risk
            ind_result = evaluate_industry_risk(naics_codes)
            ind_score = ind_result["composite_score"]

            # 5. Entity Structure Risk
            etype_scores = {"CORPORATION": 3.0, "LLC": 4.5, "LIMITED_PARTNERSHIP": 5.0, "TRUST": 7.5, "SICAV_FUND": 4.0, "HEDGE_FUND": 6.5}
            ent_score = 4.0
            if entities:
                ent_score = max(etype_scores.get(e["entity_type"], 5.0) for e in entities)

            # 6. PEP & Sanctions Risk
            has_pep = any(u["is_pep"] for u in ubos)
            pep_score = 7.5 if has_pep else 1.5

            # 7. Product & Volume Risk (Default baseline 4.0)
            prod_score = 4.0

            # Composite Calculation
            composite = (
                geo_score * weights.country_risk_weight +
                ind_score * weights.industry_sector_weight +
                ent_score * weights.entity_structure_weight +
                pep_score * weights.pep_sanctions_weight +
                prod_score * weights.product_volume_weight
            )
            composite = round(min(10.0, max(1.0, composite)), 2)

            # Assign Tier and Interval
            if composite >= 8.5:
                tier = "PROHIBITED"
                review_months = 6
            elif composite >= 7.0:
                tier = "HIGH"
                review_months = 12
            elif composite >= 4.0:
                tier = "MEDIUM"
                review_months = 24
            else:
                tier = "LOW"
                review_months = 36

            factors = [
                {"factor_name": "Geographic Risk", "raw_score": geo_score, "weight": weights.country_risk_weight, "weighted_score": round(geo_score * weights.country_risk_weight, 2), "rationale": f"Analyzed countries: {set(jurisdictions)}"},
                {"factor_name": "Industry Risk", "raw_score": ind_score, "weight": weights.industry_sector_weight, "weighted_score": round(ind_score * weights.industry_sector_weight, 2), "rationale": f"Sector: {ind_result.get('risk_category')}"},
                {"factor_name": "Entity Structure", "raw_score": ent_score, "weight": weights.entity_structure_weight, "weighted_score": round(ent_score * weights.entity_structure_weight, 2), "rationale": "Corporate legal entity assessment"},
                {"factor_name": "PEP & Sanctions", "raw_score": pep_score, "weight": weights.pep_sanctions_weight, "weighted_score": round(pep_score * weights.pep_sanctions_weight, 2), "rationale": "PEP presence: " + str(has_pep)},
                {"factor_name": "Product Volume", "raw_score": prod_score, "weight": weights.product_volume_weight, "weighted_score": round(prod_score * weights.product_volume_weight, 2), "rationale": "Institutional banking products"}
            ]

            # Persist Risk Assessment
            ra_id = f"RSK-{uuid.uuid4().hex[:8]}"
            now_str = datetime.utcnow().isoformat()
            cursor.execute("""
                INSERT INTO risk_assessments (
                    id, client_id, case_id, composite_score, risk_tier, review_frequency_months,
                    factors_json, has_overrides, created_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, 0, ?);
            """, (
                ra_id, client_id, case_id, composite, tier, review_months,
                json.dumps(factors), now_str
            ))

            # Update Client record
            cursor.execute("""
                UPDATE clients
                SET risk_tier = ?, composite_risk_score = ?, kyc_refresh_frequency_months = ?, updated_at = ?
                WHERE id = ?;
            """, (tier, composite, review_months, now_str, client_id))

            return {
                "assessment_id": ra_id,
                "client_id": client_id,
                "composite_score": composite,
                "risk_tier": tier,
                "review_frequency_months": review_months,
                "factors": factors
            }
