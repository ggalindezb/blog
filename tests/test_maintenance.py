def test_ping(client):
    response = client.get('/maintenance/ping')
    assert response.data == b'{"ping":true}\n'
