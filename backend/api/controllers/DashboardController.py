# DashboardController.py
from flask import jsonify
from ..services.DashboardService import get_dashboard_data

@app.route('/api/dashboard', methods=['GET'])
def fetch_dashboard_data():
    try:
        data = get_dashboard_data()
        return jsonify(data), 200
    except Exception as e:
        print(f"Dashboard fetch error: {e}")
        return jsonify({"error": "Failed to fetch dashboard data"}), 500
