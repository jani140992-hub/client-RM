"""
NexusCRM Client & Corporate Entity Models.
Defines institutional client profiles, corporate hierarchies, contact persons, and coverage teams.
"""

from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any
from datetime import datetime
import json

@dataclass
class ContactPerson:
    id: str
    client_id: str
    first_name: str
    last_name: str
    title: str
    email: str
    phone: str
    is_primary_signatory: bool = False
    is_key_management_personnel: bool = True
    nationality: str = "US"
    country_of_residence: str = "US"
    has_pep_flag: bool = False
    created_at: str = field(default_factory=lambda: datetime.utcnow().isoformat())

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "client_id": self.client_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "full_name": f"{self.first_name} {self.last_name}",
            "title": self.title,
            "email": self.email,
            "phone": self.phone,
            "is_primary_signatory": self.is_primary_signatory,
            "is_key_management_personnel": self.is_key_management_personnel,
            "nationality": self.nationality,
            "country_of_residence": self.country_of_residence,
            "has_pep_flag": self.has_pep_flag,
            "created_at": self.created_at
        }

@dataclass
class LegalEntity:
    id: str
    client_id: str
    legal_name: str
    trade_name: Optional[str] = None
    entity_type: str = "CORPORATION"  # CORPORATION, LLC, PARTNERSHIP, TRUST, SICAV_FUND, etc.
    jurisdiction_of_incorporation: str = "US"
    date_of_incorporation: str = "2015-06-01"
    registration_number: str = ""
    tax_identification_number: str = ""
    legal_entity_identifier: Optional[str] = None  # 20-char ISO 17442 LEI
    registered_office_address: str = ""
    principal_place_of_business: str = ""
    primary_naics_code: str = "522110"
    operating_countries: List[str] = field(default_factory=lambda: ["US"])
    is_publicly_traded: bool = False
    stock_exchange: Optional[str] = None
    ticker_symbol: Optional[str] = None
    created_at: str = field(default_factory=lambda: datetime.utcnow().isoformat())

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "client_id": self.client_id,
            "legal_name": self.legal_name,
            "trade_name": self.trade_name,
            "entity_type": self.entity_type,
            "jurisdiction_of_incorporation": self.jurisdiction_of_incorporation,
            "date_of_incorporation": self.date_of_incorporation,
            "registration_number": self.registration_number,
            "tax_identification_number": self.tax_identification_number,
            "legal_entity_identifier": self.legal_entity_identifier,
            "registered_office_address": self.registered_office_address,
            "principal_place_of_business": self.principal_place_of_business,
            "primary_naics_code": self.primary_naics_code,
            "operating_countries": self.operating_countries,
            "is_publicly_traded": self.is_publicly_traded,
            "stock_exchange": self.stock_exchange,
            "ticker_symbol": self.ticker_symbol,
            "created_at": self.created_at
        }

@dataclass
class RelationshipManager:
    id: str
    name: str
    email: str
    team: str  # Institutional Corporate, Wealth Advisory, FinTech Solutions
    desk_location: str  # New York, London, Singapore, Zurich
    active_client_count: int = 0

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "team": self.team,
            "desk_location": self.desk_location,
            "active_client_count": self.active_client_count
        }

@dataclass
class Client:
    id: str
    client_number: str  # e.g., "NX-90412"
    name: str
    client_segment: str  # INSTITUTIONAL_BANKING, WEALTH_MANAGEMENT, FAMILY_OFFICE, FINTECH
    primary_relationship_manager_id: str
    secondary_relationship_manager_id: Optional[str] = None
    compliance_officer_id: Optional[str] = None
    credit_analyst_id: Optional[str] = None
    onboarding_status: str = "PROSPECT"  # PROSPECT, ONBOARDING, ACTIVE, RESTRICTED, OFFBOARDED
    risk_tier: str = "MEDIUM"  # LOW, MEDIUM, HIGH, PROHIBITED
    composite_risk_score: float = 4.5
    kyc_refresh_frequency_months: int = 24
    last_kyc_review_date: Optional[str] = None
    next_kyc_review_date: Optional[str] = None
    onboarding_completed_date: Optional[str] = None
    legal_entities: List[LegalEntity] = field(default_factory=list)
    contacts: List[ContactPerson] = field(default_factory=list)
    tags: List[str] = field(default_factory=list)
    created_at: str = field(default_factory=lambda: datetime.utcnow().isoformat())
    updated_at: str = field(default_factory=lambda: datetime.utcnow().isoformat())

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "client_number": self.client_number,
            "name": self.name,
            "client_segment": self.client_segment,
            "primary_relationship_manager_id": self.primary_relationship_manager_id,
            "secondary_relationship_manager_id": self.secondary_relationship_manager_id,
            "compliance_officer_id": self.compliance_officer_id,
            "credit_analyst_id": self.credit_analyst_id,
            "onboarding_status": self.onboarding_status,
            "risk_tier": self.risk_tier,
            "composite_risk_score": self.composite_risk_score,
            "kyc_refresh_frequency_months": self.kyc_refresh_frequency_months,
            "last_kyc_review_date": self.last_kyc_review_date,
            "next_kyc_review_date": self.next_kyc_review_date,
            "onboarding_completed_date": self.onboarding_completed_date,
            "legal_entities": [e.to_dict() for e in self.legal_entities],
            "contacts": [c.to_dict() for c in self.contacts],
            "tags": self.tags,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
