from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from utils import validate_user_input, is_valid_email
from app.models import User

api = Blueprint("api", __name__)

@api.route("/users", methods=["GET"])
def get_users():
    return jsonify(User.find_all()), 200

@api.route("/users/<id>", methods=["GET"])
def get_user(id):
    user = User.find_one(id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user), 200



@api.route("/users", methods=["POST"])
def create_user():
    data = request.json
    required_fields = ["name", "email", "password"]
    is_valid, error_message = validate_user_input(data, required_fields)
    if not is_valid:
        return jsonify({"error": error_message}), 400
    if not is_valid_email(data["email"]):
        return jsonify({"error": "Invalid email format"}), 400
    data["password"] = generate_password_hash(data["password"])
    user_id = User.insert(data)
    return jsonify({"id": str(user_id)}), 201

@api.route("/users/<id>", methods=["PUT"])
def update_user(id):
    data = request.json
    if "password" in data:
        data["password"] = generate_password_hash(data["password"])
    User.update(id, data)
    return jsonify({"message": "User updated"}), 200

@api.route("/users/<id>", methods=["DELETE"])
def delete_user(id):
    User.delete(id)
    return jsonify({"message": "User deleted"}), 200
