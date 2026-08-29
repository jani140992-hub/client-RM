"""
Unit Tests for REST API Endpoints via Router.
"""

import unittest
from nexus.api.router import get_router

from nexus.database.connection import get_db_session
from nexus.database.migrations import run_migrations
from nexus.database.seed_data import seed_database

class TestAPIEndpoints(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with get_db_session() as conn:
            run_migrations(conn)
            seed_database(conn, num_clients=20)

    def setUp(self):
        self.router = get_router()

    def test_health_endpoint(self):
        status, body = self.router.route_request("GET", "/api/v1/health", {}, None)
        self.assertEqual(status, 200)
        self.assertEqual(body["status"], "healthy")

    def test_analytics_overview_endpoint(self):
        status, body = self.router.route_request("GET", "/api/v1/analytics/overview", {}, None)
        self.assertEqual(status, 200)
        self.assertTrue(body["success"])
        self.assertIn("total_clients", body["data"])

    def test_list_clients_endpoint(self):
        status, body = self.router.route_request("GET", "/api/v1/clients", {"limit": ["5"]}, None)
        self.assertEqual(status, 200)
        self.assertTrue(body["success"])
        self.assertLessEqual(len(body["data"]), 5)

    def test_screening_check_endpoint(self):
        status, body = self.router.route_request("POST", "/api/v1/screening/check", {}, {"name": "Viktor Sokolov"})
        self.assertEqual(status, 200)
        self.assertTrue(body["success"])
        self.assertTrue(body["has_matches"])

    def test_not_found_endpoint(self):
        status, body = self.router.route_request("GET", "/api/v1/nonexistent/route", {}, None)
        self.assertEqual(status, 404)
        self.assertFalse(body["success"])

if __name__ == "__main__":
    unittest.main()
