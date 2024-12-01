from blog import create_app

def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing


def test_hello(client):
    response = client.get('/maintenance/ping')
    assert response.data == b'{"ping":true}\n'
