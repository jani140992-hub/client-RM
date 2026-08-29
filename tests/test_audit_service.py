"""
Unit Tests for Audit Trail and Hash Chain.
"""

import unittest
from nexus.services.audit_service import AuditService
from nexus.database.connection import get_db_session
from nexus.database.migrations import run_migrations
from nexus.database.seed_data import seed_database

class TestAuditService(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with get_db_session() as conn:
            run_migrations(conn)
            seed_database(conn, num_clients=20)
    def test_log_event_hash_chain(self):
        ev1 = AuditService.log_event(
            entity_type="CLIENT",
            entity_id="CLI-TEST-01",
            action="CREATE",
            actor_id="USR-RM-01",
            actor_name="Test Actor",
            actor_role="RELATIONSHIP_MANAGER",
            change_summary="Initial prospect creation"
        )
        self.assertIsNotNone(ev1["event_hash"])
        self.assertEqual(len(ev1["event_hash"]), 64)

        ev2 = AuditService.log_event(
            entity_type="CLIENT",
            entity_id="CLI-TEST-01",
            action="UPDATE",
            actor_id="USR-RM-01",
            actor_name="Test Actor",
            actor_role="RELATIONSHIP_MANAGER",
            change_summary="Updated legal entity name"
        )
        # Prev hash of ev2 must equal hash of ev1
        self.assertEqual(ev2["prev_hash"], ev1["event_hash"])

if __name__ == "__main__":
    unittest.main()
