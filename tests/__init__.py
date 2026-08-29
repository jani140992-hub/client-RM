"""
NexusCRM Automated Test Suite Initializer.
Ensures clean database schema and seed data before running tests.
"""

from nexus.database.connection import get_db_session
from nexus.database.migrations import run_migrations
from nexus.database.seed_data import seed_database

# Initialize database schema and base seed records for clean testing
with get_db_session() as conn:
    run_migrations(conn)
    seed_database(conn, num_clients=20)
