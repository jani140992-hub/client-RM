"""
NexusCRM Document Vault API Controller.
Handles document uploads, checklist matching, and verification status approvals.
"""

from typing import Dict, Any
from nexus.services.document_service import DocumentService

class DocumentController:
    @staticmethod
    def list_documents(client_id: str) -> Dict[str, Any]:
        docs = DocumentService.get_documents_by_client(client_id)
        checklist = DocumentService.get_jurisdictional_checklist_status(client_id)
        return {
            "success": True,
            "count": len(docs),
            "documents": docs,
            "checklist": checklist
        }

    @staticmethod
    def verify_document(body: Dict[str, Any]) -> Dict[str, Any]:
        doc_id = body.get("doc_id")
        status = body.get("status")  # APPROVED, REJECTED
        reviewer_id = body.get("reviewer_id", "USR-COMPLIANCE-01")
        reason = body.get("rejection_reason")

        if not doc_id or not status:
            return {"success": False, "error": "Missing doc_id or status"}, 400

        updated = DocumentService.update_verification_status(doc_id, status, reviewer_id, reason)
        return {"success": True, "data": updated}
