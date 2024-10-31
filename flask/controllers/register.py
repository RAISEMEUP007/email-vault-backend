from flask import request, jsonify
from models.users import create_user, get_user


def signup():
    data = request.json

    # Extracting user data from the request
    first_name = data.get('firstName')
    last_name = data.get('lastName')
    company_name = data.get('companyName')
    email = data.get('email')
    password = data.get('password')

    # Validate the input data
    if not all([first_name, last_name, company_name, email, password]):
        return jsonify({"error": "All fields are required"}), 400

    # Create a new user in the database
    user = create_user(first_name, last_name, company_name, email, password)
    if user is not None:
        return jsonify({"message": "User created successfully", "userId": user}), 201
    else:
        return jsonify({"error": "Database error"}), 500

def signin():
    data = request.json

    email = data.get('email')
    password = data.get('password')

    # Validate input
    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

    user_id = get_user(email, password)
    if user_id:
        return jsonify({"message": "Sign-in successful", "userId": user_id}), 200
    else:
        return jsonify({"error": "Invalid email or password"}), 401
