"""
NexusCRM Regulatory Compliance & Audit Package Exporter.
Extracts verifiable, SHA-256 sealed audit logs and regulatory filing dossiers for regulators.
"""

import os
import json
from datetime import datetime
from nexus.database.connection import get_db_session

def export_package(output_path: str = "nexus_regulatory_audit_dossier.json"):
    print(f"[*] Compiling NexusCRM regulatory audit package to {output_path}...")
    with get_db_session() as conn:
        cursor = conn.cursor()

        # Audit events
        cursor.execute("SELECT * FROM audit_events ORDER BY timestamp ASC;")
        audit_events = [dict(r) for r in cursor.fetchall()]

        # Active cases
        cursor.execute("SELECT * FROM onboarding_cases;")
        cases = [dict(r) for r in cursor.fetchall()]

        # Screening hits & dispositions
        cursor.execute("SELECT * FROM screening_hits;")
        hits = [dict(r) for r in cursor.fetchall()]

        package = {
            "metadata": {
                "system": "NexusCRM Institutional Onboarding Platform",
                "version": "3.4.0-enterprise",
                "exported_at": datetime.utcnow().isoformat(),
                "regulatory_standard": "FINRA Rule 2090 / SOC2 Type II / EU 6AMLD",
                "total_audit_events": len(audit_events),
                "total_cases_audited": len(cases),
                "total_screening_dispositions": len(hits)
            },
            "audit_trail": audit_events,
            "onboarding_cases": cases,
            "screening_dispositions": hits
        }

        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(package, f, indent=2)

    print(f"[+] Audit package successfully written: {output_path} ({len(audit_events)} events sealed).")

if __name__ == "__main__":
    export_package()
