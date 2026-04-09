"""Very basic shipping calculator backend.

Run: python Shipping_Cost_Calculator.py
Open: http://127.0.0.1:8000/
"""

import json
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


def calculate_shipping_cost(weight: float, rate: float) -> float:
    if weight < 0 or rate < 0:
        raise ValueError("Weight and rate must be non-negative.")
    return weight * rate


class ShippingHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        web_dir = Path(__file__).resolve().parent / "web"
        super().__init__(*args, directory=str(web_dir), **kwargs)

    def do_POST(self):
        if self.path != "/calculate":
            self.send_error(404, "Not Found")
            return

        content_length = int(self.headers.get("Content-Length", "0"))
        raw = self.rfile.read(content_length)

        try:
            body = json.loads(raw.decode("utf-8"))
            weight = float(body.get("weight"))
            rate = float(body.get("rate"))
            shipping_cost = calculate_shipping_cost(weight, rate)
        except (TypeError, ValueError, json.JSONDecodeError):
            self.send_json(
                400,
                {"ok": False, "error": "Invalid input. Use non-negative numbers."},
            )
            return

        self.send_json(200, {"ok": True, "shipping_cost": round(shipping_cost, 2)})

    def send_json(self, status_code: int, data: dict) -> None:
        payload = json.dumps(data).encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)


def main() -> None:
    host = "127.0.0.1"
    port = 8000
    server = ThreadingHTTPServer((host, port), ShippingHandler)
    print(f"Server running on http://{host}:{port}/")
    print("Press Ctrl+C to stop")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
