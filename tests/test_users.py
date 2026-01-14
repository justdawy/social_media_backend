from .utils import register_and_login

def test_get_own_profile(client):
    login_response = register_and_login(client)
    token = login_response.json['access_token']
    
    # Get profile
    response = client.get('/users/me', headers={
        'Authorization': f'Bearer {token}'
    })
    
    assert response.status_code == 200
    assert response.json.get('username') == 'testuser'
    
def test_get_user(client):
    login_response = register_and_login(client)
    token = login_response.json['access_token']
    
    # Get profile
    response = client.get('/users/1', headers={
        'Authorization': f'Bearer {token}'
    })
    
    user = response.json.get('user')
    
    assert response.status_code == 200
    assert user.get('username') == 'testuser'
    
def test_edit_current_user(client):
    login_response = register_and_login(client)
    token = login_response.json['access_token']
    
    # Edit profile
    response = client.put('/users/me/edit', headers={
        'Authorization': f'Bearer {token}'
    }, json={
        'display_name': 'Test User 2',
        'bio': 'Test User 2 Bio',
        'location': 'USA',
        'website': 'example.com',
        'profile_picture_url': 'example.com/testuser2/profile_picture',
        'cover_photo_url': 'example.com/testuser2/cover_photo'
    })
    
    assert response.status_code == 200
    user = response.json.get('user')
    assert user.get('email') == 'test@example.com'
    assert user.get('display_name') == 'Test User 2'
    assert user.get('bio') == 'Test User 2 Bio'
    assert user.get('location') == 'USA'
    assert user.get('website') == 'example.com'
    assert user.get('profile_picture_url') == 'example.com/testuser2/profile_picture'
    assert user.get('cover_photo_url') == 'example.com/testuser2/cover_photo'