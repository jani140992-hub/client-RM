"""
NexusCRM Document Vault Service.
Handles document ingestion, SHA-256 integrity verification, compliance review approvals, and checklist validation.
"""

import hashlib
import uuid
from typing import List, Dict, Optional, Any
from datetime import datetime

from nexus.database.connection import get_db_session
from nexus.catalogs.document_requirements_matrix import get_required_documents_for_entity

class DocumentService:
    @staticmethod
    def get_documents_by_client(client_id: str) -> List[Dict[str, Any]]:
        with get_db_session() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT * FROM document_vault
                WHERE client_id = ?
                ORDER BY created_at DESC;
            """, (client_id,))
            return [dict(r) for r in cursor.fetchall()]

    @staticmethod
    def upload_document(
        client_id: str,
        case_id: Optional[str],
        doc_type: str,
        title: str,
        file_name: str,
        file_bytes: bytes,
        mime_type: str = "application/pdf",
        issuing_country: str = "US",
        is_ctc: bool = False,
        is_apostilled: bool = False
    ) -> Dict[str, Any]:
        doc_id = f"DOC-{uuid.uuid4().hex[:8]}"
        sha256_hash = hashlib.sha256(file_bytes).hexdigest()
        file_size = len(file_bytes)
        now_str = datetime.utcnow().isoformat()

        with get_db_session() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO document_vault (
                    id, client_id, case_id, document_type, title, file_name,
                    file_size_bytes, mime_type, sha256_checksum, verification_status,
                    is_certified_true_copy, is_apostilled, issuing_country, storage_uri, created_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 'PENDING_REVIEW', ?, ?, ?, ?, ?);
            """, (
                doc_id, client_id, case_id, doc_type, title, file_name,
                file_size, mime_type, sha256_hash, 1 if is_ctc else 0,
                1 if is_apostilled else 0, issuing_country, f"vault://{client_id}/{doc_id}/{file_name}", now_str
            ))

            cursor.execute("SELECT * FROM document_vault WHERE id = ?;", (doc_id,))
            return dict(cursor.fetchone())

    @staticmethod
    def update_verification_status(
        doc_id: str,
        status: str,  # APPROVED, REJECTED
        reviewer_id: str,
        rejection_reason: Optional[str] = None
    ) -> Dict[str, Any]:
        with get_db_session() as conn:
            cursor = conn.cursor()
            now_str = datetime.utcnow().isoformat()
            cursor.execute("""
                UPDATE document_vault
                SET verification_status = ?, verified_by = ?, verified_at = ?, rejection_reason = ?
                WHERE id = ?;
            """, (status, reviewer_id, now_str, rejection_reason, doc_id))
            cursor.execute("SELECT * FROM document_vault WHERE id = ?;", (doc_id,))
            return dict(cursor.fetchone())

    @staticmethod
    def get_jurisdictional_checklist_status(client_id: str) -> Dict[str, Any]:
        with get_db_session() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM legal_entities WHERE client_id = ? LIMIT 1;", (client_id,))
            ent = cursor.fetchone()
            if not ent:
                return {"requirements": [], "all_mandatory_satisfied": False}

            reqs = get_required_documents_for_entity(ent["jurisdiction_of_incorporation"], ent["entity_type"])
            cursor.execute("SELECT document_type, verification_status FROM document_vault WHERE client_id = ?;", (client_id,))
            docs = cursor.fetchall()
            uploaded_status = {d["document_type"]: d["verification_status"] for d in docs}

            checklist = []
            all_satisfied = True

            for r in reqs:
                v_stat = uploaded_status.get(r.code, "MISSING")
                is_ok = (v_stat == "APPROVED")
                if r.is_mandatory and not is_ok:
                    all_satisfied = False

                checklist.append({
                    "code": r.code,
                    "title": r.title,
                    "is_mandatory": r.is_mandatory,
                    "validity_days": r.validity_days,
                    "status": v_stat,
                    "satisfied": is_ok
                })

            return {
                "jurisdiction": ent["jurisdiction_of_incorporation"],
                "entity_type": ent["entity_type"],
                "requirements": checklist,
                "all_mandatory_satisfied": all_satisfied
            }
