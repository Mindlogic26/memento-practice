from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs, urlparse
from datetime import datetime

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # 1. Parse the parameters from the URL
        query_components = parse_qs(urlparse(self.path).query)
        user_name = query_components.get("name", [None])[0]
        birth_year_str = query_components.get("year", [None])[0]

        # 2. Set up web response headers
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # 3. If NO data is provided, show the multi-input form
        if not user_name or not birth_year_str:
            html_form = """
            <!DOCTYPE html>
            <html>
            <head>
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <style>
                    body { font-family: sans-serif; text-align: center; padding: 40px 20px; background: #fafafa; color: #333; }
                    .card { background: white; padding: 30px; border-radius: 12px; box-shadow: 0 4px 10px rgba(0,0,0,0.05); max-width: 400px; margin: 0 auto; }
                    input { padding: 12px; font-size: 16px; width: 100%; max-width: 280px; margin-bottom: 15px; border: 1px solid #ccc; border-radius: 6px; box-sizing: border-box; }
                    button { padding: 12px 24px; font-size: 16px; background: #000; color: #fff; border: none; border-radius: 6px; cursor: pointer; width: 100%; max-width: 280px; font-weight: bold; }
                </style>
            </head>
            <body>
                <div class="card">
                    <h2>Life Engine Practice</h2>
                    <form action="/" method="get">
                        <input type="text" name="name" placeholder="Your Name" required><br>
                        <input type="number" name="year" placeholder="Birth Year (e.g., 1995)" min="1900" max="2026" required><br>
                        <button type="submit">Calculate Life Statistics</button>
                    </form>
                </div>
            </body>
            </html>
            """
            self.wfile.write(html_form.encode('utf-8'))
            return

        # 4. Data processing and math engine
        try:
            birth_year = int(birth_year_str)
            current_year = 2026
            
            # Calculate metrics
            age_this_year = current_year - birth_year
            weeks_lived = age_this_year * 52
            
        except ValueError:
            # Fallback if someone types a broken number
            age_this_year = "Unknown"
            weeks_lived = "Unknown"

        # 5. Return the calculated data visualization
        html_result = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <style>
                body {{ font-family: sans-serif; text-align: center; padding: 40px 20px; background: #111; color: #eee; }}
                .card {{ background: #222; padding: 30px; border-radius: 12px; max-width: 400px; margin: 0 auto; border: 1px solid #333; }}
                .highlight {{ color: #00ffcc; font-size: 28px; font-weight: bold; margin: 10px 0; }}
                a {{ display: inline-block; margin-top: 25px; color: #00ffcc; text-decoration: none; font-size: 14px; }}
            </style>
        </head>
        <body>
            <div class="card">
                <h1>{user_name}'s Metrics</h1>
                <p>Turning age this year:</p>
                <div class="highlight">{age_this_year}</div>
                <p>Approximate weeks lived:</p>
                <div class="highlight">~ {weeks_lived:,} weeks</div>
                <a href="/">← Reset Calculator</a>
            </div>
        </body>
        </html>
        """
        self.wfile.write(html_result.encode('utf-8'))
        return