# WorkflowController.py
from flask import request, jsonify
from ..models import WorkflowModel
from ..services.WorkflowService import create_workflow, update_workflow
from ..utils import validate_input

@app.route('/api/workflow', methods=['POST'])
def create_new_workflow():
    data = request.json
    try:
        if not validate_input(data):
            raise ValueError("Invalid input data")
        workflow = create_workflow(data)
        return jsonify(workflow), 201
    except Exception as e:
        print(f"Error creating workflow: {e}")
        return jsonify({"error": "Failed to create workflow"}), 400

@app.route('/api/workflow/<id>', methods=['PUT'])
def update_existing_workflow(id):
    data = request.json
    try:
        if not validate_input(data):
            raise ValueError("Invalid input data")
        workflow = update_workflow(id, data)
        return jsonify(workflow)
    except Exception as e:
        print(f"Error updating workflow: {e}")
        return jsonify({"error": "Failed to update workflow"}), 400
