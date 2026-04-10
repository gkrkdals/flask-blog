from flask import Blueprint, render_template

post_bp = Blueprint('post', __name__)

@post_bp.route('/')
@post_bp.route('/home')
def home():
    """블로그 홈 화면을 조회합니다.
    작성된 게시물 목록 조회 뷰 템플릿을 렌더링하고 반환합니다.
    ---
    tags:
      - Post API
    responses:
      200:
        description: 홈 화면 HTML 템플릿 로드 성공
    """
    return render_template('home.html')

@post_bp.route('/post/<int:post_id>')
def post_detail(post_id):
    """특정 블로그 게시물의 상세 내용을 조회합니다.
    선택한 게시물의 ID를 바탕으로 상세 화면 템플릿을 반환합니다.
    ---
    tags:
      - Post API
    parameters:
      - name: post_id
        in: path
        type: integer
        required: true
        description: 조회할 게시물의 고유 ID
    responses:
      200:
        description: 게시물 상세 화면 HTML 템플릿 로드 성공
    """
    return render_template('post_detail.html', post_id=post_id)

@post_bp.route('/create')
def create_post():
    """새 게시물 작성 페이지를 반환합니다.
    사용자가 로그인되어 있는 경우에만 접근할 수 있는 글 작성 폼 템플릿입니다.
    ---
    tags:
      - Post API
    responses:
      200:
        description: 새 글 작성 폼 템플릿 반환
      401:
        description: 인증되지 않은 사용자의 접근 거부 동작
    """
    from flask import session
    if not session.get("logged_in"):
        return "NOT_AUTHENTICATED", 401
    return render_template('create_post.html')
