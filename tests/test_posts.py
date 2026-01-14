from .utils import register_and_login

def test_create_post(client):
    login_response = register_and_login(client)
    token = login_response.json['access_token']
    
    # Create post
    response = client.post('posts/create', headers={
        'Authorization': f'Bearer {token}'
    }, json={
        'title': 'Test Post',
        'content': 'Its Test Post'
    })
    
    post = response.json.get('post')
    
    assert response.status_code == 201
    assert post.get('id') == 1
    assert post.get('title') == 'Test Post'
    assert post.get('content') == 'Its Test Post'