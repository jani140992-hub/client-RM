"""
Unit Tests for Risk Engine and Scoring Decomposition.
"""

import unittest
from nexus.catalogs.fatf_jurisdictions import calculate_jurisdiction_risk_score, is_jurisdiction_prohibited
from nexus.catalogs.industry_risk_codes import evaluate_industry_risk
from nexus.services.risk_service import RiskService
from nexus.services.client_service import ClientService

class TestRiskEngine(unittest.TestCase):
    def test_prohibited_jurisdiction(self):
        self.assertTrue(is_jurisdiction_prohibited("KP"))  # North Korea
        self.assertTrue(is_jurisdiction_prohibited("IR"))  # Iran
        self.assertFalse(is_jurisdiction_prohibited("US"))

    def test_country_risk_composite(self):
        score, tier, edd = calculate_jurisdiction_risk_score(["US", "GB"])
        self.assertEqual(tier, "LOW")
        self.assertFalse(edd)

        # Mixing with blacklisted jurisdiction
        score_high, tier_high, edd_high = calculate_jurisdiction_risk_score(["US", "KP"])
        self.assertEqual(tier_high, "PROHIBITED")
        self.assertTrue(edd_high)

    def test_industry_risk_evaluation(self):
        res = evaluate_industry_risk(["523910"])  # Crypto VASP
        self.assertTrue(res["requires_edd"])
        self.assertGreaterEqual(res["composite_score"], 8.0)

if __name__ == "__main__":
    unittest.main()
