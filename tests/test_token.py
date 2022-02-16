import json
import requests
import pytest

def test_response():
    ploads = {'name': 'admin', 'password': 'qwerty'}
    r = requests.post('http://localhost:8080/login', params=ploads)
    data = json.loads(r.text)
    global token
    token = (data['content'])
    assert len(token) == 32

def test_user_name():
    ploads2 = {'token': token}
    r2 = requests.get('http://localhost:8080/user', params=ploads2)
    data2 = json.loads(r2.text)
    content = (data2['content'])
    assert content == "admin"
