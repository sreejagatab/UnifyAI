# monitoring_routes.py
from flask import Blueprint, jsonify
from ..services.MonitoringService import get_system_status, get_api_usage

monitoring_routes = Blueprint('monitoring_routes', __name__)

@monitoring_routes.route('/status', methods=['GET'])
def status():
    try:
        status = get_system_status()
        return jsonify(status), 200
    except Exception as e:
        print(f"System status error: {e}")
        return jsonify({"error": "Failed to retrieve system status"}), 500

@monitoring_routes.route('/api-usage', methods=['GET'])
def api_usage():
    try:
        usage = get_api_usage()
        return jsonify(usage), 200
    except Exception as e:
        print(f"API usage error: {e}")
        return jsonify({"error": "Failed to retrieve API usage data"}), 500
