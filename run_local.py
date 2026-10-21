"""Run the dashboard locally: python run_local.py  ->  http://127.0.0.1:8050"""
from dashboard.app import app

if __name__ == "__main__":
    app.run(debug=False, host="127.0.0.1", port=8050)
