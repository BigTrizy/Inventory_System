import psycopg


def get_connection():
    return psycopg.connect(
        host="database",
        dbname="inventory_db",
        user="temporaryadmin",
        password="temporarypassword",
        port=5432,
    )

def check_database():
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1")
                result = cursor.fetchone()

        return result[0] == 1

    except Exception as e:
        print(e)
        return False

def check_inventory():
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM products")
                return cursor.fetchall()

    except Exception as e:
        print(e)
        return []