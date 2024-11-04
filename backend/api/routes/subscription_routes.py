# subscription_routes.py
from flask import Blueprint, request, jsonify
from ..services.SubscriptionService import check_subscription, upgrade_subscription
from ..utils import validate_input

subscription_routes = Blueprint('subscription_routes', __name__)

@subscription_routes.route('/check', methods=['POST'])
def check_subscription():
    data = request.json
    try:
        access_level = check_subscription(data['user_id'])
        return jsonify(access_level), 200
    except Exception as e:
        print(f"Subscription check error: {e}")
        return jsonify({"error": "Subscription check failed"}), 500

@subscription_routes.route('/upgrade', methods=['POST'])
def upgrade():
    data = request.json
    try:
        result = upgrade_subscription(data['user_id'], data['plan_id'])
        return jsonify({"message": "Subscription upgraded"}), 200
    except Exception as e:
        print(f"Subscription upgrade error: {e}")
        return jsonify({"error": "Failed to upgrade subscription"}), 500
