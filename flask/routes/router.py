from flask import Blueprint
from controllers.register import signin, signup

# Create a Blueprint for user registration and authentication
register_blueprint = Blueprint('register', __name__)

# Signup Route
@register_blueprint.route('/signup', methods=['POST'])
def signup_route():
    return signup()

# Signin Route
@register_blueprint.route('/signin', methods=['POST'])
def signin_route():
    return signin()
