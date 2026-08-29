"""
NexusCRM API Controllers Package.
"""

from nexus.api.controllers.client_controller import ClientController
from nexus.api.controllers.onboarding_controller import OnboardingController
from nexus.api.controllers.screening_controller import ScreeningController
from nexus.api.controllers.risk_controller import RiskController
from nexus.api.controllers.document_controller import DocumentController
from nexus.api.controllers.analytics_controller import AnalyticsController
from nexus.api.controllers.auth_controller import AuthController

__all__ = [
    "ClientController",
    "OnboardingController",
    "ScreeningController",
    "RiskController",
    "DocumentController",
    "AnalyticsController",
    "AuthController",
]
