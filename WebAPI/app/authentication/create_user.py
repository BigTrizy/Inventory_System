from scripts.database import get_connection
from scripts.authentication.password import hash_password

def verify_user_exist(username):
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT * FROM users WHERE username = %s
                """,
                (username,)
            )
 
            user = cursor.fetchone()

            if user is not None:
                return True

            return False

def verify_access_level_exist(access_level):
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT * FROM access_levels WHERE id = %s
                """,
                (access_level,)
            )
 
            access_level_exist = cursor.fetchone()

            if access_level_exist is not None:
                return True

            return False




def create_user(username, access_level, password):
    # The try makes it so the transaction is rolled back in case of either
    # one of the Inserts failing or one of the verify functions
    try:
        if verify_user_exist(username):
                return "Error: User already exists"
        if not verify_access_level_exist(access_level):
                    return "Error: Access Level doesn't exist"
        password_hash = hash_password(password)
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    """
                    INSERT INTO users (username, access_level) 
                    VALUES (%s, %s) 
                    RETURNING id
                    """,
                    (username, access_level)
                )
                user_id = cursor.fetchone()[0]
                cursor.execute(
                    """
                    INSERT INTO users_passwords (user_id, password_hash) 
                    VALUES (%s, %s)
                    """,
                    (user_id, password_hash)
                )
            return {"User Created:": username,
                    "Access Level": access_level}
    except Exception as exception:
        return {"Error Encountered. Rollback Applied.": str(exception)}
            