import pytest

# 인증 정보 설정
TEST_ID = "dev"
TEST_PWD = "12345"

def test_unauthenticated_post_access(client):
    """
    시나리오 1: 로그인이 되어있지 않을 때 post_controller(ex: /create) 진입 시 인증 실패
    """
    response = client.get('/create')
    
    # 템플릿의 에러 메시지, JSON 응답, 또는 리다이렉트 파라미터 등을 통해 NOT_AUTHENTICATED를 확인
    # 구현 방식에 따라 assert 방법을 조절해주세요.
    assert response.status_code in [401, 302]
    assert b"NOT_AUTHENTICATED" in response.data

def test_login_wrong_info(client):
    """
    시나리오 2: 로그인 시도 시 ID/PWD가 맞지 않으면 인증 실패
    """
    response = client.post('/login', data={
        'user_id': TEST_ID,
        'password': 'wrong_password'
    })
    
    # 로그인 실패 시 에러 메시지 출력 확인
    assert response.status_code in [400, 401, 200]
    assert b"WRONG_INFO" in response.data

def test_login_success(client):
    """
    시나리오 3: 로그인 시도 시 ID/PWD가 맞으면 로그인 성공 및 post_controller 접근 가능
    """
    # 1. 로그인 요청
    login_response = client.post('/login', data={
        'user_id': TEST_ID,
        'password': TEST_PWD
    }, follow_redirects=True)
    
    # 로그인 성공 시 이유(reason)가 표시되지 않고 패스됨을 확인
    assert login_response.status_code == 200
    assert b"NOT_AUTHENTICATED" not in login_response.data
    assert b"WRONG_INFO" not in login_response.data
    
    # 2. 로그인 상태에서 post_controller 자원 접근 시도
    post_response = client.get('/create')
    assert post_response.status_code == 200
    # 보호된 페이지인 글 작성 텍스트가 정상적으로 로드되는지 확인
    assert b"\xec\x83\x88 \xea\xb8\x80 \xec\x9e\x91\xec\x84\xb1" in post_response.data

def test_logout(client):
    """
    시나리오 번외: 로그아웃 로직 정상 작동 확인
    """
    # 먼저 로그인
    client.post('/login', data={'user_id': TEST_ID, 'password': TEST_PWD})
    
    # 로그아웃
    logout_response = client.get('/logout', follow_redirects=True)
    assert logout_response.status_code == 200
    
    # 보호된 페이지 접근 시 다시 차단되는지 확인
    post_response = client.get('/create')
    assert b"NOT_AUTHENTICATED" in post_response.data