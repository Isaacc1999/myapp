import pytest
from app.app import app  # Correct import path

@pytest.fixture
def client():
    app.testing = True  # Flask uses .testing, not .config['TESTING']
    with app.test_client() as client:
        yield client

def test_square_number(client):
    response = client.get('/square_number?number=2')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Square of 2.0 is 4.0"
