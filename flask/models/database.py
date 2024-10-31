import os
from rococo.data import MySqlAdapter

def get_db_connection():
    try:
        return MySqlAdapter(os.getenv('DB_HOST'), int(os.getenv('DB_PORT')), os.getenv('DB_USER'), os.getenv('DB_PASSWORD'), os.getenv('DB_NAME'))
    except Exception as e:
        print(e)
        return None