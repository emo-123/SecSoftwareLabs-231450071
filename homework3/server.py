from http.server import BaseHTTPRequestHandler, HTTPServer
import json

HOST = "127.0.0.1"
PORT = 8081

EVENTS = [
    {"id": 1, "severity": "low", "type": "login"},
    {"id": 2, "severity": "high", "type": "bruteforce"},
    {"id": 3, "severity": "medium", "type": "port-scan"},
    {"id": 4, "severity": "low", "type": "logout"},
    {"id": 5, "severity": "high", "type": "malware"},
    {"id": 6, "severity": "medium", "type": "failed-login"},
    {"id": 7, "severity": "low", "type": "file-access"},
    {"id": 8, "severity": "high", "type": "suspicious-login"},
    {"id": 9, "severity": "medium", "type": "policy-violation"},
    {"id": 10, "severity": "low", "type": "password-change"},
]


def make_summary():
    summary = {"total": len(EVENTS), "low": 0, "medium": 0, "high": 0}
    for event in EVENTS:
        summary[event["severity"]] += 1
    return summary


class Handler(BaseHTTPRequestHandler):

    def send_json(self, status, data):
        # Python nesnesi -> JSON string -> bytes
        body = json.dumps(data).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path == "/api/events":
            self.send_json(200, EVENTS)

        elif self.path == "/api/events/high":
            high_events = []
            for event in EVENTS:
                if event["severity"] == "high":
                    high_events.append(event)
            self.send_json(200, high_events)

        elif self.path == "/api/summary":
            self.send_json(200, make_summary())

        else:
            self.send_json(404, {"error": "Endpoint not found"})


if __name__ == "__main__":
    server = HTTPServer((HOST, PORT), Handler)
    print(f"Server calisiyor: http://{HOST}:{PORT}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer kapatildi.")
        server.server_close()
