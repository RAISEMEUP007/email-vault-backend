import os
from rococo.data import MySqlAdapter

def get_db_connection():
    try:
        print(os.getenv('MYSQL_HOST'))
        print(os.getenv('MYSQL_PORT'))
        print(os.getenv('MYSQL_USER'))
        print(os.getenv('MYSQL_PASSWORD'))
        print(os.getenv('MYSQL_DATABASE'))
        return MySqlAdapter(os.getenv('MYSQL_HOST'), int(os.getenv('MYSQL_PORT')), os.getenv('MYSQL_USER'), os.getenv('MYSQL_PASSWORD'), os.getenv('MYSQL_DATABASE'))
    except Exception as e:
        print(e)
        return None