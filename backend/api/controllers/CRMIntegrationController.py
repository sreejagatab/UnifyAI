# CRMIntegrationController.py
from flask import request, jsonify
from ..services.CRMIntegrationService import sync_crm_data

@app.route('/api/crm/sync', methods=['POST'])
def sync_crm():
    data = request.json
    try:
        result = sync_crm_data(data)
        return jsonify({"status": "CRM Sync Success"}), 200
    except Exception as e:
        print(f"CRM sync error: {e}")
        return jsonify({"error": "CRM Sync failed"}), 500
