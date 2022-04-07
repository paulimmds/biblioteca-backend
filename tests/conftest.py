import pytest
from application import create_app

@pytest.fixture()
def app():
    app = create_app('development')
    app.config.update({
        'TESTING': True,
    })

    yield app

@pytest.fixture()
def test_client(app):
    return app.test_client()