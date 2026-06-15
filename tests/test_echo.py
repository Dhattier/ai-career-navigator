from fastapi.testclient import TestClient

from ai_career_navigator.main import app


def test_echo_endpoint() -> None:
    client = TestClient(app)

    response = client.post("/api/v1/echo", json={"message": "hello"})

    assert response.status_code == 200
    assert response.json() == {"message": "hello"}
