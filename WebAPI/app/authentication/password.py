from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from scripts.database import get_connection


def hash_password(password):
    ph = PasswordHasher()
    return ph.hash(password)


def compare_password(username, user_password):
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT id FROM users WHERE username = %s
                    """,
                    (username,)
                )

                user = cursor.fetchone()

                if user is None:
                    return False, "User doesn't exist"

                user_id = user[0]

                cursor.execute(
                    """
                    SELECT password_hash
                    FROM users_passwords
                    WHERE user_id = %s
                    """,
                    (user_id,)
                )

                password = cursor.fetchone()

                if password is None:
                    return False, "Password doesn't match"

                db_hash = password[0]

                ph = PasswordHasher()
                ph.verify(db_hash, user_password)

    except VerifyMismatchError:
        return False, "Password doesn't match"

    except Exception as exception:
        return False, str(exception)

    return True, "Password matches"