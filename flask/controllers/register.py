from flask import request, jsonify
from models.users import create_user, get_user
from rococo.messaging import RabbitMqConnection
import os
from rococo.messaging import RabbitMqConnection
import pika


def signup():
    try:
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
        # user = create_user(first_name, last_name, company_name, email, password)

        message = {
            "event": "USER_CREATED",
            "data": {
                "confirmation_link": 'confirmation_link',
                "recipient_name": 'user.name',
            },
            "to_emails": ['axelpcxs3@gmail.com'],
        }

        # print(message)
        # with RabbitMqConnection('localhost', 15672, 'guest', 'guest', '/') as conn:
        #     print("------------------conn")
        #     print(conn)
        #     print("------------------conn====================")
        #     conn.send_message('hello_world', {'message': 'data'})
        connection = pika.BlockingConnection(
            pika.ConnectionParameters('localhost', 5672, '/', pika.PlainCredentials('guest', 'guest')))
        print("Connected to RabbitMQ")
        channel = connection.channel()
        channel.queue_declare(queue='sssss')
        channel.basic_publish(exchange='',
                              routing_key='hello',
                              body='Hello World!')
        print(" [x] Sent 'Hello World!'")
        connection.close()
        print("connection closed")
        return jsonify({"error": "test"}), 200
        # if user is not None:
        #     return jsonify({"message": "User created successfully", "userId": user}), 201
        # else:
        #     return jsonify({"error": "Database error"}), 500

    except Exception as e:
        return jsonify({"error": "Internal Server error"}), 500

def signin():
    try:
        print('---------------sddssdsdsd')
        EMAIL_TRANSMITTER_QUEUE_NAME = os.getenv('QUEUE_NAME_PREFIX') + os.getenv('EmailServiceProcessor_QUEUE_NAME')

        message = {
            "event": "USER_CREATED",
            "data": {
                "confirmation_link": 'confirmation_link',
                "recipient_name": 'user.name',
            },
            "to_emails": ['user.email'],  # A list of email addresses where the email should be sent.
        }

        with RabbitMqConnection(os.getenv('RABBITMQ_HOST'), int(os.getenv('RABBITMQ_PORT')), os.getenv('RABBITMQ_USER'), os.getenv('RABBITMQ_PASSWORD'), os.getenv('RABBITMQ_VIRTUAL_HOST')) as conn:
            conn.send_message('queue_name', {'message': 'data'})
        return jsonify({"error": "test"}), 200
        # data = request.json
        #
        # email = data.get('email')
        # password = data.get('password')
        #
        # if not email or not password:
        #     return jsonify({"error": "Email and password are required"}), 400
        #
        # user_id = get_user(email, password)
        # if user_id:
        #     return jsonify({"message": "Sign-in successful", "userId": user_id}), 200
        # else:
        #     return jsonify({"error": "Invalid email or password"}), 401
    except Exception as e:
        return jsonify({"error": "Internal Server error"}), 500