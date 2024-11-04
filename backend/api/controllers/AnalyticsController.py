# AnalyticsController.py
from flask import jsonify
from ..services.AnalyticsService import generate_report

@app.route('/api/analytics/report', methods=['GET'])
def fetch_analytics_report():
    try:
        report = generate_report()
        return jsonify(report)
    except Exception as e:
        print(f"Error fetching analytics report: {e}")
        return jsonify({"error": "Failed to fetch report"}), 500
