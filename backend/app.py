from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import socket
from datetime import datetime

APP_ENV = os.getenv("APP_ENV", "unknown")
APP_VERSION = os.getenv("APP_VERSION", "unknown")
HOSTNAME = socket.gethostname()


class Handler(BaseHTTPRequestHandler):

    def do_GET(self):

        message = (
            "Hello from Nginx Developer!\n"
            f"Environment: {APP_ENV}\n"
            f"Version: {APP_VERSION}\n"
            f"Container: {HOSTNAME}\n"
            f"Path: {self.path}\n"
            f"Time: {datetime.now()}\n"
        ).encode()

        print(f"Request received: {self.path}", flush=True)

        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.send_header("Content-Length", str(len(message)))
        self.end_headers()

        self.wfile.write(message)


server = HTTPServer(("0.0.0.0", 8000), Handler)

print("Backend started on port 8000", flush=True)

server.serve_forever()
