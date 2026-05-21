import os
import requests
import pytest

# Die URL ziehen wir uns flexibel aus einer Umgebungsvariable
BASE_URL = os.getenv("APP_URL", "http://localhost:8000")

def test_health_endpoint():
    response = requests.get(f"{BASE_URL}/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_ready_endpoint():
    response = requests.get(f"{BASE_URL}/ready")
    assert response.status_code == 200
    assert response.json()["status"] == "ready"