"""
NexusCRM Unified Server & Web Application.
Provides high-concurrency multithreaded HTTP REST routing, static asset serving, and optional ASGI bridge.
"""

import os
import sys
import json
import logging
from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import ThreadingMixIn
from urllib.parse import urlparse, parse_qs
from typing import Dict, Any

from nexus.config import get_config
from nexus.api.router import get_router
from nexus.database.connection import get_db_session
from nexus.database.migrations import run_migrations
from nexus.database.seed_data import seed_database

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")
logger = logging.getLogger("nexus.server")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "ui", "static")

class ThreadingHTTPServer(ThreadingMixIn, HTTPServer):
    daemon_threads = True

class NexusHTTPHandler(BaseHTTPRequestHandler):
    def _send_cors_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type, Authorization, X-Requested-With")

    def do_OPTIONS(self):
        self.send_response(204)
        self._send_cors_headers()
        self.end_headers()

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path
        query = parse_qs(parsed.query)

        # Route 1: Serve Static Web Portal UI
        if path == "/" or path == "/index.html":
            self._serve_file(os.path.join(STATIC_DIR, "index.html"), "text/html; charset=utf-8")
            return

        if path.startswith("/static/"):
            rel_path = path[len("/static/"):]
            full_path = os.path.join(STATIC_DIR, rel_path)
            content_type = "text/plain"
            if rel_path.endswith(".html"):
                content_type = "text/html; charset=utf-8"
            elif rel_path.endswith(".css"):
                content_type = "text/css; charset=utf-8"
            elif rel_path.endswith(".js"):
                content_type = "application/javascript; charset=utf-8"
            elif rel_path.endswith(".png"):
                content_type = "image/png"
            elif rel_path.endswith(".svg"):
                content_type = "image/svg+xml"

            self._serve_file(full_path, content_type)
            return

        # Route 2: REST API
        if path.startswith("/api/"):
            router = get_router()
            status, body = router.route_request("GET", path, query, None)
            self._send_json_response(status, body)
            return

        # Fallback 404
        self._send_json_response(404, {"success": False, "error": f"Resource not found: {path}"})

    def do_POST(self):
        parsed = urlparse(self.path)
        path = parsed.path
        query = parse_qs(parsed.query)

        content_length = int(self.headers.get("Content-Length", 0))
        body = None
        if content_length > 0:
            raw_body = self.rfile.read(content_length)
            try:
                body = json.loads(raw_body.decode("utf-8"))
            except Exception as e:
                self._send_json_response(400, {"success": False, "error": f"Invalid JSON body: {str(e)}"})
                return

        router = get_router()
        status, resp_body = router.route_request("POST", path, query, body)
        self._send_json_response(status, resp_body)

    def _serve_file(self, file_path: str, content_type: str):
        if not os.path.exists(file_path):
            self._send_json_response(404, {"success": False, "error": "File not found"})
            return
        try:
            with open(file_path, "rb") as f:
                content = f.read()
            self.send_response(200)
            self.send_header("Content-Type", content_type)
            self.send_header("Content-Length", str(len(content)))
            self._send_cors_headers()
            self.end_headers()
            self.wfile.write(content)
        except Exception as e:
            logger.error(f"Error serving {file_path}: {e}")
            self._send_json_response(500, {"success": False, "error": str(e)})

    def _send_json_response(self, status: int, body: Any):
        payload = json.dumps(body).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(payload)))
        self._send_cors_headers()
        self.end_headers()
        self.wfile.write(payload)

    def log_message(self, format, *args):
        # Clean formatted logging
        if get_config().server.debug:
            logger.debug("%s - - [%s] %s" % (self.address_string(), self.log_date_time_string(), format % args))

def start_server(host: str = "127.0.0.1", port: int = 8090):
    # Ensure database is initialized and seeded
    with get_db_session() as conn:
        run_migrations(conn)
        seed_database(conn, num_clients=35)

    server_address = (host, port)
    httpd = ThreadingHTTPServer(server_address, NexusHTTPHandler)
    logger.info(f"NexusCRM Enterprise HTTP Server listening on http://{host}:{port}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        logger.info("Server shutting down gracefully...")
        httpd.server_close()

if __name__ == "__main__":
    cfg = get_config()
    start_server(host=cfg.server.host, port=cfg.server.port)
