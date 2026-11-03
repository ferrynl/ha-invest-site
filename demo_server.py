"""Serve the product site and the original app in an isolated public demo."""
import mimetypes
import os
from http.server import ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

from demo import DEMO_READS, ensure_demo
from server import Handler, store

site = Path(os.environ.get("SITE_DIR", "/site"))
pages = {"/" + file.name: file for file in site.glob("*.html")}
pages["/"] = site / "index.html"
pages.update({"/assets/" + file.name: file for file in (site / "assets").iterdir() if file.is_file()})

demo_api = DEMO_READS | {"/api/session", "/api/account/dashboard", "/api/fx", "/api/reports/charges", "/api/instrument/company"}
asset_suffixes = (".js", ".css", ".ttf", ".json", ".svg", ".png")


class PublicDemo(Handler):
    def do_GET(self):
        url = urlsplit(self.path)
        if url.path in pages:
            file = pages[url.path]
            return self.respond(file.read_bytes(), kind=mimetypes.guess_type(file.name)[0], etag=True)
        if url.path == "/app" or (url.path == "/app/" and parse_qs(url.query).get("profile") != ["demo"]):
            self.send_response(302)
            self.send_header("Location", "/app/?profile=demo")
            self.send_header("Content-Length", "0")
            self.end_headers()
            return
        if not url.path.startswith("/app/"):
            return self.send_error(404)

        route = url.path.removeprefix("/app")
        if route.startswith("/api/"):
            if route not in demo_api:
                return self.respond({"error": "Unavailable in the public demo."}, 403)
        elif route != "/" and not route.endswith(asset_suffixes):
            return self.send_error(404)

        # Ignore caller-controlled profile selection and use the app's demo store.
        while "X-HomeInvest-Profile" in self.headers:
            del self.headers["X-HomeInvest-Profile"]
        self.headers["X-HomeInvest-Profile"] = "demo"
        self.path = route + ("?" + url.query if url.query else "")
        super().do_GET()

    def do_POST(self):
        self.close_connection = True
        return self.respond({"error": "The public demo is read-only."}, 405)


if __name__ == "__main__":
    ensure_demo(store.root / "demo")
    ThreadingHTTPServer(("0.0.0.0", int(os.environ.get("PORT", "80"))), PublicDemo).serve_forever()
