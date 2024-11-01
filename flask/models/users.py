import hashlib
import datetime
from dataclasses import field, dataclass
from rococo.models import VersionedModel
from models.database import get_db_connection

@dataclass
class Users(VersionedModel):
    first_name : str
    last_name : str
    company_name : str
    email: str
    password: str
    referral_code: str
    created_at: datetime

# Hashing function
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Create user in the database
def create_user(first_name, last_name, company_name, email, password):
    hashed_password = hash_password(password)

    with get_db_connection() as adapter:
        try:
            result = adapter.save('users', {
                'first_name' : first_name,
                'last_name' : last_name,
                'company_name' : company_name,
                'email' : email,
                'password' : hashed_password,
                'created_at' : datetime.datetime.now(),
                'changed_on' : datetime.datetime.now(),
            })
            return result
        except Exception as e:
            print(e)
            return None


def get_user(email, password):
    hashed_password = hash_password(password)

    email = f'"{email}"'
    hashed_password = f'"{hashed_password}"'

    with get_db_connection() as adapter:
        try:
            query = f'SELECT * FROM users WHERE email = {email} AND password = {hashed_password};'
            result = adapter.execute_query(query, {})
            return result
        except Exception as e:
            print(f"Error with database: {e}")
            return None

