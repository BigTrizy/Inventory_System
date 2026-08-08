from scripts.database import get_connection

def set_product_stock(id, qty):
	with get_connection() as connection:
	    with connection.cursor() as cursor:
	        cursor.execute(
	            """
	            SELECT * FROM products WHERE id = %s
	            """,
	            (id,)
	            )

	        product = cursor.fetchone()
	        if product is None:
	        	return{"error: Product not found."}

	        current_stock = product[3]
	        new_stock = qty + current_stock

	        if new_stock < 0:
	        	return {
	        	"Impossible to complete transaction"
	        	"Current Stock": current_stock,
	        	"Remaining after transaction": new_stock
	        	}

	        cursor.execute(
	        	"""
	        	UPDATE products SET stock = %s WHERE id = %s
				""",(new_stock, id))

	        return {
	                "id": product[0],
	                "sku": product[1],
	                "name": product[2],
	                "Stock PreTransaction": current_stock,
	                "Stock Movement": qty,
	                "Stock PostTransaction": new_stock
	            }