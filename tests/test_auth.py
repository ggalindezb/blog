import re
import json

def test_good_login(client):
    data = {
        'key': '2a1e0fc0-7bab-4aa0-9e2f-23d7ddd81241'
    }
    response = client.post(
            '/auth/login',
            content_type='application/json',
            data=json.dumps(data))
    payload = json.loads(response.text)
    assert response.status_code == 201
    assert re.search(r'application/json', response.headers['Content-Type'])
    assert 'jwt' in payload

def test_bad_login(client):
    data = {
        'key': 'bad_key'
    }
    response = client.post(
            '/auth/login',
            content_type='application/json',
            data=json.dumps(data))
    assert response.status_code == 401
    assert response.text == ''
