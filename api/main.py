from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs, urlparse

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # 1. Parse the name from the web URL
        query_components = parse_qs(urlparse(self.path).query)
        user_name = query_components.get("name", [None])[0]

        # 2. Set up web response headers
        self.send_response(200)
        self.send_header('Content-type', 'text/html') # Changed to HTML!
        self.end_headers()

        # 3. If NO name is provided, show the input form webpage
        if not user_name:
            html_form = """
            <!DOCTYPE html>
            <html>
            <head>
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <style>
                    body { font-family: sans-serif; text-align: center; padding: 50px; background: #fafafa; }
                    input { padding: 10px; font-size: 16px; width: 80%; max-width: 300px; margin-bottom: 10px; }
                    button { padding: 10px 20px; font-size: 16px; background: #000; color: #fff; border: none; cursor: pointer; }
                </style>
            </head>
            <body>
                <h2>What is your name?</h2>
                <form action="/" method="get">
                    <input type="text" name="name" placeholder="Type your name here..." required><br>
                    <button type="submit">Submit</button>
                </form>
            </body>
            </html>
            """
            self.wfile.write(html_form.encode('utf-8'))
            return

        # 4. If a name IS provided, show the greeting page
        html_greeting = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <style>
                body {{ font-family: sans-serif; text-align: center; padding: 50px; background: #e6f7ff; }}
                a {{ display: inline-block; margin-top: 20px; color: #0070f3; }}
            </style>
        </head>
        <body>
            <h1>Hello {user_name}!</h1>
            <p>Welcome to your app. Your practice server is working flawlessly.</p>
            <a href="/">Try another name</a>
        </body>
        </html>
        """
        self.wfile.write(html_greeting.encode('utf-8'))
        return