import pytest

from app import create_app
from app.extensions import db
from app.models import User

@pytest.fixture()
def app():
    """Create application for testing"""
    app = create_app('test_config.py')
    
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()
        
@pytest.fixture()
def client(app):
    """Create test client"""
    return app.test_client()

@pytest.fixture()
def runner(app):
    """Create test CLI runner"""
    return app.test_cli_runner()