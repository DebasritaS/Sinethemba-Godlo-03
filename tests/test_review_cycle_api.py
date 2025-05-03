from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_start_and_complete_review_cycle():
    cycle_id = "cycle-1"
    reviewer_id = "reviewer-1"
    description = "Quarterly access review"

    # Start a new cycle
    response = client.post("/review-cycles/", params={
        "cycle_id": cycle_id,
        "reviewer_id": reviewer_id,
        "description": description
    })
    assert response.status_code == 200
    assert response.json()["message"] == "Cycle started successfully"

    # Complete the cycle
    response = client.post(f"/review-cycles/{cycle_id}/complete")
    assert response.status_code == 200
    assert response.json()["message"] == "Cycle completed"

def test_list_all_and_active_cycles():
    response = client.get("/review-cycles/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

    response = client.get("/review-cycles/active")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
