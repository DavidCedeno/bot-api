import pytest
import os
from fastapi.testclient import TestClient
from src.main import app

pytestmark = pytest.mark.integration

@pytest.mark.skipif(not os.getenv("RUN_INTEGRATION"), reason="Integration tests require real database")
def test_db_connection():
    with TestClient(app) as client:
        response = client.get("/api/v1/health/db-check")
        assert response.status_code == 200
        assert response.json() == {"result": 1}