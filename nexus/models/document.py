"""
NexusCRM Document Vault Models.
Document records, SHA-256 integrity proofs, verification statuses, and jurisdictional checklists.
"""

from dataclasses import dataclass, field
from typing import Optional, Dict, Any
from datetime import datetime

@dataclass
class DocumentRecord:
    id: str
    client_id: str
    case_id: Optional[str]
    document_type: str  # CERT_OF_INCORPORATION, REGISTER_OF_DIRECTORS, W8_W9_TAX_FORM, etc.
    title: str
    file_name: str
    file_size_bytes: int
    mime_type: str
    sha256_checksum: str
    verification_status: str = "PENDING_REVIEW"  # PENDING_REVIEW, APPROVED, REJECTED, EXPIRED
    verified_by: Optional[str] = None
    verified_at: Optional[str] = None
    rejection_reason: Optional[str] = None
    issue_date: Optional[str] = None
    expiry_date: Optional[str] = None  # None if perpetual
    is_certified_true_copy: bool = False
    is_apostilled: bool = False
    issuing_authority: Optional[str] = None
    issuing_country: str = "US"
    storage_uri: str = ""
    created_at: str = field(default_factory=lambda: datetime.utcnow().isoformat())

    def is_expired(self, current_date_iso: Optional[str] = None) -> bool:
        if not self.expiry_date:
            return False
        now_str = current_date_iso or datetime.utcnow().isoformat()[:10]
        return self.expiry_date < now_str

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "client_id": self.client_id,
            "case_id": self.case_id,
            "document_type": self.document_type,
            "title": self.title,
            "file_name": self.file_name,
            "file_size_bytes": self.file_size_bytes,
            "mime_type": self.mime_type,
            "sha256_checksum": self.sha256_checksum,
            "verification_status": self.verification_status,
            "verified_by": self.verified_by,
            "verified_at": self.verified_at,
            "rejection_reason": self.rejection_reason,
            "issue_date": self.issue_date,
            "expiry_date": self.expiry_date,
            "is_expired": self.is_expired(),
            "is_certified_true_copy": self.is_certified_true_copy,
            "is_apostilled": self.is_apostilled,
            "issuing_authority": self.issuing_authority,
            "issuing_country": self.issuing_country,
            "storage_uri": self.storage_uri,
            "created_at": self.created_at
        }
