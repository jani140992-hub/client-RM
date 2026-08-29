"""
NexusCRM Configuration Management.
Centralized settings for runtime, database persistence, SLA thresholds, risk score weighting, and security parameters.
"""

import os
from dataclasses import dataclass, field
from typing import Dict, Any

@dataclass
class DatabaseConfig:
    db_path: str = os.environ.get("NEXUS_DB_PATH", os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "nexus_crm.db"))
    timeout_seconds: float = 30.0
    enable_wal: bool = True
    max_connections: int = 20

@dataclass
class ServerConfig:
    host: str = os.environ.get("NEXUS_HOST", "127.0.0.1")
    port: int = int(os.environ.get("NEXUS_PORT", "8090"))
    jwt_secret: str = os.environ.get("NEXUS_JWT_SECRET", "nexus-enterprise-crm-super-secret-key-2026")
    token_expiry_hours: int = 24
    cors_allow_all: bool = True
    debug: bool = os.environ.get("NEXUS_DEBUG", "false").lower() == "true"

@dataclass
class SLAThresholds:
    pre_qualification_hours: float = 24.0
    kyc_document_review_hours: float = 48.0
    compliance_edd_review_hours: float = 72.0
    credit_underwriting_hours: float = 48.0
    legal_contracting_hours: float = 96.0
    total_onboarding_target_days: float = 14.0
    escalation_warning_pct: float = 0.80  # Trigger amber warning at 80% SLA elapsed

@dataclass
class RiskMatrixWeights:
    country_risk_weight: float = 0.25
    entity_structure_weight: float = 0.15
    industry_sector_weight: float = 0.20
    pep_sanctions_weight: float = 0.25
    product_volume_weight: float = 0.15
    
    # Thresholds for overall score (0.0 to 10.0 scale)
    low_risk_max: float = 3.99
    medium_risk_max: float = 6.99
    high_risk_max: float = 8.49
    # Anything >= 8.50 is CRITICAL / PROHIBITED

@dataclass
class NexusConfig:
    database: DatabaseConfig = field(default_factory=DatabaseConfig)
    server: ServerConfig = field(default_factory=ServerConfig)
    sla: SLAThresholds = field(default_factory=SLAThresholds)
    risk_weights: RiskMatrixWeights = field(default_factory=RiskMatrixWeights)
    version: str = "3.4.0-enterprise"
    system_name: str = "NexusCRM Institutional Onboarding Platform"

# Global configuration instance
_config_instance: NexusConfig = NexusConfig()

def get_config() -> NexusConfig:
    global _config_instance
    return _config_instance
