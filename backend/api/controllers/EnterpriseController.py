# EnterpriseController.py
from flask import jsonify, request
from ..services.EnterpriseService import manage_roles, get_enterprise_report

@app.route('/api/enterprise/roles', methods=['POST'])
def manage_enterprise_roles():
    data = request.json
    try:
        result = manage_roles(data)
        return jsonify(result), 200
    except Exception as e:
        print(f"Role management failed: {e}")
        return jsonify({"error": "Failed to manage roles"}), 400
