"""
NexusCRM Client API Controller.
Handles client listing, search, retrieval, and registration endpoints.
"""

from typing import Dict, Any
from nexus.services.client_service import ClientService

class ClientController:
    @staticmethod
    def list_clients(query_params: Dict[str, Any]) -> Dict[str, Any]:
        search = query_params.get("search", [None])[0]
        status = query_params.get("status", [None])[0]
        risk_tier = query_params.get("risk_tier", [None])[0]
        limit = int(query_params.get("limit", [50])[0])
        offset = int(query_params.get("offset", [0])[0])

        clients = ClientService.get_all_clients(
            search_query=search,
            status=status,
            risk_tier=risk_tier,
            limit=limit,
            offset=offset
        )
        return {
            "success": True,
            "count": len(clients),
            "data": clients
        }

    @staticmethod
    def get_client(client_id: str) -> Dict[str, Any]:
        client = ClientService.get_client_by_id(client_id)
        if not client:
            return {"success": False, "error": f"Client {client_id} not found"}, 404
        return {"success": True, "data": client}

    @staticmethod
    def create_client(body: Dict[str, Any]) -> Dict[str, Any]:
        required = ["name", "client_segment", "jurisdiction", "entity_type"]
        for r in required:
            if r not in body:
                return {"success": False, "error": f"Missing required parameter: {r}"}, 400

        client = ClientService.create_client(
            name=body["name"],
            client_segment=body["client_segment"],
            rm_id=body.get("rm_id", "RM-101"),
            jurisdiction=body["jurisdiction"],
            entity_type=body["entity_type"],
            naics_code=body.get("naics_code", "522110"),
            tags=body.get("tags", [])
        )
        return {"success": True, "data": client}, 201
