import pytest

from project import app as _app


@pytest.fixture(scope="session")
def app():
    app = _app.create_app()
    app.config.update({ "TESTING": True })

    yield app

@pytest.fixture(scope="session")
def client(app):
    return app.test_client()