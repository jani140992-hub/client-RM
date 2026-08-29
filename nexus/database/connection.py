"""
NexusCRM Database Connection Pool & Context Management.
Thread-safe SQLite connection factory configured for high concurrency with WAL mode and foreign key enforcement.
"""

import sqlite3
import threading
from contextlib import contextmanager
from typing import Generator
from nexus.config import get_config

class DatabaseConnectionPool:
    def __init__(self, db_path: str, timeout: float = 30.0, enable_wal: bool = True):
        self.db_path = db_path
        self.timeout = timeout
        self.enable_wal = enable_wal
        self._local = threading.local()
        self._lock = threading.Lock()
        self._init_db_settings()

    def _init_db_settings(self):
        conn = sqlite3.connect(self.db_path, timeout=self.timeout)
        try:
            if self.enable_wal:
                conn.execute("PRAGMA journal_mode = WAL;")
            conn.execute("PRAGMA synchronous = NORMAL;")
            conn.execute("PRAGMA foreign_keys = ON;")
            conn.execute("PRAGMA busy_timeout = 30000;")
            conn.commit()
        finally:
            conn.close()

    def get_connection(self) -> sqlite3.Connection:
        if not hasattr(self._local, "connection") or self._local.connection is None:
            conn = sqlite3.connect(self.db_path, timeout=self.timeout)
            conn.row_factory = sqlite3.Row
            conn.execute("PRAGMA foreign_keys = ON;")
            if self.enable_wal:
                conn.execute("PRAGMA journal_mode = WAL;")
            self._local.connection = conn
        return self._local.connection

    @contextmanager
    def session(self) -> Generator[sqlite3.Connection, None, None]:
        conn = self.get_connection()
        try:
            yield conn
            conn.commit()
        except Exception:
            conn.rollback()
            raise

_pool: DatabaseConnectionPool = None
_pool_lock = threading.Lock()

def get_db_pool() -> DatabaseConnectionPool:
    global _pool
    if _pool is None:
        with _pool_lock:
            if _pool is None:
                config = get_config()
                _pool = DatabaseConnectionPool(
                    db_path=config.database.db_path,
                    timeout=config.database.timeout_seconds,
                    enable_wal=config.database.enable_wal
                )
    return _pool

@contextmanager
def get_db_session() -> Generator[sqlite3.Connection, None, None]:
    pool = get_db_pool()
    with pool.session() as conn:
        yield conn
