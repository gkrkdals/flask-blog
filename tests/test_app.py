def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"My Portfolio Blog" in response.data

def test_post_detail(client):
    response = client.get('/post/1')
    assert response.status_code == 200
    assert b"1" in response.data

def test_create_post_page(client):
    response = client.get('/create')
    assert response.status_code == 200
    assert b"\xec\x83\x88 \xea\xb8\x80 \xec\x9e\x91\xec\x84\xb1" in response.data # "새 글 작성" in utf-8
