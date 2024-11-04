# SpotInstanceController.py
from flask import jsonify
from ..services.SpotInstanceService import manage_spot_instances

@app.route('/api/spot-instances/manage', methods=['POST'])
def manage_spot():
    try:
        manage_spot_instances()
        return jsonify({"status": "Spot instances adjusted"}), 200
    except Exception as e:
        print(f"Spot instance adjustment failed: {e}")
        return jsonify({"error": "Failed to adjust spot instances"}), 500
