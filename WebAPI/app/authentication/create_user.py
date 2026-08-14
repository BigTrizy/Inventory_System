from scripts.database import get_connection
from argon2 import PasswordHasher

def verify_user_exist(username):
    with get_connection as connection:
        with connection.cursor() as cursor:
            cursor.excecute(
                """
                SELECT * FROM users WHERE username = %s
                """
                (username,)
            )
 
            user = cursor.fetchone()

            if user is not None:
                return True

            return False

def hash_password(password):
    password_hash = PasswordHasher()
    return password_hash



def create_user(username, access_level, password):
    if(verify_user_exist(username)== True):
        return "Error, user already exists."
    
    password_hash = hash_password(password)
    with get_connection as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                """

                """
            )