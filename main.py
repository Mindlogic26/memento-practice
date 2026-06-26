from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs, urlparse

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # 1. Parse the name from the web URL (e.g., ?name=John)
        query_components = parse_qs(urlparse(self.path).query)
        user_name = query_components.get("name", ["Stranger"])[0]

        # 2. Set up the web response headers
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        # 3. Send the custom message back to the browser
        message = f"Hello {user_name}, welcome to your app! Your practice server is working."
        self.wfile.write(message.encode('utf-8'))
        return