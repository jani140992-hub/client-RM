"""
NexusCRM Periodic Batch AML Rescreening Job.
Automates scheduled portfolio-wide rescreening against refreshed OFAC SDN and PEP lists.
"""

from nexus.database.connection import get_db_session
from nexus.services.kyc_aml_service import KYCAMLService

def run_batch_rescreen():
    print("[*] Initiating portfolio-wide periodic AML rescreening...")
    with get_db_session() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, client_id FROM onboarding_cases;")
        cases = cursor.fetchall()

        total_hits = 0
        for row in cases:
            case_id, client_id = row[0], row[1]
            res = KYCAMLService.screen_entity_and_ubos(case_id, client_id)
            total_hits += res["total_hits_found"]

        print(f"[+] Batch rescreening complete across {len(cases)} cases. Total hits detected: {total_hits}.")

if __name__ == "__main__":
    run_batch_rescreen()
