import pytest
import os
from blog import create_app

@pytest.fixture
def app():
    app = create_app({
        'TESTING': True,
        'DATABASE': os.path.join(os.getcwd(), 'blog/db/blog-db-dev'),
    })

    yield app

@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()
