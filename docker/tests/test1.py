import pytest
import requests


def test_response():
    url = "http://localhost:8080"
    response = requests.get(url)
    assert response.status_code == 200
