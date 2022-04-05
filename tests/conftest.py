import pytest
from application import init_app

@pytest.fixture()
def app():
    app = init_app('development')
    app.config.update({
        'TESTING': True,
    })

    yield app

@pytest.fixture()
def test_client(app):
    return app.test_client()