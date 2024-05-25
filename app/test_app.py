import pytest
from app import app, get_db_connection


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            yield client


def test_get_users(client):
    rv = client.get('/')
    assert rv.status_code == 200
    assert isinstance(rv.json, list)


def test_db_connection():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT 1')
    result = cursor.fetchone()
    assert result is not None
    cursor.close()
    conn.close()
