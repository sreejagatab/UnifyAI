# analytics_routes.py
from flask import Blueprint, jsonify
from ..services.AnalyticsService import generate_report

analytics_routes = Blueprint('analytics_routes', __name__)

@analytics_routes.route('/report', methods=['GET'])
def report():
    try:
        report_data = generate_report()
        return jsonify(report_data), 200
    except Exception as e:
        print(f"Analytics error: {e}")
        return jsonify({"error": "Failed to generate report"}), 500
