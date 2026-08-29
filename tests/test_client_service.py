"""
Unit Tests for NexusCRM Client Service.
"""

import unittest
from nexus.database.connection import get_db_session
from nexus.database.migrations import run_migrations
from nexus.services.client_service import ClientService

class TestClientService(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with get_db_session() as conn:
            run_migrations(conn)

    def test_create_and_retrieve_client(self):
        client = ClientService.create_client(
            name="Apex Horizon Capital Corp",
            client_segment="INSTITUTIONAL_BANKING",
            rm_id="RM-101",
            jurisdiction="US",
            entity_type="CORPORATION",
            naics_code="522110"
        )
        self.assertIsNotNone(client)
        self.assertEqual(client["name"], "Apex Horizon Capital Corp")
        self.assertEqual(client["client_segment"], "INSTITUTIONAL_BANKING")
        self.assertTrue(len(client["legal_entities"]) > 0)
        self.assertEqual(client["legal_entities"][0]["jurisdiction_of_incorporation"], "US")

    def test_search_clients(self):
        clients = ClientService.get_all_clients(search_query="Apex", limit=10)
        self.assertTrue(len(clients) > 0)
        self.assertIn("Apex", clients[0]["name"])

if __name__ == "__main__":
    unittest.main()
