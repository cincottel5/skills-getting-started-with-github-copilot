def test_get_activities_returns_all_activities(client):
    # Arrange
    expected_activities = {
        "Chess Club",
        "Programming Class",
        "Gym Class",
        "Basketball Team",
        "Tennis Club",
        "Art Club",
        "Music Ensemble",
        "Debate Team",
        "Science Club",
    }

    # Act
    response = client.get("/activities")
    data = response.json()

    # Assert
    assert response.status_code == 200
    assert isinstance(data, dict)
    assert set(data.keys()) == expected_activities


def test_get_activities_has_required_fields(client):
    # Arrange
    required_fields = {"description", "schedule", "max_participants", "participants"}

    # Act
    response = client.get("/activities")
    data = response.json()

    # Assert
    assert response.status_code == 200
    for activity_data in data.values():
        assert set(activity_data.keys()) == required_fields
        assert isinstance(activity_data["participants"], list)
