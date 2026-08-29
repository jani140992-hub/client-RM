"""
NexusCRM Onboarding API Controller.
Handles stage progression, milestone completion, and onboarding workflow endpoints.
"""

from typing import Dict, Any
from nexus.services.onboarding_service import OnboardingService
from nexus.services.workflow_engine import WorkflowEngine

class OnboardingController:
    @staticmethod
    def get_case(client_id: str) -> Dict[str, Any]:
        case = OnboardingService.get_case_by_client_id(client_id)
        if not case:
            return {"success": False, "error": f"No onboarding case found for client {client_id}"}, 404
        return {"success": True, "data": case}

    @staticmethod
    def advance_stage(body: Dict[str, Any]) -> Dict[str, Any]:
        case_id = body.get("case_id")
        if not case_id:
            return {"success": False, "error": "Missing case_id"}, 400

        actor_id = body.get("actor_id", "USR-RM-01")
        actor_role = body.get("actor_role", "RELATIONSHIP_MANAGER")
        notes = body.get("notes")

        try:
            updated_case = OnboardingService.advance_stage(case_id, actor_id, actor_role, notes)
            return {"success": True, "data": updated_case}
        except Exception as e:
            return {"success": False, "error": str(e)}, 400
