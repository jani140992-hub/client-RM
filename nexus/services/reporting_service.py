"""
NexusCRM Analytics & Pipeline Reporting Service.
Aggregates key onboarding funnel metrics, SLA breaches, risk tier distribution, and velocity KPIs.
"""

from typing import Dict, Any, List
from nexus.database.connection import get_db_session

class ReportingService:
    @staticmethod
    def get_dashboard_overview() -> Dict[str, Any]:
        with get_db_session() as conn:
            cursor = conn.cursor()

            # 1. Total Clients count
            cursor.execute("SELECT COUNT(*) FROM clients;")
            total_clients = cursor.fetchone()[0]

            # 2. Active Onboarding Funnel count
            cursor.execute("SELECT COUNT(*) FROM onboarding_cases WHERE current_stage != 'COMPLETED';")
            active_onboardings = cursor.fetchone()[0]

            # 3. Completed Onboardings count
            cursor.execute("SELECT COUNT(*) FROM onboarding_cases WHERE current_stage = 'COMPLETED';")
            completed_onboardings = cursor.fetchone()[0]

            # 4. SLA Status Breakdown
            cursor.execute("""
                SELECT sla_status, COUNT(*)
                FROM onboarding_cases
                WHERE current_stage != 'COMPLETED'
                GROUP BY sla_status;
            """)
            sla_breakdown = {row[0]: row[1] for row in cursor.fetchall()}

            # 5. Risk Tier Distribution
            cursor.execute("""
                SELECT risk_tier, COUNT(*)
                FROM clients
                GROUP BY risk_tier;
            """)
            risk_distribution = {row[0]: row[1] for row in cursor.fetchall()}

            # 6. Stage Funnel Counts
            cursor.execute("""
                SELECT current_stage, COUNT(*)
                FROM onboarding_cases
                GROUP BY current_stage;
            """)
            stage_distribution = {row[0]: row[1] for row in cursor.fetchall()}

            # 7. Open Compliance Screening Hits
            cursor.execute("SELECT COUNT(*) FROM screening_hits WHERE disposition = 'OPEN';")
            open_screening_hits = cursor.fetchone()[0]

            # 8. Pending Tasks count
            cursor.execute("SELECT COUNT(*) FROM action_tasks WHERE status = 'OPEN';")
            pending_tasks = cursor.fetchone()[0]

            return {
                "total_clients": total_clients,
                "active_onboardings": active_onboardings,
                "completed_onboardings": completed_onboardings,
                "open_screening_hits": open_screening_hits,
                "pending_tasks": pending_tasks,
                "sla_breakdown": {
                    "GREEN": sla_breakdown.get("GREEN", 0),
                    "AMBER": sla_breakdown.get("AMBER", 0),
                    "RED": sla_breakdown.get("RED", 0)
                },
                "risk_tier_distribution": {
                    "LOW": risk_distribution.get("LOW", 0),
                    "MEDIUM": risk_distribution.get("MEDIUM", 0),
                    "HIGH": risk_distribution.get("HIGH", 0),
                    "PROHIBITED": risk_distribution.get("PROHIBITED", 0)
                },
                "stage_funnel": stage_distribution
            }
