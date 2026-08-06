from scripts.database import get_connection


def get_suppliers():
    #print("GET PRODUCT CALLED")
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM suppliers")
                result = cursor.fetchall()

                suppliers = []

                for row in result:
                    suppliers.append({
                        "id": row[0],
                        "name": row[1],
                        "phone": row[2],
                        "address": row[3],
                        "description": row[4]
                    })
                #print(suppliers)
                return suppliers

    except Exception as e:
        print(f"Database error: {e}")
        return []