import re
from bs4 import BeautifulSoup

def test_fetch_posts(client):
    response = client.get('/posts/')
    assert response.status_code == 200
    assert re.search(r'text/html', response.headers['Content-Type'])

def test_fetch_post(client):
    response = client.get('/posts/test')
    assert response.status_code == 200
    assert re.search(r'text/html', response.headers['Content-Type'])
    # parser = BeautifulSoup(response.body, 'html.parser')
