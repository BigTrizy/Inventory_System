import psycopg


def check_database():

    try:
        connection = psycopg.connect(
            host="database",
            dbname="inventory_db",
            user="temporaryadmin",
            password="temporarypassword",
            port=5432
        )

        cursor = connection.cursor()

        cursor.execute("SELECT 1")

        result = cursor.fetchone()

        cursor.close()
        connection.close()

        return result[0] == 1

    except Exception as e:
        print(e)
        return False