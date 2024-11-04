# APIUsageController.py
from flask import jsonify
from ..services.APITrackingService import track_api_usage

@app.route('/api/api-usage', methods=['GET'])
def get_api_usage():
    try:
        usage_data = track_api_usage()
        return jsonify(usage_data), 200
    except Exception as e:
        print(f"API usage error: {e}")
        return jsonify({"error": "Failed to track API usage"}), 500
