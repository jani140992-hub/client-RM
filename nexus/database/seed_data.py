"""
NexusCRM Enterprise Database Seeder.
Generates comprehensive synthetic portfolios of institutional corporate clients,
relationship managers, multi-layer UBO graphs, onboarding cases across the 10 stages,
document vault files with SHA-256 checksums, sanctions screening cases, and audit trails.
"""

import sqlite3
import json
import uuid
import hashlib
from datetime import datetime, timedelta
import random

from nexus.models.onboarding import STAGE_ORDER, OnboardingStage
from nexus.catalogs.document_requirements_matrix import get_required_documents_for_entity

def seed_database(conn: sqlite3.Connection, num_clients: int = 50):
    cursor = conn.cursor()

    # Check if database is already seeded
    cursor.execute("SELECT COUNT(*) FROM clients;")
    if cursor.fetchone()[0] > 0:
        print("[*] Database already contains records. Skipping seed.")
        return

    print(f"[*] Seeding database with {num_clients} institutional clients, cases, UBOs, and documents...")

    # 1. Seed Relationship Managers
    rms = [
        ("RM-101", "Marcus Vance", "marcus.vance@nexuscrm.com", "Institutional Corporate Banking", "New York", 14),
        ("RM-102", "Eleanor Davies", "eleanor.davies@nexuscrm.com", "Private Wealth & Family Offices", "London", 12),
        ("RM-103", "Kaito Tanaka", "kaito.tanaka@nexuscrm.com", "FinTech & Digital Assets", "Singapore", 11),
        ("RM-104", "Claire Beaumont", "claire.beaumont@nexuscrm.com", "Alternative Asset Management", "Zurich", 9),
        ("RM-105", "Siddharth Mehta", "siddharth.mehta@nexuscrm.com", "Cross-Border Trade Solutions", "Dubai", 8)
    ]

    for rm in rms:
        cursor.execute("""
            INSERT OR REPLACE INTO relationship_managers (id, name, email, team, desk_location, active_client_count)
            VALUES (?, ?, ?, ?, ?, ?);
        """, rm)

    client_segments = ["INSTITUTIONAL_BANKING", "WEALTH_MANAGEMENT", "FAMILY_OFFICE", "FINTECH"]
    jurisdictions = ["US", "GB", "KY", "LU", "SG", "CH", "IE", "DE", "AE", "HK"]
    entity_types = ["CORPORATION", "LLC", "LIMITED_PARTNERSHIP", "TRUST", "SICAV_FUND", "HEDGE_FUND"]
    naics_list = ["522110", "522293", "523910", "523110", "523920", "531120", "483111", "541511"]

    corp_prefixes = ["Apex", "Vanguard", "Horizon", "Blackstone", "Starlight", "Crestview", "Aegis", "Meridian", "Solaria", "Pinnacle", "Quantum", "Cascade", "Titan", "Olympus", "Frontier"]
    corp_suffixes = ["Capital Partners", "Holdings Inc", "Global Fund LP", "Technologies DMCC", "Asset Management SA", "Financial Trust", "Ventures Ltd", "International Corp"]

    first_names = ["Alexander", "Victoria", "Julian", "Sophia", "Gabriel", "Olivia", "Lucas", "Emma", "William", "Isabella", "Sebastian", "Mia"]
    last_names = ["Rothschild", "Sterling", "Vanderbilt", "Sinclair", "Mercer", "Blackwood", "Kensington", "Ashford", "Montgomery", "Fairfax"]

    now = datetime.utcnow()

    # Previous hash tracker for tamper-evident audit log
    last_audit_hash = "0000000000000000000000000000000000000000000000000000000000000000"

    for i in range(num_clients):
        cid = f"CLI-{1000 + i}"
        client_num = f"NX-{80000 + i}"
        cname = f"{corp_prefixes[i % len(corp_prefixes)]} {corp_suffixes[(i * 3 + 1) % len(corp_suffixes)]} #{i+1}"
        csegment = client_segments[i % len(client_segments)]
        rm_id = rms[i % len(rms)][0]
        
        # Distribute across stages
        stage_idx = i % len(STAGE_ORDER)
        stage_enum = STAGE_ORDER[stage_idx]
        current_stage = stage_enum.value

        if current_stage == "COMPLETED":
            onb_status = "ACTIVE"
            comp_date = (now - timedelta(days=random.randint(5, 60))).isoformat()
            completion_pct = 100.0
        elif current_stage in ["PROSPECT_LEAD", "PRE_QUALIFICATION"]:
            onb_status = "PROSPECT"
            comp_date = None
            completion_pct = round((stage_idx + 1) * 9.5, 1)
        else:
            onb_status = "ONBOARDING"
            comp_date = None
            completion_pct = round((stage_idx + 1) * 9.5, 1)

        risk_tiers = ["LOW", "MEDIUM", "HIGH"]
        risk_tier = risk_tiers[i % len(risk_tiers)]
        comp_score = 2.5 if risk_tier == "LOW" else (5.5 if risk_tier == "MEDIUM" else 7.8)
        refresh_freq = 36 if risk_tier == "LOW" else (24 if risk_tier == "MEDIUM" else 12)

        created_dt = now - timedelta(days=(40 - (i % 30)))
        created_at = created_dt.isoformat()
        updated_at = now.isoformat()

        # Insert Client
        cursor.execute("""
            INSERT INTO clients (
                id, client_number, name, client_segment, primary_relationship_manager_id,
                onboarding_status, risk_tier, composite_risk_score, kyc_refresh_frequency_months,
                last_kyc_review_date, next_kyc_review_date, onboarding_completed_date, tags,
                created_at, updated_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        """, (
            cid, client_num, cname, csegment, rm_id, onb_status, risk_tier, comp_score,
            refresh_freq, created_at[:10], (now + timedelta(days=refresh_freq*30)).isoformat()[:10],
            comp_date, json.dumps(["Tier-1 Institutional", csegment.replace("_", " ")]),
            created_at, updated_at
        ))

        # Insert Legal Entity
        eid = f"ENT-{2000 + i}"
        juris = jurisdictions[i % len(jurisdictions)]
        etype = entity_types[i % len(entity_types)]
        naics = naics_list[i % len(naics_list)]
        lei = f"549300{i:04d}NXCRM000{i%9}"

        cursor.execute("""
            INSERT INTO legal_entities (
                id, client_id, legal_name, trade_name, entity_type,
                jurisdiction_of_incorporation, date_of_incorporation, registration_number,
                tax_identification_number, legal_entity_identifier, registered_office_address,
                principal_place_of_business, primary_naics_code, operating_countries,
                is_publicly_traded, created_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        """, (
            eid, cid, cname, f"{corp_prefixes[i % len(corp_prefixes)]} Group", etype,
            juris, "2018-03-15", f"REG-{juris}-{800000+i}", f"TIN-{juris}-{400000+i}",
            lei, f"Financial Center Tower, Suite {i*10 + 100}, {juris}",
            f"Corporate Headquarters, {juris}", naics, json.dumps([juris, "US", "GB"]),
            1 if (i % 7 == 0) else 0, created_at
        ))

        # Insert Key Contacts
        fn = first_names[i % len(first_names)]
        ln = last_names[(i * 2 + 1) % len(last_names)]
        contact_id = f"CNT-{3000 + i}"
        cursor.execute("""
            INSERT INTO contact_persons (
                id, client_id, first_name, last_name, title, email, phone,
                is_primary_signatory, is_key_management_personnel, nationality,
                country_of_residence, has_pep_flag, created_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        """, (
            contact_id, cid, fn, ln, "Chief Executive Officer & Managing Director",
            f"{fn.lower()}.{ln.lower()}@{corp_prefixes[i % len(corp_prefixes)].lower()}group.com",
            f"+1-212-555-01{i:02d}", 1, 1, juris, juris, 1 if (i % 8 == 0) else 0, created_at
        ))

        # Insert UBO Owners (Direct + Parent Intermediary + Natural Person)
        ubo1_id = f"UBO-{4000 + i * 2}"
        cursor.execute("""
            INSERT INTO ubo_owners (
                id, client_id, entity_id, owner_type, name, ownership_percentage,
                voting_rights_percentage, is_direct_owner, country_of_citizenship,
                country_of_tax_residence, is_pep, pep_tier, sanctions_check_status,
                idv_verification_status, identification_type, identification_number,
                date_of_birth, control_type, created_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        """, (
            ubo1_id, cid, eid, "INDIVIDUAL", f"{fn} {ln}", 65.0, 70.0, 1,
            juris, juris, 1 if (i % 8 == 0) else 0, 2 if (i % 8 == 0) else None,
            "CLEAR", "VERIFIED", "PASSPORT", f"P{juris}{700000+i}",
            "1974-08-22", "EQUITY_OWNERSHIP", created_at
        ))

        ubo2_id = f"UBO-{4000 + i * 2 + 1}"
        cursor.execute("""
            INSERT INTO ubo_owners (
                id, client_id, entity_id, owner_type, name, ownership_percentage,
                voting_rights_percentage, is_direct_owner, country_of_citizenship,
                country_of_tax_residence, is_pep, pep_tier, sanctions_check_status,
                idv_verification_status, identification_type, identification_number,
                date_of_birth, control_type, created_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        """, (
            ubo2_id, cid, eid, "INDIVIDUAL", f"Arthur {last_names[(i+3)%len(last_names)]}", 35.0, 30.0, 1,
            "GB", "GB", 0, None, "CLEAR", "VERIFIED", "PASSPORT", f"PGB{800000+i}",
            "1981-11-14", "EQUITY_OWNERSHIP", created_at
        ))

        # Insert Onboarding Case
        case_id = f"CAS-{5000 + i}"
        case_num = f"ONB-2026-{1000 + i}"
        sla_elapsed = round(random.uniform(12.0, 280.0), 1)
        sla_budget = 336.0
        sla_status = "RED" if sla_elapsed >= sla_budget else ("AMBER" if (sla_elapsed / sla_budget) >= 0.8 else "GREEN")
        is_edd = (risk_tier == "HIGH") or (i % 6 == 0)

        cursor.execute("""
            INSERT INTO onboarding_cases (
                id, client_id, case_number, current_stage, stage_index,
                target_completion_date, sla_hours_budget, sla_hours_elapsed, sla_status,
                is_edd_triggered, assigned_relationship_manager_id, assigned_compliance_officer_id,
                completion_percentage, notes, created_at, updated_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        """, (
            case_id, cid, case_num, current_stage, stage_idx,
            (created_dt + timedelta(days=14)).isoformat()[:10],
            sla_budget, sla_elapsed, sla_status, 1 if is_edd else 0,
            rm_id, "USR-COMPLIANCE-01", completion_pct,
            f"Onboarding case initiated for {cname} under {csegment} protocol.",
            created_at, updated_at
        ))

        # Add Milestones for the case
        for s_idx, st in enumerate(STAGE_ORDER[:10]):
            m_id = f"MLS-{case_id}-{s_idx}"
            is_done = (s_idx < stage_idx) or (current_stage == "COMPLETED")
            cursor.execute("""
                INSERT INTO case_milestones (id, case_id, stage, title, is_completed, completed_by, completed_at)
                VALUES (?, ?, ?, ?, ?, ?, ?);
            """, (
                m_id, case_id, st.value, f"Completion of {st.value.replace('_', ' ').title()}",
                1 if is_done else 0, rm_id if is_done else None,
                (created_dt + timedelta(days=s_idx)).isoformat() if is_done else None
            ))

        # Add Documents from Requirements Matrix
        req_docs = get_required_documents_for_entity(juris, etype)
        for d_idx, doc_req in enumerate(req_docs[:6]):
            doc_id = f"DOC-{case_id}-{d_idx}"
            file_name = f"{cname.replace(' ', '_').lower()}_{doc_req.code.lower()}.pdf"
            fake_hash = hashlib.sha256(f"{cid}-{doc_req.code}-{i}".encode("utf-8")).hexdigest()
            doc_status = "APPROVED" if (stage_idx >= 3 or current_stage == "COMPLETED") else "PENDING_REVIEW"

            cursor.execute("""
                INSERT INTO document_vault (
                    id, client_id, case_id, document_type, title, file_name,
                    file_size_bytes, mime_type, sha256_checksum, verification_status,
                    verified_by, verified_at, issue_date, expiry_date,
                    is_certified_true_copy, is_apostilled, issuing_country, created_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
            """, (
                doc_id, cid, case_id, doc_req.code, doc_req.title, file_name,
                random.randint(120000, 2500000), "application/pdf", fake_hash,
                doc_status, "USR-COMPLIANCE-01" if doc_status == "APPROVED" else None,
                now.isoformat() if doc_status == "APPROVED" else None,
                "2024-01-10", "2027-01-10", 1 if doc_req.requires_certified_true_copy else 0,
                1 if doc_req.requires_apostille else 0, juris, created_at
            ))

        # Add Action Tasks
        task_id = f"TSK-{case_id}-01"
        cursor.execute("""
            INSERT INTO action_tasks (
                id, case_id, client_id, task_type, title, description, priority,
                status, assigned_to_user_id, assigned_role, due_date, is_sla_breached, created_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        """, (
            task_id, case_id, cid, "REVIEW_DOCUMENT", f"Perform Verification of Constitutional Documents for {cname}",
            "Verify official state stamp and registration seals against jurisdictional gazette.",
            "HIGH" if risk_tier == "HIGH" else "MEDIUM",
            "COMPLETED" if (stage_idx >= 4 or current_stage == "COMPLETED") else "OPEN",
            "USR-COMPLIANCE-01", "COMPLIANCE_OFFICER",
            (now + timedelta(days=2)).isoformat()[:10],
            1 if sla_status == "RED" else 0, created_at
        ))

        # Add Screening Hit if applicable
        if i % 4 == 0:
            hit_id = f"HIT-{case_id}-01"
            cursor.execute("""
                INSERT INTO screening_hits (
                    id, case_id, subject_name, subject_type, catalog_source,
                    hit_reference_id, matched_name, match_score, programs_or_tier,
                    disposition, reviewed_by, reviewed_at, clearance_rationale, created_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
            """, (
                hit_id, case_id, f"{fn} {ln}", "INDIVIDUAL", "OFAC_SDN",
                "10045", f"{fn} {ln}", 0.88, "SDGT / GLOMAG",
                "CLEARED_FALSE_POSITIVE" if stage_idx >= 5 else "OPEN",
                "USR-COMPLIANCE-01" if stage_idx >= 5 else None,
                now.isoformat() if stage_idx >= 5 else None,
                "False positive verified via passport number and date of birth mismatch." if stage_idx >= 5 else None,
                created_at
            ))

        # Add Risk Assessment
        ra_id = f"RSK-{case_id}"
        factors = [
            {"factor_name": "Geographic Risk", "raw_score": 4.0 if juris in ["US", "GB"] else 7.5, "weight": 0.25, "weighted_score": 1.0, "rationale": f"Incorporation jurisdiction {juris}"},
            {"factor_name": "Industry Risk", "raw_score": 5.0, "weight": 0.20, "weighted_score": 1.0, "rationale": f"NAICS sector {naics}"},
            {"factor_name": "Entity Structure", "raw_score": 4.5, "weight": 0.15, "weighted_score": 0.67, "rationale": f"{etype} entity type"},
            {"factor_name": "PEP & Sanctions", "raw_score": 6.0 if (i % 8 == 0) else 1.0, "weight": 0.25, "weighted_score": 0.5, "rationale": "Clear of true positive sanctions matches"},
            {"factor_name": "Product Volume", "raw_score": 4.0, "weight": 0.15, "weighted_score": 0.6, "rationale": "Standard institutional credit facilities"}
        ]
        cursor.execute("""
            INSERT INTO risk_assessments (
                id, client_id, case_id, composite_score, risk_tier, review_frequency_months,
                factors_json, has_overrides, created_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
        """, (
            ra_id, cid, case_id, comp_score, risk_tier, refresh_freq,
            json.dumps(factors), 0, created_at
        ))

        # Add Audit Trail Event
        audit_id = f"AUD-{uuid.uuid4().hex[:12]}"
        audit_payload = {
            "id": audit_id,
            "entity_type": "CLIENT",
            "entity_id": cid,
            "action": "CREATE",
            "actor_id": rm_id,
            "timestamp": created_at,
            "prev_hash": last_audit_hash,
            "summary": f"Initial prospective record created for {cname}"
        }
        current_hash = hashlib.sha256(json.dumps(audit_payload, sort_keys=True).encode("utf-8")).hexdigest()
        
        cursor.execute("""
            INSERT INTO audit_events (
                id, entity_type, entity_id, action, actor_id, actor_name,
                actor_role, timestamp, change_summary, previous_event_hash, event_hash
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        """, (
            audit_id, "CLIENT", cid, "CREATE", rm_id, rms[i % len(rms)][1],
            "RELATIONSHIP_MANAGER", created_at,
            f"Prospect client record created for {cname}",
            last_audit_hash, current_hash
        ))
        last_audit_hash = current_hash

    conn.commit()
    print(f"[*] Successfully seeded {num_clients} clients and associated onboarding records.")
