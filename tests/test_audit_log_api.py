from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_log_and_fetch_audit_entries():
    # Log an action
    response = client.post("/audit-logs/", params={
        "user_id": "admin-1",
        "action": "Completed review",
        "entity": "ReviewCycle(cycle-1)"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["user_id"] == "admin-1"
    assert "timestamp" in data

    # Get logs for a user
    response = client.get("/audit-logs/user/admin-1")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

    # Get all logs
    response = client.get("/audit-logs/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
