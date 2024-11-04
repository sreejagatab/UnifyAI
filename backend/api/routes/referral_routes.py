# referral_routes.py
from flask import Blueprint, request, jsonify
from ..services.ReferralService import add_referral, get_referral_data
from ..utils import validate_input

referral_routes = Blueprint('referral_routes', __name__)

@referral_routes.route('/add', methods=['POST'])
def add_referral():
    data = request.json
    try:
        if not validate_input(data, required_fields=["referrer_id", "referred_email"]):
            return jsonify({"error": "Invalid input"}), 400
        add_referral(data['referrer_id'], data['referred_email'])
        return jsonify({"message": "Referral added successfully"}), 201
    except Exception as e:
        print(f"Referral addition error: {e}")
        return jsonify({"error": "Referral addition failed"}), 500

@referral_routes.route('/get/<user_id>', methods=['GET'])
def get_referral(user_id):
    try:
        referral_data = get_referral_data(user_id)
        return jsonify(referral_data), 200
    except Exception as e:
        print(f"Error retrieving referral data: {e}")
        return jsonify({"error": "Failed to retrieve referral data"}), 500
