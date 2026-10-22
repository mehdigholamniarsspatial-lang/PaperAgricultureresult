"""Run the dashboard locally: python run_local.py  ->  http://127.0.0.1:8050 (or $PORT)"""
import os

from dashboard.app import app

if __name__ == "__main__":
    app.run(debug=False, host="127.0.0.1", port=int(os.environ.get("PORT", 8050)))
