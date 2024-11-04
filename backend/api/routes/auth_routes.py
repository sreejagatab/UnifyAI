# auth_routes.py
from flask import Blueprint, request, jsonify
from ..services.AuthService import login_user, register_user, verify_token
from ..utils import validate_input

auth_routes = Blueprint('auth_routes', __name__)

@auth_routes.route('/login', methods=['POST'])
def login():
    data = request.json
    try:
        if not validate_input(data, required_fields=["username", "password"]):
            return jsonify({"error": "Invalid input"}), 400
        token = login_user(data['username'], data['password'])
        return jsonify({"token": token}), 200
    except Exception as e:
        print(f"Login error: {e}")
        return jsonify({"error": "Login failed"}), 401

@auth_routes.route('/signup', methods=['POST'])
def signup():
    data = request.json
    try:
        if not validate_input(data, required_fields=["username", "email", "password"]):
            return jsonify({"error": "Invalid input"}), 400
        user = register_user(data)
        return jsonify({"message": "User registered successfully"}), 201
    except Exception as e:
        print(f"Signup error: {e}")
        return jsonify({"error": "Signup failed"}), 500
