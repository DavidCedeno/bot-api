from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_check_live():
    response = client.get("/api/v1/health/live")
    assert response.status_code == 200
    assert response.json() == {"status": "alive"}

def test_check_ready():
    response = client.get("/api/v1/health/ready")
    assert response.status_code == 200
    assert response.json() == {"status": "ready"}