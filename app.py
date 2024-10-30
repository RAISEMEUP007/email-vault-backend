from flask import Flask, request, jsonify
import pymysql
import hashlib
import datetime
from flask_cors import CORS

app = Flask(__name__)

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'password',
    'database': 'email_vault'
}

# Enable CORS for all routes
CORS(app)

# Hashing function
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to create a database connection
def get_db_connection():
    connection = pymysql.connect(**db_config)
    return connection

# Signup Route
@app.route('/signup', methods=['POST'])
def signup():
    data = request.json  # Get the JSON data from the request
    print(data)

    # Extracting user data from the request
    first_name = data.get('firstName')
    last_name = data.get('lastName')
    company_name = data.get('companyName')
    email = data.get('email')
    password = data.get('password')

    # Validate the input data
    if not all([first_name, last_name, company_name, email, password]):
        return jsonify({"error": "All fields are required"}), 400

    # Hash the password
    hashed_password = hash_password(password)

    # Create a new user in the database
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO users (first_name, last_name, company_name, email, password, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (first_name, last_name, company_name, email, hashed_password, datetime.datetime.now(), datetime.datetime.now())
        )
        connection.commit()
        user_id = cursor.lastrowid  # Get the new user's ID
        cursor.close()
        connection.close()

        return jsonify({"message": "User created successfully", "userId": user_id}), 201

    except pymysql.MySQLError as e:
        print(e)
        return jsonify({"error": "Database error"}), 500

# Signin Route
@app.route('/signin', methods=['POST'])
def signin():
    data = request.json

    email = data.get('email')
    password = data.get('password')

    # Validate input
    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

    # Hash the provided password
    hashed_password = hash_password(password)

    try:
        connection = get_db_connection()
        cursor = connection.cursor(pymysql.cursors.DictCursor)

        # Query to find user with provided email and password
        cursor.execute(
            "SELECT * FROM users WHERE email = %s AND password = %s",
            (email, hashed_password)
        )
        user = cursor.fetchone()
        print (user)

        cursor.close()
        connection.close()

        if user:
            # Successful authentication
            return jsonify({"message": "Sign-in successful", "userId": user['id']}), 200
        else:
            return jsonify({"error": "Invalid email or password"}), 401

    except pymysql.MySQLError as e:
        print(f"Error with database: {e}")
        return jsonify({"error": "Database error"}), 500

if __name__ == '__main__':
    app.run(debug=True)
