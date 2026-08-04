from fastapi import FastAPI
from scripts.database import check_database, check_inventory


app = FastAPI()


@app.get("/")
def root():
    return {
        "status": "API is running"
    }


@app.get("/health")
def health():

    database_status = check_database()

    return {
        "api": "healthy",
        "database": "healthy" if database_status else "unavailable"
    }

@app.get("/products")
def products():
    inventory = check_inventory()

    products = []

    for row in inventory:
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