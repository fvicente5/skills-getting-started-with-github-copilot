def test_unregister_removes_existing_participant(client):
    # Arrange
    activity_name = "Basketball Team"
    existing_email = "alex@mergington.edu"

    # Act
    unregister_response = client.delete(
        f"/activities/{activity_name}/signup",
        params={"email": existing_email},
    )
    activities_response = client.get("/activities")
    participants = activities_response.json()[activity_name]["participants"]

    # Assert
    assert unregister_response.status_code == 200
    assert existing_email not in participants


def test_unregister_returns_404_for_unknown_activity(client):
    # Arrange
    unknown_activity = "Unknown Club"
    email = "student@mergington.edu"

    # Act
    response = client.delete(
        f"/activities/{unknown_activity}/signup",
        params={"email": email},
    )

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_unregister_returns_404_for_non_enrolled_participant(client):
    # Arrange
    activity_name = "Chess Club"
    non_enrolled_email = "not.enrolled@mergington.edu"

    # Act
    response = client.delete(
        f"/activities/{activity_name}/signup",
        params={"email": non_enrolled_email},
    )

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Student is not signed up for this activity"
