"""
NexusCRM Analytics API Controller.
Provides executive dashboard metrics, funnel velocity, and compliance SLA performance endpoints.
"""

from typing import Dict, Any
from nexus.services.reporting_service import ReportingService
from nexus.services.task_service import TaskService
from nexus.services.audit_service import AuditService

class AnalyticsController:
    @staticmethod
    def get_overview() -> Dict[str, Any]:
        data = ReportingService.get_dashboard_overview()
        return {"success": True, "data": data}

    @staticmethod
    def get_tasks(params: Dict[str, Any]) -> Dict[str, Any]:
        assigned = params.get("assigned_user", [None])[0]
        status = params.get("status", [None])[0]
        tasks = TaskService.get_tasks(assigned_user=assigned, status=status)
        return {"success": True, "count": len(tasks), "data": tasks}

    @staticmethod
    def get_audit_trail(params: Dict[str, Any]) -> Dict[str, Any]:
        ent_type = params.get("entity_type", [None])[0]
        ent_id = params.get("entity_id", [None])[0]
        limit = int(params.get("limit", [100])[0])
        events = AuditService.get_events(entity_type=ent_type, entity_id=ent_id, limit=limit)
        return {"success": True, "count": len(events), "data": events}
