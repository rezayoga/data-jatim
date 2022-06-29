import pytest

from app import create_app
from app.models import db


@pytest.fixture(scope='module')
def test_client():
    app = create_app()
    app.config.from_object('config.DevelopmentConfig')
    with app.test_client() as testing_client:
        # Establish an application context
        with app.app_context():
            yield testing_client


"""
@pytest.fixture(scope='module')
def test_database():
    app = create_app()
    db.init_app(app)
    db.create_all()
    yield db  # testing happens here
    db.session.remove()
    db.drop_all()
"""
