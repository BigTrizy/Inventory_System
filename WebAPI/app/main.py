from fastapi import FastAPI
from scripts.database import check_database
from scripts.requests.get_products import get_products, search_products, search_products_id
from scripts.requests.get_suppliers import get_suppliers


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
    result = get_products()
    return result

@app.get("/products/search")
def search_product(name: str):
    return search_products(name)

@app.get("/products/{id}")
def search_product_id(id: int):
    return search_products_id(id)

@app.get("/suppliers")
def suppliers():
    result = get_suppliers()
    return result

