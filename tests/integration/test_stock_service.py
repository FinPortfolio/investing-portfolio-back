from fastapi.testclient import TestClient

from fastapi_app.main import main_app

client = TestClient(main_app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Everything is OK!!!"}
