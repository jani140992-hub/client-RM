"""
NexusCRM Onboarding Case Service.
Manages the lifecycle of client onboarding cases across the 10 stages, milestones, and SLA monitoring.
"""

import sqlite3
import uuid
from typing import List, Dict, Optional, Any
from datetime import datetime, timedelta

from nexus.database.connection import get_db_session
from nexus.models.onboarding import STAGE_ORDER, OnboardingStage

class OnboardingService:
    @staticmethod
    def get_case_by_client_id(client_id: str) -> Optional[Dict[str, Any]]:
        with get_db_session() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT ob.*, c.name as client_name, c.client_number, c.risk_tier, c.client_segment,
                       rm.name as rm_name
                FROM onboarding_cases ob
                JOIN clients c ON ob.client_id = c.id
                LEFT JOIN relationship_managers rm ON ob.assigned_relationship_manager_id = rm.id
                WHERE ob.client_id = ?;
            """, (client_id,))
            row = cursor.fetchone()
            if not row:
                return None
            case_data = dict(row)

            # Milestones
            cursor.execute("SELECT * FROM case_milestones WHERE case_id = ? ORDER BY id ASC;", (case_data["id"],))
            case_data["milestones"] = [dict(m) for m in cursor.fetchall()]

            # Approval Gates
            cursor.execute("SELECT * FROM approval_gates WHERE case_id = ? ORDER BY created_at ASC;", (case_data["id"],))
            case_data["approval_gates"] = [dict(g) for g in cursor.fetchall()]

            # Screening Hits
            cursor.execute("SELECT * FROM screening_hits WHERE case_id = ? ORDER BY created_at DESC;", (case_data["id"],))
            case_data["screening_hits"] = [dict(h) for h in cursor.fetchall()]

            return case_data

    @staticmethod
    def initialize_case(client_id: str, rm_id: str, sla_hours: float = 336.0) -> Dict[str, Any]:
        case_id = f"CAS-{uuid.uuid4().hex[:8]}"
        case_number = f"ONB-2026-{uuid.uuid4().hex[:6].upper()}"
        now = datetime.utcnow()
        target_date = (now + timedelta(hours=sla_hours)).isoformat()[:10]

        with get_db_session() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO onboarding_cases (
                    id, client_id, case_number, current_stage, stage_index,
                    target_completion_date, sla_hours_budget, sla_hours_elapsed, sla_status,
                    is_edd_triggered, assigned_relationship_manager_id, completion_percentage,
                    created_at, updated_at
                ) VALUES (?, ?, ?, ?, 0, ?, ?, 0.0, 'GREEN', 0, ?, 0.0, ?, ?);
            """, (
                case_id, client_id, case_number, STAGE_ORDER[0].value,
                target_date, sla_hours, rm_id, now.isoformat(), now.isoformat()
            ))

            # Initialize Milestones
            for s_idx, st in enumerate(STAGE_ORDER[:10]):
                m_id = f"MLS-{case_id}-{s_idx}"
                cursor.execute("""
                    INSERT INTO case_milestones (id, case_id, stage, title, is_completed)
                    VALUES (?, ?, ?, ?, 0);
                """, (m_id, case_id, st.value, f"Complete requirements for {st.value.replace('_', ' ').title()}"))

        return OnboardingService.get_case_by_client_id(client_id)

    @staticmethod
    def advance_stage(case_id: str, actor_id: str, actor_role: str, notes: Optional[str] = None) -> Dict[str, Any]:
        with get_db_session() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM onboarding_cases WHERE id = ?;", (case_id,))
            case_row = cursor.fetchone()
            if not case_row:
                raise ValueError(f"Case {case_id} not found")
            
            curr_idx = case_row["stage_index"]
            if curr_idx >= len(STAGE_ORDER) - 1:
                return dict(case_row)  # Already at final stage

            next_idx = curr_idx + 1
            next_stage = STAGE_ORDER[next_idx].value
            now_str = datetime.utcnow().isoformat()

            # Mark milestone done
            cursor.execute("""
                UPDATE case_milestones
                SET is_completed = 1, completed_by = ?, completed_at = ?
                WHERE case_id = ? AND stage = ?;
            """, (actor_id, now_str, case_id, case_row["current_stage"]))

            # Calculate new percentage
            cursor.execute("SELECT COUNT(*), SUM(is_completed) FROM case_milestones WHERE case_id = ?;", (case_id,))
            total_m, done_m = cursor.fetchone()
            new_pct = round(((done_m or 0) / (total_m or 1)) * 100.0, 1)

            # If moving to COMPLETED, update client onboarding_status
            if next_stage == "COMPLETED":
                cursor.execute("""
                    UPDATE clients
                    SET onboarding_status = 'ACTIVE', onboarding_completed_date = ?, updated_at = ?
                    WHERE id = ?;
                """, (now_str, now_str, case_row["client_id"]))

            cursor.execute("""
                UPDATE onboarding_cases
                SET current_stage = ?, stage_index = ?, completion_percentage = ?, updated_at = ?
                WHERE id = ?;
            """, (next_stage, next_idx, new_pct, now_str, case_id))

        return OnboardingService.get_case_by_client_id(case_row["client_id"])
