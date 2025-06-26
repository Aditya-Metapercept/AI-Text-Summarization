from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_summarize_success():
    response = client.post("/summarize", json={"text": "This is a long enough text to test the summarization functionality of our API."})
    assert response.status_code == 200
    assert "summary" in response.json()

def test_summarize_empty():
    response = client.post("/summarize", json={"text": ""})
    assert response.status_code == 400

def test_summarize_too_short():
    response = client.post("/summarize", json={"text": "Too short."})
    assert response.status_code == 400
