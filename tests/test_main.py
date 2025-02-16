import re

def test_fetch_root(client):
    response = client.get('/')
    assert response.status_code == 200
    assert re.search(r'text/html', response.headers['Content-Type'])
