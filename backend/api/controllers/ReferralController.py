# ReferralController.py
from flask import request, jsonify
from ..services.ReferralService import track_referral, get_referral_data

@app.route('/api/referral', methods=['POST'])
def add_referral():
    data = request.json
    try:
        referral_result = track_referral(data)
        return jsonify(referral_result)
    except Exception as e:
        print(f"Error adding referral: {e}")
        return jsonify({"error": "Referral addition failed"}), 400
