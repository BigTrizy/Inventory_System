from scripts.database import get_connection
from scripts.requests.get_products import search_products_ids

def search_transactions(product, date, time):
    with get_connection() as connection:
            with connection.cursor() as cursor:
                if product == None:
                    product = "*"
                else: 
                    products = search_products_ids() 
                if date == None:
                    date = "*"
                if time == None:
                    time = "*"

                cursor.execute(
                    """
                    SELECT * FROM transactions WHERE 
                    
                    """,
                    (id,)
                    )
                product = cursor.fetchall()

                
                return {
                    
                    }
                