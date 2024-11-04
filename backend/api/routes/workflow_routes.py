# workflow_routes.py
from flask import Blueprint, request, jsonify
from ..services.WorkflowService import create_workflow, fetch_workflows
from ..utils import validate_input

workflow_routes = Blueprint('workflow_routes', __name__)

@workflow_routes.route('/create', methods=['POST'])
def create():
    data = request.json
    try:
        if not validate_input(data):
            return jsonify({"error": "Invalid workflow data"}), 400
        workflow = create_workflow(data)
        return jsonify(workflow), 201
    except Exception as e:
        print(f"Workflow creation error: {e}")
        return jsonify({"error": "Failed to create workflow"}), 500

@workflow_routes.route('/list', methods=['GET'])
def list_workflows():
    try:
        workflows = fetch_workflows()
        return jsonify(workflows), 200
    except Exception as e:
        print(f"Workflow retrieval error: {e}")
        return jsonify({"error": "Failed to retrieve workflows"}), 500
