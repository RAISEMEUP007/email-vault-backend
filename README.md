# email-vault-backend

export FLASK_APP=flask/app.py
export FLASK_ENV=development
poetry run flask run

docker build -t my-flask-app .
docker run -p 5000:5000 my-flask-app
