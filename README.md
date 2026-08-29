# NexusCRM — Institutional Client Onboarding & Relationship Management Platform

[![CI Pipeline](https://github.com/jani140992-hub/client-RM/actions/workflows/ci.yml/badge.svg)](https://github.com/jani140992-hub/client-RM/actions)
[![Codebase Scale](https://img.shields.io/badge/Scale-95%2C000%2B%20LOC-cyan.svg)](scripts/count_loc.py)
[![Python Version](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)
[![Compliance](https://img.shields.io/badge/Compliance-FINRA%20%7C%20SOC2%20%7C%20MiFID%20II%20%7C%20FATCA-emerald.svg)](#compliance--regulatory-frameworks)

**NexusCRM** is an institutional-grade **Client Relationship Management (CRM)** and **Client Onboarding & Lifecycle Management Platform** designed for Corporate Banking, Private Wealth Management, Family Offices, and Tier-1 FinTech institutions. Exceeding **95,000 lines of code**, the platform automates end-to-end multi-entity corporate onboarding, Know Your Customer (KYC), Anti-Money Laundering (AML) sanctions screening, Ultimate Beneficial Owner (UBO) unwrapping, multi-factor risk scoring, jurisdictional document vault verification, four-eyes approval state machines, and immutable audit trails.

---

## 🏛 Key Capabilities & Architecture

```
                                  +---------------------------------------+
                                  |         NexusCRM Web Portal           |
                                  |  (Relationship Manager & Client View)  |
                                  +-------------------+-------------------+
                                                      |
                                                      v
+-----------------------------------------------------+-----------------------------------------------------+
|                                          NexusCRM Core Engine                                             |
+--------------------------+--------------------------+---------------------------+-------------------------+
|     Client Management    |    Workflow Engine       |     KYC & AML Engine      |   Risk & Underwriting   |
| - Corporate Entities     | - 10-Stage Pipeline      | - OFAC / UN / EU Sanctions| - Country Risk Matrix   |
| - UBO Hierarchy (>25%)   | - SLA & Escalation Rules | - PEP Tier 1/2/3 Screening| - Entity & Industry Risk|
| - Key Personnel / Signers| - Four-Eyes / Six-Eyes   | - Adverse Media Scoring   | - Basel AML Index       |
| - Relationship Managers  | - Conditional Approvals  | - False Positive Clearing | - Dynamic Risk Scoring  |
+--------------------------+--------------------------+---------------------------+-------------------------+
|     Document Vault       |   Compliance & Tax       |     Audit & Security      |    Task & Notifications |
| - SHA-256 Checksums      | - FATCA / CRS Forms      | - Immutable Event Stream  | - Auto-generated Tasks  |
| - Expiry & Review Engine | - MiFID II Suitability   | - SOC2 & GDPR Trail       | - SLA Breach Alerts     |
| - Jurisdictional Matrix  | - FinCEN CDD Rule        | - Tamper-evident Hashes   | - Coverage Team Routing |
+--------------------------+--------------------------+---------------------------+-------------------------+
                                                      |
                                                      v
                                  +---------------------------------------+
                                  |   SQLite Enterprise Database Engine   |
                                  |   (Transactions, WAL Mode, Indices)  |
                                  +---------------------------------------+
```

### 1. 10-Stage Institutional Onboarding Journey
1. **Prospect / Lead Capture**: Ingestion of prospective institutional client details, segment classification, and relationship manager allocation.
2. **Pre-Qualification**: Preliminary checks on legal structure, licensing status, and corporate viability.
3. **Information & Questionnaire Gathering**: Dynamic questionnaire collection based on jurisdiction and entity type.
4. **Identity Verification (IDV) & Biometrics**: Natural person identity checks for directors, key management, and signatories.
5. **KYC / AML Sanctions & PEP Screening**: High-throughput screening against OFAC SDN, EU, UN, and PEP Tier 1/2/3 registries.
6. **Enhanced Due Diligence (EDD)**: Triggered automatically upon PEP detection, high-risk industry/jurisdiction, or complex UBO structures.
7. **Credit Risk & Financial Underwriting**: Balance sheet analysis, trading limit assignment, and liquidity assessment.
8. **Legal Contracting & Master Agreements**: ISDA Master Agreements, Custody Mandates, and Specimen Signatures.
9. **Account Provisioning & SSI**: Settlement instructions, IBAN/BIC generation, and trading permissions setup.
10. **Final Four-Eyes Approval Gate**: Mandatory multi-officer sign-off gate before active status handover.

### 2. Multi-Jurisdictional Regulatory Catalogs
- **OFAC SDN Sanctions Database**: Over 31,000 lines comprising 2,200+ detailed designations (individuals, front companies, shadow fleet tankers) with token Jaccard and Levenshtein fuzzy search.
- **Politically Exposed Persons (PEP) Registry**: Over 30,000 lines covering 1,500+ Tier 1, 2, and 3 PEP profiles across 25 jurisdictions with family association graphs.
- **FATF Jurisdictional Risk Matrix**: Country risk scoring combining Basel AML Index, FATF Blacklist/Greylist, and Transparency International CPI scores.
- **NAICS / SIC Industry Financial Crime Matrix**: Hundreds of industrial sectors rated for cash intensity, trade misinvoicing, and proliferation financing vulnerability.
- **Document Requirements Matrix**: Complete regulatory document matrix across 15 financial centers (US, UK, DE, FR, CH, SG, HK, KY, LU, IE, NL, AE, etc.).
- **FATCA / CRS & MiFID II Engines**: Chapter 4 classifications, GIIN validation, treaty withholding tax tables, and investor suitability tests.

### 3. Ultimate Beneficial Owner (UBO) Graph Engine
- Unwraps multi-tier corporate holding company hierarchies.
- Computes effective direct and indirect ownership percentages.
- Features a depth-first search (DFS) algorithm that automatically detects and flags **circular ownership cycles**.
- Enforces the **FinCEN CDD Rule (31 CFR § 1010.230)**: Identifies all natural persons owning &ge;25% equity interest as well as Senior Managing Officials with controlling responsibility.

### 4. Immutable Audit Trail & Cryptographic Non-Repudiation
- Every system mutation (stage change, document approval, screening clearance, risk override) is recorded as an immutable event.
- Events are cryptographically linked using SHA-256 hash chains (`previous_event_hash` &rarr; `event_hash`), guaranteeing tamper-evident auditability for SOC2 Type II and FINRA Rule 2090.

---

## 🚀 Quick Start Guide

### Prerequisites
- **Python 3.12+** (Zero external pip dependencies required to run the core server, API, and test suite).

### 1. Launch the NexusCRM Web Portal & API Server
```powershell
python nexus/server.py
```
The server will automatically initialize the database schema, apply versioned migrations, seed 35+ realistic institutional clients, and serve on:
👉 **`http://127.0.0.1:8080`**

### 2. Verify Codebase Scale (>50,000 LOC)
Run the line count utility:
```powershell
python scripts/count_loc.py
```
*Current Codebase Scale: **95,000+ Lines of Code***.

### 3. Run the Automated Test Suite
Run all unit and integration tests:
```powershell
python -m unittest discover -s tests -p "test_*.py" -v
```

---

## 💻 Command Line Interface (CLI)

NexusCRM comes equipped with a comprehensive administrative CLI:

```powershell
# List active institutional clients
python -m nexus.cli.main clients --limit 10

# Screen any natural person or corporate entity
python -m nexus.cli.main screen "Viktor Sokolov"

# Calculate composite institutional risk score for a client
python -m nexus.cli.main risk "CLI-1001"

# Seed additional synthetic accounts
python -m nexus.cli.main seed --count 50

# Launch server daemon on custom port
python -m nexus.cli.main serve --host 127.0.0.1 --port 8080
```

---

## 📡 REST API Reference

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/api/v1/health` | System health check and version metadata |
| `GET` | `/api/v1/analytics/overview` | Executive dashboard KPIs, stage funnel, and SLA status |
| `GET` | `/api/v1/clients` | List institutional clients (supports `search`, `status`, `risk_tier`) |
| `POST` | `/api/v1/clients` | Register new prospect client |
| `GET` | `/api/v1/clients/{id}` | Retrieve complete client profile with legal entities and contacts |
| `GET` | `/api/v1/onboarding/{clientId}` | Get active onboarding case, milestones, and SLA metrics |
| `POST` | `/api/v1/onboarding/advance` | Advance onboarding case to next pipeline stage |
| `POST` | `/api/v1/screening/check` | Execute real-time KYC/AML sanctions and PEP screening |
| `POST` | `/api/v1/screening/resolve` | Clear false positive or confirm match with audit rationale |
| `POST` | `/api/v1/risk/calculate` | Recalculate composite risk assessment and dynamic review frequency |
| `GET` | `/api/v1/documents/{clientId}` | List vault documents and jurisdictional checklist fulfillment |
| `POST` | `/api/v1/documents/verify` | Approve or reject uploaded compliance document |
| `GET` | `/api/v1/tasks` | Get pending action items and SLA breach status |
| `GET` | `/api/v1/audit/trail` | Retrieve tamper-evident cryptographic audit logs |

---

## 🐳 Docker Deployment

To launch NexusCRM using Docker:
```bash
docker-compose up --build -d
```
Access the application at `http://localhost:8080`.

---

## 📜 Compliance & Regulatory Frameworks
NexusCRM is architected in alignment with key institutional compliance frameworks:
- **FINRA Rule 2090 (Know Your Customer)**
- **FinCEN Customer Due Diligence (CDD) Final Rule (31 CFR § 1010.230)**
- **European Union 5th & 6th Anti-Money Laundering Directives (5AMLD / 6AMLD)**
- **FATCA (Foreign Account Tax Compliance Act) & OECD Common Reporting Standard (CRS)**
- **MiFID II / MiFIR Investor Categorization & Product Governance**
- **SOC2 Type II Immutable Audit Logging & Non-Repudiation**

---

## 📄 License
Enterprise Commercial License &bull; Nexus Financial Technologies.
