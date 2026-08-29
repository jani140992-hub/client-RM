"""
Unit Tests for Document Vault and Verification.
"""

import unittest
from nexus.services.client_service import ClientService
from nexus.services.document_service import DocumentService
from nexus.database.connection import get_db_session
from nexus.database.migrations import run_migrations
from nexus.database.seed_data import seed_database

class TestDocumentVault(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with get_db_session() as conn:
            run_migrations(conn)
            seed_database(conn, num_clients=20)
    def test_document_upload_and_verify(self):
        client = ClientService.create_client(
            name="Vault Document Test Ltd",
            client_segment="FAMILY_OFFICE",
            rm_id="RM-101",
            jurisdiction="KY",
            entity_type="LIMITED_PARTNERSHIP"
        )
        fake_content = b"PDF-1.4 Mock Institutional Certificate of Incumbency and Register of Directors"
        doc = DocumentService.upload_document(
            client_id=client["id"],
            case_id=None,
            doc_type="CERT_OF_INCORPORATION",
            title="Certificate of Incorporation",
            file_name="cert_incorp.pdf",
            file_bytes=fake_content,
            issuing_country="KY"
        )
        self.assertEqual(doc["verification_status"], "PENDING_REVIEW")
        self.assertEqual(len(doc["sha256_checksum"]), 64)

        # Verify document
        verified = DocumentService.update_verification_status(
            doc["id"],
            status="APPROVED",
            reviewer_id="USR-COMPLIANCE-01"
        )
        self.assertEqual(verified["verification_status"], "APPROVED")
        self.assertEqual(verified["verified_by"], "USR-COMPLIANCE-01")

if __name__ == "__main__":
    unittest.main()
