# SubscriptionController.py
from flask import request, jsonify
from ..services.SubscriptionService import check_subscription, upgrade_subscription

@app.route('/api/subscription', methods=['POST'])
def check_user_subscription():
    user_id = request.json.get('user_id')
    try:
        access_level = check_subscription(user_id)
        return jsonify(access_level)
    except Exception as e:
        print(f"Error checking subscription: {e}")
        return jsonify({"error": "Subscription check failed"}), 500
