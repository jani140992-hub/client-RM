"""
NexusCRM Enterprise Command Line Interface.
Provides CLI operations for batch screening, risk calculation, audit verification, and server orchestration.
"""

import sys
import argparse
import json
from tabulate import tabulate if False else None

from nexus.config import get_config
from nexus.server import start_server
from nexus.database.connection import get_db_session
from nexus.database.migrations import run_migrations
from nexus.database.seed_data import seed_database
from nexus.services.client_service import ClientService
from nexus.services.risk_service import RiskService
from nexus.catalogs.ofac_sdn_sanctions import get_ofac_search_engine
from nexus.catalogs.pep_registry import get_pep_screening_engine

def main():
    parser = argparse.ArgumentParser(description="NexusCRM Institutional Client Onboarding CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Command: serve
    serve_parser = subparsers.add_parser("serve", help="Start the NexusCRM HTTP Server and Web Portal")
    serve_parser.add_argument("--host", default="127.0.0.1", help="Host interface (default: 127.0.0.1)")
    serve_parser.add_argument("--port", type=int, default=8080, help="Port number (default: 8080)")

    # Command: seed
    seed_parser = subparsers.add_parser("seed", help="Seed database with synthetic institutional accounts")
    seed_parser.add_argument("--count", type=int, default=40, help="Number of clients to generate")

    # Command: screen
    screen_parser = subparsers.add_parser("screen", help="Screen a person or entity against sanctions and PEP catalogs")
    screen_parser.add_argument("query", help="Name to screen")

    # Command: clients
    clients_parser = subparsers.add_parser("clients", help="List active institutional clients")
    clients_parser.add_argument("--limit", type=int, default=20, help="Maximum records")

    # Command: risk
    risk_parser = subparsers.add_parser("risk", help="Calculate institutional risk score for a client")
    risk_parser.add_argument("client_id", help="Client ID to assess")

    args = parser.parse_args()

    if args.command == "serve":
        start_server(host=args.host, port=args.port)
    elif args.command == "seed":
        with get_db_session() as conn:
            run_migrations(conn)
            seed_database(conn, num_clients=args.count)
    elif args.command == "screen":
        oe = get_ofac_search_engine()
        pe = get_pep_screening_engine()
        ofac_hits = oe.search_name(args.query)
        pep_hits = pe.screen_individual(args.query)
        print(f"=== KYC/AML Screening Results for '{args.query}' ===")
        print(f"OFAC SDN Matches ({len(ofac_hits)}):")
        for h in ofac_hits:
            print(f"  - [{h['match_score']*100:.1f}%] {h['name']} ({h['sdn_type']}) - Programs: {h['programs']}")
        print(f"\nPEP Matches ({len(pep_hits)}):")
        for p in pep_hits:
            print(f"  - [{p['match_score']*100:.1f}%] {p['full_name']} (Tier {p['tier']} - {p['country_code']}) - Role: {p['role_title']}")
    elif args.command == "clients":
        clients = ClientService.get_all_clients(limit=args.limit)
        print(f"{'Client Number':<12} {'Client Name':<38} {'Segment':<22} {'Risk':<8} {'Stage':<20}")
        print("-" * 105)
        for c in clients:
            print(f"{c['client_number']:<12} {c['name'][:36]:<38} {c['client_segment'][:20]:<22} {c['risk_tier']:<8} {c['current_stage']:<20}")
    elif args.command == "risk":
        result = RiskService.calculate_client_risk(args.client_id)
        print(f"=== Composite Risk Assessment for {args.client_id} ===")
        print(f"Composite Score: {result['composite_score']} / 10.0")
        print(f"Assigned Risk Tier: {result['risk_tier']}")
        print(f"Periodic Review Interval: Every {result['review_frequency_months']} months")
        print("\nFactor Decomposition:")
        for f in result['factors']:
            print(f"  - {f['factor_name']:<20}: Raw={f['raw_score']:<4} Weight={f['weight']:<4} Weighted={f['weighted_score']:<4} ({f['rationale']})")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
