import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"

@pytest.mark.api
def test_get_usuario():
    response = requests.get(f"{BASE_URL}/users/1")
    assert response.status_code == 200
    assert response.json()["username"] == "Bret"

@pytest.mark.api
def test_create_post():
    payload = {"title": "QA Automation", "body": "Proyecto Final", "userId": 1}
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    assert response.status_code == 201
    assert response.json()["title"] == "QA Automation"