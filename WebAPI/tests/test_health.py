from fastapi.testclient import TestClient
from scripts.main import app

test_app = TestClient(app)
def test_health():
    response = test_app.get("/health")
    assert response.status_code == 200
    assert response.json()["api"] == "healthy"