from app import app

def test_home():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello from Flask CI/CD Pipeline!" in response.data
    
