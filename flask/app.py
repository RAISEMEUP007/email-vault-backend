from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from routes.router import register_blueprint

load_dotenv('test.env')
load_dotenv('local.env')
load_dotenv('.env.secrets')

app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

# Register the blueprints with the app
app.register_blueprint(register_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
