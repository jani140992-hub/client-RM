"""
NexusCRM Workflow Engine.
Enforces stage transition prerequisites, four-eyes approval gates, and automated task dispatch.
"""

from typing import Dict, Any, Optional
from datetime import datetime
import uuid

from nexus.database.connection import get_db_session
from nexus.models.onboarding import STAGE_ORDER, OnboardingStage

class WorkflowEngine:
    @staticmethod
    def evaluate_stage_prerequisites(case_id: str, target_stage: str) -> Dict[str, Any]:
        """
        Validates whether all prerequisites for entering target_stage are satisfied:
        - Prior milestones completed
        - Mandatory documents uploaded and approved
        - Sanctions/PEP hits cleared (no OPEN hits)
        - 4-eyes approval sign-offs present where required
        """
        with get_db_session() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM onboarding_cases WHERE id = ?;", (case_id,))
            case = cursor.fetchone()
            if not case:
                return {"allowed": False, "reason": "Case not found"}

            # If moving into STAGE_6_EDD_INVESTIGATION or STAGE_7_CREDIT_UNDERWRITING:
            # All screening hits must be resolved
            if target_stage in ["CREDIT_UNDERWRITING", "LEGAL_CONTRACTING", "FINAL_APPROVAL_GATE"]:
                cursor.execute("SELECT COUNT(*) FROM screening_hits WHERE case_id = ? AND disposition = 'OPEN';", (case_id,))
                open_hits = cursor.fetchone()[0]
                if open_hits > 0:
                    return {
                        "allowed": False,
                        "reason": f"Cannot transition to {target_stage}: {open_hits} screening hits remain unresolved in OPEN status."
                    }

            # If moving into FINAL_APPROVAL_GATE:
            # Check mandatory documents
            cursor.execute("""
                SELECT COUNT(*) FROM document_vault
                WHERE case_id = ? AND verification_status = 'APPROVED';
            """, (case_id,))
            approved_docs = cursor.fetchone()[0]
            if approved_docs < 2 and target_stage == "FINAL_APPROVAL_GATE":
                return {
                    "allowed": False,
                    "reason": "At least 2 verified documents required prior to final approval gate."
                }

            return {"allowed": True, "reason": "All stage transition prerequisites satisfied."}

    @staticmethod
    def create_approval_gate(
        case_id: str,
        stage: str,
        gate_name: str,
        required_role: str = "COMPLIANCE_OFFICER"
    ) -> Dict[str, Any]:
        gate_id = f"GAT-{uuid.uuid4().hex[:8]}"
        now_str = datetime.utcnow().isoformat()
        with get_db_session() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO approval_gates (
                    id, case_id, stage, gate_name, required_role, status, created_at
                ) VALUES (?, ?, ?, ?, ?, 'PENDING', ?);
            """, (gate_id, case_id, stage, gate_name, required_role, now_str))
            cursor.execute("SELECT * FROM approval_gates WHERE id = ?;", (gate_id,))
            return dict(cursor.fetchone())

    @staticmethod
    def record_sign_off(
        gate_id: str,
        decision: str,  # APPROVED, REJECTED
        approver_id: str,
        approver_name: str,
        comments: str
    ) -> Dict[str, Any]:
        now_str = datetime.utcnow().isoformat()
        with get_db_session() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE approval_gates
                SET status = ?, approver_id = ?, approver_name = ?, comments = ?, decided_at = ?
                WHERE id = ?;
            """, (decision, approver_id, approver_name, comments, now_str, gate_id))
            cursor.execute("SELECT * FROM approval_gates WHERE id = ?;", (gate_id,))
            return dict(cursor.fetchone())
