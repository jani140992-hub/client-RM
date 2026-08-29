"""
Unit Tests for KYC/AML Screening Engine.
"""

import unittest
from nexus.catalogs.ofac_sdn_sanctions import get_ofac_search_engine, OFAC_SDN_RECORDS
from nexus.catalogs.pep_registry import get_pep_screening_engine, PEP_DATABASE
from nexus.services.kyc_aml_service import KYCAMLService
from nexus.database.connection import get_db_session

class TestKYCAMLEngine(unittest.TestCase):
    def setUp(self):
        self.ofac = get_ofac_search_engine()
        self.pep = get_pep_screening_engine()

    def test_ofac_exact_match(self):
        sample = list(OFAC_SDN_RECORDS.values())[0]
        results = self.ofac.search_name(sample.name, threshold=0.85)
        self.assertTrue(len(results) > 0)
        self.assertEqual(results[0]["name"], sample.name)
        self.assertGreaterEqual(results[0]["match_score"], 0.90)

    def test_pep_screening(self):
        sample_pep = list(PEP_DATABASE.values())[0]
        hits = self.pep.screen_individual(sample_pep.full_name, country_code=sample_pep.country_code)
        self.assertTrue(len(hits) > 0)
        self.assertEqual(hits[0]["full_name"], sample_pep.full_name)
        self.assertIn("role_title", hits[0])

    def test_clean_name_returns_no_hits(self):
        hits = self.ofac.search_name("Unrelated Nonexistent Person XYZ987", threshold=0.80)
        self.assertEqual(len(hits), 0)

if __name__ == "__main__":
    unittest.main()
