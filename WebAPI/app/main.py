from fastapi import FastAPI
from scripts.database import check_database
from scripts.requests.get_products import get_products, search_products, search_products_id
from scripts.requests.get_suppliers import get_suppliers
from scripts.update_requests.update_stocks import set_product_stock 
from pydantic import BaseModel

class TransactionRequest(BaseModel):
    id: int
    qty: int
    user: str
    reason: str

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

@app.post("/products/update")
def update_products_stock(transaction: TransactionRequest):
    return set_product_stock(
        transaction.id,
        transaction.qty,
        transaction.user,
        transaction.reason
    )

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



