"""
NexusCRM Database Schema DDL.
Creates relational tables, indices, and constraints for clients, entities, UBOs, cases, documents, risk, and audit trails.
"""

import sqlite3
import logging

logger = logging.getLogger("nexus.database.schema")

DDL_SCHEMA = """
-- Relationship Managers Table
CREATE TABLE IF NOT EXISTS relationship_managers (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    team TEXT NOT NULL,
    desk_location TEXT NOT NULL,
    active_client_count INTEGER DEFAULT 0
);

-- Clients Table
CREATE TABLE IF NOT EXISTS clients (
    id TEXT PRIMARY KEY,
    client_number TEXT UNIQUE NOT NULL,
    name TEXT NOT NULL,
    client_segment TEXT NOT NULL,
    primary_relationship_manager_id TEXT NOT NULL,
    secondary_relationship_manager_id TEXT,
    compliance_officer_id TEXT,
    credit_analyst_id TEXT,
    onboarding_status TEXT NOT NULL DEFAULT 'PROSPECT',
    risk_tier TEXT NOT NULL DEFAULT 'MEDIUM',
    composite_risk_score REAL DEFAULT 4.5,
    kyc_refresh_frequency_months INTEGER DEFAULT 24,
    last_kyc_review_date TEXT,
    next_kyc_review_date TEXT,
    onboarding_completed_date TEXT,
    tags TEXT, -- JSON array of string tags
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL,
    FOREIGN KEY (primary_relationship_manager_id) REFERENCES relationship_managers(id)
);

-- Legal Entities Table
CREATE TABLE IF NOT EXISTS legal_entities (
    id TEXT PRIMARY KEY,
    client_id TEXT NOT NULL,
    legal_name TEXT NOT NULL,
    trade_name TEXT,
    entity_type TEXT NOT NULL,
    jurisdiction_of_incorporation TEXT NOT NULL,
    date_of_incorporation TEXT,
    registration_number TEXT,
    tax_identification_number TEXT,
    legal_entity_identifier TEXT,
    registered_office_address TEXT,
    principal_place_of_business TEXT,
    primary_naics_code TEXT,
    operating_countries TEXT, -- JSON array
    is_publicly_traded INTEGER DEFAULT 0,
    stock_exchange TEXT,
    ticker_symbol TEXT,
    created_at TEXT NOT NULL,
    FOREIGN KEY (client_id) REFERENCES clients(id) ON DELETE CASCADE
);

-- Contact Persons Table
CREATE TABLE IF NOT EXISTS contact_persons (
    id TEXT PRIMARY KEY,
    client_id TEXT NOT NULL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    title TEXT NOT NULL,
    email TEXT NOT NULL,
    phone TEXT NOT NULL,
    is_primary_signatory INTEGER DEFAULT 0,
    is_key_management_personnel INTEGER DEFAULT 1,
    nationality TEXT DEFAULT 'US',
    country_of_residence TEXT DEFAULT 'US',
    has_pep_flag INTEGER DEFAULT 0,
    created_at TEXT NOT NULL,
    FOREIGN KEY (client_id) REFERENCES clients(id) ON DELETE CASCADE
);

-- UBO Owners Table
CREATE TABLE IF NOT EXISTS ubo_owners (
    id TEXT PRIMARY KEY,
    client_id TEXT NOT NULL,
    entity_id TEXT NOT NULL,
    owner_type TEXT NOT NULL, -- INDIVIDUAL or INTERMEDIARY_ENTITY
    name TEXT NOT NULL,
    ownership_percentage REAL NOT NULL,
    voting_rights_percentage REAL NOT NULL,
    is_direct_owner INTEGER DEFAULT 1,
    parent_owner_id TEXT,
    country_of_citizenship TEXT DEFAULT 'US',
    country_of_tax_residence TEXT DEFAULT 'US',
    is_pep INTEGER DEFAULT 0,
    pep_tier INTEGER,
    sanctions_check_status TEXT DEFAULT 'CLEAR',
    idv_verification_status TEXT DEFAULT 'VERIFIED',
    identification_type TEXT DEFAULT 'PASSPORT',
    identification_number TEXT,
    date_of_birth TEXT,
    residential_address TEXT,
    control_type TEXT DEFAULT 'EQUITY_OWNERSHIP',
    created_at TEXT NOT NULL,
    FOREIGN KEY (client_id) REFERENCES clients(id) ON DELETE CASCADE,
    FOREIGN KEY (entity_id) REFERENCES legal_entities(id) ON DELETE CASCADE
);

-- Onboarding Cases Table
CREATE TABLE IF NOT EXISTS onboarding_cases (
    id TEXT PRIMARY KEY,
    client_id TEXT UNIQUE NOT NULL,
    case_number TEXT UNIQUE NOT NULL,
    current_stage TEXT NOT NULL DEFAULT 'PROSPECT_LEAD',
    stage_index INTEGER DEFAULT 0,
    target_completion_date TEXT,
    sla_hours_budget REAL DEFAULT 336.0,
    sla_hours_elapsed REAL DEFAULT 0.0,
    sla_status TEXT DEFAULT 'GREEN',
    is_edd_triggered INTEGER DEFAULT 0,
    assigned_relationship_manager_id TEXT,
    assigned_compliance_officer_id TEXT,
    assigned_credit_officer_id TEXT,
    assigned_operations_lead_id TEXT,
    completion_percentage REAL DEFAULT 0.0,
    notes TEXT,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL,
    FOREIGN KEY (client_id) REFERENCES clients(id) ON DELETE CASCADE
);

-- Milestones Table
CREATE TABLE IF NOT EXISTS case_milestones (
    id TEXT PRIMARY KEY,
    case_id TEXT NOT NULL,
    stage TEXT NOT NULL,
    title TEXT NOT NULL,
    is_completed INTEGER DEFAULT 0,
    completed_by TEXT,
    completed_at TEXT,
    notes TEXT,
    FOREIGN KEY (case_id) REFERENCES onboarding_cases(id) ON DELETE CASCADE
);

-- Document Vault Table
CREATE TABLE IF NOT EXISTS document_vault (
    id TEXT PRIMARY KEY,
    client_id TEXT NOT NULL,
    case_id TEXT,
    document_type TEXT NOT NULL,
    title TEXT NOT NULL,
    file_name TEXT NOT NULL,
    file_size_bytes INTEGER NOT NULL,
    mime_type TEXT NOT NULL,
    sha256_checksum TEXT NOT NULL,
    verification_status TEXT DEFAULT 'PENDING_REVIEW',
    verified_by TEXT,
    verified_at TEXT,
    rejection_reason TEXT,
    issue_date TEXT,
    expiry_date TEXT,
    is_certified_true_copy INTEGER DEFAULT 0,
    is_apostilled INTEGER DEFAULT 0,
    issuing_authority TEXT,
    issuing_country TEXT DEFAULT 'US',
    storage_uri TEXT,
    created_at TEXT NOT NULL,
    FOREIGN KEY (client_id) REFERENCES clients(id) ON DELETE CASCADE
);

-- Screening Hits Table
CREATE TABLE IF NOT EXISTS screening_hits (
    id TEXT PRIMARY KEY,
    case_id TEXT NOT NULL,
    subject_name TEXT NOT NULL,
    subject_type TEXT NOT NULL,
    catalog_source TEXT NOT NULL,
    hit_reference_id TEXT NOT NULL,
    matched_name TEXT NOT NULL,
    match_score REAL NOT NULL,
    programs_or_tier TEXT NOT NULL,
    disposition TEXT DEFAULT 'OPEN',
    reviewed_by TEXT,
    reviewed_at TEXT,
    clearance_rationale TEXT,
    created_at TEXT NOT NULL,
    FOREIGN KEY (case_id) REFERENCES onboarding_cases(id) ON DELETE CASCADE
);

-- EDD Investigation Cases Table
CREATE TABLE IF NOT EXISTS edd_cases (
    id TEXT PRIMARY KEY,
    case_id TEXT NOT NULL,
    client_id TEXT NOT NULL,
    trigger_reason TEXT NOT NULL,
    risk_level TEXT DEFAULT 'HIGH',
    status TEXT DEFAULT 'IN_PROGRESS',
    investigator_id TEXT,
    source_of_wealth_verified INTEGER DEFAULT 0,
    source_of_wealth_notes TEXT,
    senior_management_approval_by TEXT,
    senior_management_approval_at TEXT,
    investigation_findings TEXT,
    mitigating_controls TEXT, -- JSON array
    created_at TEXT NOT NULL,
    completed_at TEXT,
    FOREIGN KEY (case_id) REFERENCES onboarding_cases(id) ON DELETE CASCADE,
    FOREIGN KEY (client_id) REFERENCES clients(id) ON DELETE CASCADE
);

-- Risk Assessments Table
CREATE TABLE IF NOT EXISTS risk_assessments (
    id TEXT PRIMARY KEY,
    client_id TEXT NOT NULL,
    case_id TEXT,
    composite_score REAL NOT NULL,
    risk_tier TEXT NOT NULL,
    review_frequency_months INTEGER NOT NULL,
    factors_json TEXT NOT NULL,
    has_overrides INTEGER DEFAULT 0,
    override_reason TEXT,
    overridden_by TEXT,
    assessed_by TEXT DEFAULT 'AUTOMATED_ENGINE',
    approved_by TEXT,
    created_at TEXT NOT NULL,
    FOREIGN KEY (client_id) REFERENCES clients(id) ON DELETE CASCADE
);

-- Approval Gates Table
CREATE TABLE IF NOT EXISTS approval_gates (
    id TEXT PRIMARY KEY,
    case_id TEXT NOT NULL,
    stage TEXT NOT NULL,
    gate_name TEXT NOT NULL,
    required_role TEXT NOT NULL,
    status TEXT DEFAULT 'PENDING',
    approver_id TEXT,
    approver_name TEXT,
    comments TEXT,
    decided_at TEXT,
    created_at TEXT NOT NULL,
    FOREIGN KEY (case_id) REFERENCES onboarding_cases(id) ON DELETE CASCADE
);

-- Action Tasks Table
CREATE TABLE IF NOT EXISTS action_tasks (
    id TEXT PRIMARY KEY,
    case_id TEXT NOT NULL,
    client_id TEXT NOT NULL,
    task_type TEXT NOT NULL,
    title TEXT NOT NULL,
    description TEXT,
    priority TEXT DEFAULT 'MEDIUM',
    status TEXT DEFAULT 'OPEN',
    assigned_to_user_id TEXT,
    assigned_role TEXT DEFAULT 'COMPLIANCE_OFFICER',
    due_date TEXT NOT NULL,
    is_sla_breached INTEGER DEFAULT 0,
    resolution_notes TEXT,
    completed_at TEXT,
    created_at TEXT NOT NULL,
    FOREIGN KEY (case_id) REFERENCES onboarding_cases(id) ON DELETE CASCADE,
    FOREIGN KEY (client_id) REFERENCES clients(id) ON DELETE CASCADE
);

-- Immutable Audit Log Table
CREATE TABLE IF NOT EXISTS audit_events (
    id TEXT PRIMARY KEY,
    entity_type TEXT NOT NULL,
    entity_id TEXT NOT NULL,
    action TEXT NOT NULL,
    actor_id TEXT NOT NULL,
    actor_name TEXT NOT NULL,
    actor_role TEXT NOT NULL,
    ip_address TEXT DEFAULT '127.0.0.1',
    timestamp TEXT NOT NULL,
    previous_state TEXT, -- JSON
    new_state TEXT,      -- JSON
    change_summary TEXT NOT NULL,
    previous_event_hash TEXT NOT NULL,
    event_hash TEXT NOT NULL
);

-- Indices for rapid queries
CREATE INDEX IF NOT EXISTS idx_clients_status ON clients(onboarding_status);
CREATE INDEX IF NOT EXISTS idx_clients_rm ON clients(primary_relationship_manager_id);
CREATE INDEX IF NOT EXISTS idx_cases_stage ON onboarding_cases(current_stage);
CREATE INDEX IF NOT EXISTS idx_cases_sla ON onboarding_cases(sla_status);
CREATE INDEX IF NOT EXISTS idx_entities_client ON legal_entities(client_id);
CREATE INDEX IF NOT EXISTS idx_ubo_entity ON ubo_owners(entity_id);
CREATE INDEX IF NOT EXISTS idx_documents_client ON document_vault(client_id);
CREATE INDEX IF NOT EXISTS idx_screening_case ON screening_hits(case_id);
CREATE INDEX IF NOT EXISTS idx_tasks_assigned ON action_tasks(assigned_to_user_id, status);
CREATE INDEX IF NOT EXISTS idx_audit_entity ON audit_events(entity_type, entity_id);
"""

def initialize_database(conn: sqlite3.Connection):
    """Executes the DDL schema to ensure all tables and indexes exist."""
    cursor = conn.cursor()
    cursor.executescript(DDL_SCHEMA)
    conn.commit()
    logger.info("NexusCRM database schema initialized successfully.")
