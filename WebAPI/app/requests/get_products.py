from scripts.database import get_connection


def get_products():
    #print("GET PRODUCT CALLED")
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM products")
                result = cursor.fetchall()

                products = []

                for row in result:
                    products.append({
                        "id": row[0],
                        "sku": row[1],
                        "name": row[2],
                        "stock": row[3],
                        "stock_critical": row[4],
                        "description": row[5],
                        "supplier_id": row[6]
                    })
                #print(products)
                return products

    except Exception as e:
        print(f"Database error: {e}")
        return []

def search_products_id(id):
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT * FROM products WHERE id = %s
                """,
                (id,)
                )
            product = cursor.fetchone()

            
            return {
                "id": product[0],
                "sku": product[1],
                "name": product[2],
                "stock": product[3],
                "stock_critical": product[4],
                "description": product[5],
                "supplier_id": product[6]
                }
            return 

def search_products(name):
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT * FROM products WHERE name ILIKE %s
                """,
                (f"%{name}%",) 
                )
            rows = cursor.fetchall()
            products = []

            for row in rows:
                products.append({
                    "id": row[0],
                    "sku": row[1],
                    "name": row[2],
                    "stock": row[3],
                    "stock_critical": row[4],
                    "description": row[5],
                    "supplier_id": row[6]
                })
            return products