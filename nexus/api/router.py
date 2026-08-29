"""
NexusCRM Request Dispatcher and HTTP Router.
Directs incoming REST requests to designated controllers with automatic parameter parsing and error serialization.
"""

import re
import json
from typing import Dict, Any, Tuple, Optional, Callable
from urllib.parse import parse_qs, urlparse

from nexus.api.controllers import (
    ClientController,
    OnboardingController,
    ScreeningController,
    RiskController,
    DocumentController,
    AnalyticsController,
    AuthController
)

class APIRouter:
    def __init__(self):
        # Maps (METHOD, regex_pattern) -> handler_function
        self.routes = []
        self._register_routes()

    def _add_route(self, method: str, pattern: str, handler: Callable):
        regex = re.compile(f"^{pattern}$")
        self.routes.append((method.upper(), regex, handler))

    def _register_routes(self):
        # Health & Meta
        self._add_route("GET", r"/api/v1/health", self._handle_health)
        self._add_route("GET", r"/api/v1/auth/me", lambda p, q, b: (200, AuthController.get_current_user()))

        # Analytics & Metrics
        self._add_route("GET", r"/api/v1/analytics/overview", lambda p, q, b: (200, AnalyticsController.get_overview()))
        self._add_route("GET", r"/api/v1/tasks", lambda p, q, b: (200, AnalyticsController.get_tasks(q)))
        self._add_route("GET", r"/api/v1/audit/trail", lambda p, q, b: (200, AnalyticsController.get_audit_trail(q)))

        # Clients
        self._add_route("GET", r"/api/v1/clients", lambda p, q, b: (200, ClientController.list_clients(q)))
        self._add_route("POST", r"/api/v1/clients", self._handle_create_client)
        self._add_route("GET", r"/api/v1/clients/(?P<id>[a-zA-Z0-9_\-]+)", self._handle_get_client)

        # Onboarding Cases
        self._add_route("GET", r"/api/v1/onboarding/(?P<id>[a-zA-Z0-9_\-]+)", self._handle_get_case)
        self._add_route("POST", r"/api/v1/onboarding/advance", self._handle_advance_stage)

        # Screening
        self._add_route("POST", r"/api/v1/screening/check", self._handle_screening_check)
        self._add_route("POST", r"/api/v1/screening/resolve", self._handle_resolve_hit)

        # Risk
        self._add_route("POST", r"/api/v1/risk/calculate", self._handle_calculate_risk)

        # Documents
        self._add_route("GET", r"/api/v1/documents/(?P<id>[a-zA-Z0-9_\-]+)", self._handle_list_documents)
        self._add_route("POST", r"/api/v1/documents/verify", self._handle_verify_document)

    def _handle_health(self, params, query, body):
        return 200, {
            "status": "healthy",
            "version": "3.4.0-enterprise",
            "system": "NexusCRM Institutional Onboarding Platform"
        }

    def _handle_get_client(self, params, query, body):
        res = ClientController.get_client(params["id"])
        if isinstance(res, tuple):
            return res[1], res[0]
        return 200, res

    def _handle_create_client(self, params, query, body):
        res = ClientController.create_client(body or {})
        if isinstance(res, tuple):
            return res[1], res[0]
        return 200, res

    def _handle_get_case(self, params, query, body):
        res = OnboardingController.get_case(params["id"])
        if isinstance(res, tuple):
            return res[1], res[0]
        return 200, res

    def _handle_advance_stage(self, params, query, body):
        res = OnboardingController.advance_stage(body or {})
        if isinstance(res, tuple):
            return res[1], res[0]
        return 200, res

    def _handle_screening_check(self, params, query, body):
        res = ScreeningController.run_check(body or {})
        if isinstance(res, tuple):
            return res[1], res[0]
        return 200, res

    def _handle_resolve_hit(self, params, query, body):
        res = ScreeningController.resolve_hit(body or {})
        if isinstance(res, tuple):
            return res[1], res[0]
        return 200, res

    def _handle_calculate_risk(self, params, query, body):
        res = RiskController.calculate_risk(body or {})
        if isinstance(res, tuple):
            return res[1], res[0]
        return 200, res

    def _handle_list_documents(self, params, query, body):
        res = DocumentController.list_documents(params["id"])
        return 200, res

    def _handle_verify_document(self, params, query, body):
        res = DocumentController.verify_document(body or {})
        if isinstance(res, tuple):
            return res[1], res[0]
        return 200, res

    def route_request(self, method: str, path: str, query: Dict[str, Any], body: Optional[Dict[str, Any]]) -> Tuple[int, Dict[str, Any]]:
        for route_method, regex, handler in self.routes:
            if route_method == method.upper():
                match = regex.match(path)
                if match:
                    try:
                        return handler(match.groupdict(), query, body)
                    except Exception as e:
                        return 500, {"success": False, "error": f"Internal Server Error: {str(e)}"}
        return 404, {"success": False, "error": f"Route not found: {method} {path}"}

_router = APIRouter()

def get_router() -> APIRouter:
    return _router
