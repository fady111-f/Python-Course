"""
🌐 Python Mastery Platform — Web App & Dashboard Local Server
==============================================================
Launches a local web server hosting:
  - 📊 Interactive Web Dashboard (http://localhost:8000/dashboard/)
  - 📚 Documentation Site      (http://localhost:8000/docs/)

Usage:
    python server.py
"""

import http.server
import socketserver
import webbrowser
import os
import sys
import subprocess
import threading
import time

# ===== UTF-8 Support =====
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

PORT = 8000
REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
SITE_DIR = os.path.join(REPO_ROOT, "site")


def build_docs_if_needed():
    """Ensure MkDocs site is built."""
    if not os.path.exists(SITE_DIR) or not os.listdir(SITE_DIR):
        print("  🔨 Building MkDocs documentation site...")
        try:
            subprocess.run([sys.executable, "-m", "mkdocs", "build"], cwd=REPO_ROOT, check=True)
            print("  ✅ Docs built successfully.")
        except Exception as e:
            print(f"  ⚠️ Could not build docs: {e}")


class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=REPO_ROOT, **kwargs)

    def end_headers(self):
        # Prevent caching for live development
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()

    def do_GET(self):
        # Redirect root to dashboard
        if self.path == "/" or self.path == "":
            self.send_response(302)
            self.send_header("Location", "/dashboard/")
            self.end_headers()
            return
        
        # Route /docs/ to /site/
        if self.path.startswith("/docs"):
            rel_path = self.path[5:] # remove /docs
            if not rel_path or rel_path == "/":
                rel_path = "/index.html"
            target_path = os.path.normpath(os.path.join(SITE_DIR, rel_path.lstrip("/")))
            if os.path.exists(target_path) and os.path.isfile(target_path):
                self.send_response(200)
                if target_path.endswith(".html"):
                    self.send_header("Content-Type", "text/html; charset=utf-8")
                elif target_path.endswith(".css"):
                    self.send_header("Content-Type", "text/css")
                elif target_path.endswith(".js"):
                    self.send_header("Content-Type", "application/javascript")
                self.end_headers()
                with open(target_path, "rb") as f:
                    self.wfile.write(f.read())
                return

        return super().do_GET()


def main():
    build_docs_if_needed()

    print("=" * 60)
    print(" 🌐 PYTHON MASTERY PLATFORM — LOCAL WEB SERVER")
    print("=" * 60)
    print(f"\n  🚀 Server running at http://localhost:{PORT}")
    print(f"  📊 Web Dashboard : http://localhost:{PORT}/dashboard/")
    print(f"  📚 Documentation : http://localhost:{PORT}/docs/")
    print("\n  Press Ctrl+C to stop the server.\n")

    # Automatically open browser after 1 second
    def open_browser():
        time.sleep(1.2)
        webbrowser.open(f"http://localhost:{PORT}/dashboard/")

    threading.Thread(target=open_browser, daemon=True).start()

    try:
        with socketserver.TCPServer(("", PORT), CustomHTTPRequestHandler) as httpd:
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 Server stopped gracefully.")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error starting server: {e}")


if __name__ == "__main__":
    main()
