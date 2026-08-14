from fastapi.testclient import TestClient
from scripts.main import app

test_app = TestClient(app)
def test_health():
    response = test_app.get("/health")
    assert response.status_code == 200
    assert response.json()["api"] == "healthy"


def test_product_search():
    response = test_app.get("/products")
    assert response.status_code == 200
    assert response.json()[0]["id"] == 1
    assert response.json()[0]["sku"] == "DELL-LAPTOP-32GB-BLK"

def
    