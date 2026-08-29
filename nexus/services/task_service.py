"""
NexusCRM Action Task Service.
Manages onboarding action items, team assignments, SLA deadline monitoring, and resolution workflows.
"""

import uuid
from typing import List, Dict, Optional, Any
from datetime import datetime, timedelta

from nexus.database.connection import get_db_session

class TaskService:
    @staticmethod
    def get_tasks(
        assigned_user: Optional[str] = None,
        status: Optional[str] = None,
        case_id: Optional[str] = None,
        limit: int = 50
    ) -> List[Dict[str, Any]]:
        with get_db_session() as conn:
            cursor = conn.cursor()
            query = """
                SELECT t.*, c.name as client_name, ob.case_number
                FROM action_tasks t
                JOIN clients c ON t.client_id = c.id
                JOIN onboarding_cases ob ON t.case_id = ob.id
                WHERE 1=1
            """
            params = []
            if assigned_user:
                query += " AND t.assigned_to_user_id = ?"
                params.append(assigned_user)
            if status:
                query += " AND t.status = ?"
                params.append(status)
            if case_id:
                query += " AND t.case_id = ?"
                params.append(case_id)

            query += " ORDER BY t.due_date ASC LIMIT ?;"
            params.append(limit)

            cursor.execute(query, params)
            return [dict(r) for r in cursor.fetchall()]

    @staticmethod
    def create_task(
        case_id: str,
        client_id: str,
        task_type: str,
        title: str,
        description: str,
        priority: str = "MEDIUM",
        assigned_user_id: str = "USR-COMPLIANCE-01",
        assigned_role: str = "COMPLIANCE_OFFICER",
        due_in_hours: float = 48.0
    ) -> Dict[str, Any]:
        task_id = f"TSK-{uuid.uuid4().hex[:8]}"
        now = datetime.utcnow()
        due_date = (now + timedelta(hours=due_in_hours)).isoformat()[:10]

        with get_db_session() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO action_tasks (
                    id, case_id, client_id, task_type, title, description,
                    priority, status, assigned_to_user_id, assigned_role,
                    due_date, is_sla_breached, created_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, 'OPEN', ?, ?, ?, 0, ?);
            """, (
                task_id, case_id, client_id, task_type, title, description,
                priority, assigned_user_id, assigned_role, due_date, now.isoformat()
            ))

            cursor.execute("SELECT * FROM action_tasks WHERE id = ?;", (task_id,))
            return dict(cursor.fetchone())

    @staticmethod
    def complete_task(task_id: str, resolution_notes: str) -> Dict[str, Any]:
        with get_db_session() as conn:
            cursor = conn.cursor()
            now_str = datetime.utcnow().isoformat()
            cursor.execute("""
                UPDATE action_tasks
                SET status = 'COMPLETED', resolution_notes = ?, completed_at = ?
                WHERE id = ?;
            """, (resolution_notes, now_str, task_id))
            cursor.execute("SELECT * FROM action_tasks WHERE id = ?;", (task_id,))
            return dict(cursor.fetchone())
