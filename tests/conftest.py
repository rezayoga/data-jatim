import pytest

from app import create_app
from app.models import db, Ptsl

@pytest.fixture(scope='module')
def new_ptsl():
    ptsl = Ptsl('Kabupaten Malang', 1, 2, 3)
    return ptsl


@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app()
    flask_app.config.from_object('config.TestingConfig')

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as testing_client:
        # Establish an application context
        with flask_app.app_context():
            yield testing_client  # this is where the testing happens!


@pytest.fixture(scope='module')
def init_database(test_client):
    # Create the database and the database table
    db.create_all()

    # Insert user data
    ptsl1 = Ptsl('Kabupaten Malang', 1, 2, 3)
    ptsl2 = Ptsl('Kota Batu', 4, 5, 6)
    db.session.add(ptsl1)
    db.session.add(ptsl2)

    # Commit the changes for the users
    db.session.commit()

    yield  # this is where the testing happens!

    db.drop_all()
