# email-vault-backend

export FLASK_APP=flask/app.py
export FLASK_ENV=development
poetry run flask run

sudo docker build -t my-flask-app .
sudo docker run -p 5000:5000 my-flask-app

sudo docker-compose down --volumes --remove-orphans
sudo docker system prune -a
sudo docker-compose build --no-cache
sudo docker compose up