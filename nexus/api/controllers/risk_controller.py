"""
NexusCRM Risk API Controller.
Handles risk assessment calculation, factor decomposition, and dynamic review scheduling endpoints.
"""

from typing import Dict, Any
from nexus.services.risk_service import RiskService

class RiskController:
    @staticmethod
    def calculate_risk(body: Dict[str, Any]) -> Dict[str, Any]:
        client_id = body.get("client_id")
        case_id = body.get("case_id")
        if not client_id:
            return {"success": False, "error": "Missing client_id"}, 400

        result = RiskService.calculate_client_risk(client_id, case_id)
        return {"success": True, "data": result}
