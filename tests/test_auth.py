def test_register_success(client):
    response = client.post(
        '/auth/register',
        json={
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'password123',
        },
    )

    assert response.status_code == 201
    assert b'User created succesfully' in response.data


def test_login_success(client):
    # register
    client.post(
        '/auth/register',
        json={
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'password123',
        },
    )

    # then log in
    response = client.post(
        '/auth/login', json={'username': 'testuser', 'password': 'password123'}
    )

    assert response.status_code == 200
    assert 'access_token' in response.json
