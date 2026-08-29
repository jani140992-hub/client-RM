"""
NexusCRM Domain Models Package.
Exports client, entity, UBO, onboarding, compliance, risk, document, workflow, audit, and task models.
"""

from nexus.models.client import Client, LegalEntity, ContactPerson, RelationshipManager
from nexus.models.ubo import UBOOwner, OwnershipGraph
from nexus.models.onboarding import OnboardingCase, OnboardingStage, MilestoneItem, STAGE_ORDER
from nexus.models.compliance import ScreeningHit, EDDInvestigationCase
from nexus.models.risk import RiskAssessment, RiskFactorBreakdown
from nexus.models.document import DocumentRecord
from nexus.models.workflow import ApprovalGate, WorkflowTransition
from nexus.models.audit import AuditEvent
from nexus.models.task import ActionTask

__all__ = [
    "Client",
    "LegalEntity",
    "ContactPerson",
    "RelationshipManager",
    "UBOOwner",
    "OwnershipGraph",
    "OnboardingCase",
    "OnboardingStage",
    "MilestoneItem",
    "STAGE_ORDER",
    "ScreeningHit",
    "EDDInvestigationCase",
    "RiskAssessment",
    "RiskFactorBreakdown",
    "DocumentRecord",
    "ApprovalGate",
    "WorkflowTransition",
    "AuditEvent",
    "ActionTask",
]
