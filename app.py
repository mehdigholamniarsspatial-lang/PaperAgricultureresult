"""Vercel entry point (zero-configuration Flask).

Vercel detects this file and serves every request through the Flask
instance named `app` — here, the server behind the Dash dashboard.
"""
from dashboard.app import server as app  # noqa: F401  (Vercel looks for `app`)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8050)
