from fastapi.testclient import TestClient

from src.main import build_app


def test_ping():
    client = TestClient(
        app=build_app(),
        follow_redirects=False,
    )
    response = client.get("/ping")
    assert response.status_code == 200
