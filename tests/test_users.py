def test_get_own_profile(client):
    # register and login
    client.post('/auth/register', json={
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'password123'
    })

    login_response = client.post('/auth/login', json={
        'username': 'testuser',
        'password': 'password123'
    })
    token = login_response.json['access_token']
    
    # Get profile
    response = client.get('/users/me', headers={
        'Authorization': f'Bearer {token}'
    })
    
    assert response.status_code == 200
    assert response.json.get('username') == 'testuser'