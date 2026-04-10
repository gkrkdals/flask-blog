from flask import Blueprint, request, session
login_bp = Blueprint('login', __name__)

TEST_ID = 'dev'
TEST_PWD = '12345'

@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    """사용자 로그인을 처리합니다.
    GET 요청 시 로그인 페이지를 반환하고, POST 요청 시 자격 증명을 통해 로그인을 수행합니다.
    ---
    tags:
      - Auth API
    parameters:
      - name: user_id
        in: formData
        type: string
        required: false
        description: 사용자 계정 아이디
      - name: password
        in: formData
        type: string
        required: false
        description: 사용자 계정 비밀번호
    responses:
      200:
        description: 로그인 성공 및 로그인 페이지 로드 완료
      401:
        description: 잘못된 계정 정보 입력
    """
    if request.method == 'POST':
        user_id = request.form.get('user_id')
        password = request.form.get('password')
        if user_id == TEST_ID and password == TEST_PWD:
            session['logged_in'] = True
            return 'LOGIN_SUCCESS', 200
        else:
            return 'WRONG_INFO', 401
    return 'LOGIN_PAGE'

@login_bp.route('/logout', methods=['GET'])
def logout():
    """사용자 로그아웃을 처리합니다.
    서버 측 세션을 초기화시켜 로그아웃 상태로 전환합니다.
    ---
    tags:
      - Auth API
    responses:
      200:
        description: 로그아웃 성공 메시지
    """
    session.clear()
    return 'LOGOUT_SUCCESS', 200
