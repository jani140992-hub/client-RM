"""
NexusCRM Database Migrations Engine.
Manages automated schema version tracking and idempotent execution of schema upgrades.
"""

import sqlite3
import logging
from typing import List, Tuple
from nexus.database.schema import initialize_database

logger = logging.getLogger("nexus.database.migrations")

MIGRATIONS: List[Tuple[int, str, str]] = [
    (1, "initial_schema_v3_4", "Initial database schema with clients, cases, documents, UBOs, and audit trails."),
    (2, "add_performance_indices", "CREATE INDEX IF NOT EXISTS idx_clients_composite ON clients(risk_tier, onboarding_status);"),
    (3, "add_audit_actor_index", "CREATE INDEX IF NOT EXISTS idx_audit_actor ON audit_events(actor_id, timestamp);")
]

def run_migrations(conn: sqlite3.Connection):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS schema_migrations (
            version INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            applied_at TEXT NOT NULL
        );
    """)
    conn.commit()

    cursor.execute("SELECT version FROM schema_migrations ORDER BY version ASC;")
    applied_versions = {row[0] for row in cursor.fetchall()}

    for version, name, sql_or_func in MIGRATIONS:
        if version not in applied_versions:
            logger.info(f"Applying migration {version}: {name}")
            if version == 1:
                initialize_database(conn)
            else:
                cursor.execute(sql_or_func)
            
            cursor.execute("""
                INSERT INTO schema_migrations (version, name, applied_at)
                VALUES (?, ?, datetime('now'));
            """, (version, name))
            conn.commit()

    logger.info("All schema migrations applied successfully.")
