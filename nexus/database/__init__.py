"""
NexusCRM Database Package.
Exports connection pool, schema initializers, migrations, and seed utilities.
"""

from nexus.database.connection import get_db_pool, get_db_session
from nexus.database.schema import initialize_database
from nexus.database.migrations import run_migrations
from nexus.database.seed_data import seed_database

__all__ = [
    "get_db_pool",
    "get_db_session",
    "initialize_database",
    "run_migrations",
    "seed_database",
]
