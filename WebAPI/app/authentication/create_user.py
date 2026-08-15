from scripts.database import get_connection
from scripts.authentication.password import hash_password
from scripts.standards.standards import validate_username, normalize_username

def verify_user_exist(username):
    with get_connection() as connection:
        with connection.cursor() as cursor:
            username = normalize_username(username)
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
    # The transaction is rolled back with the help of the connection() 
    # context manager. I case of anything returning an error in the try block.
    try:

        # Normalize and then verify the username. Then SQL requests to 
        # make sure everything is valid for creation.
        username_valid, message, username = validate_username(username)
        if not username_valid:
            return (False, message)
        if verify_user_exist(username):
            return (False, "Error: User already exists")
        if not verify_access_level_exist(access_level):
            return (False, "Error: Access Level doesn't exist")

        password_hash = hash_password(password)

        # User creation Queries.
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
            return (
                True,
                {
                    "User Created": username,
                    "Access Level": access_level
                }
            )
        
    # Wide net that catches any exception and throws it back. 
    # Should eventually be more granular
    except Exception as exception:
        return (False,{"Error Encountered. Rollback Applied.": str(exception)})
            