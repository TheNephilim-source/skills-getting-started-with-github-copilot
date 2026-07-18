from fastapi.testclient import TestClient

from src.app import app, activities


def test_unregister_participant_removes_email_from_activity():
    client = TestClient(app)
    activity_name = "Chess Club"
    activity = activities[activity_name]
    original_participants = activity["participants"].copy()
    email = "new.student@mergington.edu"

    try:
        response = client.post(
            f"/activities/{activity_name}/signup",
            params={"email": email},
        )
        assert response.status_code == 200
        assert email in activity["participants"]

        response = client.delete(
            f"/activities/{activity_name}/signup",
            params={"email": email},
        )
        assert response.status_code == 200
        assert email not in activity["participants"]
    finally:
        activity["participants"] = original_participants
