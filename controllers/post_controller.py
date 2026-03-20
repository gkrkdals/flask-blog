from flask import Blueprint

post_bp = Blueprint('post', __name__)

@post_bp.route('/')
@post_bp.route('/home')
def home():
    return """
    <h2>My Portfolio Blog</h2>
    <ul>
        <li><a href='/post/1'>Docker 컨테이너로 개인 서버 구축하기</a></li>
        <li><a href='/post/2'>아몬드 멸치볶음 레시피</a></li>
        <li><a href='/post/3'>임페리얼 스타우트 시음기</a></li>
    </ul>
    <br>
    <a href='/create'>[+ 새 글 작성하기]</a>
    """

@post_bp.route('/post/<int:post_id>')
def post_detail(post_id):
    return f"""
    <h2>블로그 글 상세 읽기</h2>
    <p>현재 <b>{post_id}번</b> 글의 본문을 읽고 있습니다.</p>
    <p>글 내용</p>
    <br>
    <a href='/'>[← 목록으로 돌아가기]</a>
    """

@post_bp.route('/create')
def create_post():
    from flask import session
    if not session.get("logged_in"):
        return "NOT_AUTHENTICATED", 401
    return """
    <h2>새 글 작성</h2>
    <form action="/" method="get">
        <label>제목: <input type="text" name="title" placeholder="글 제목 입력"></label><br><br>
        <label>내용:<br><textarea name="content" rows="6" cols="40" placeholder="본문 내용을 입력하세요"></textarea></label><br><br>
        <button type="submit">블로그에 등록하기</button>
    </form>
    <br>
    <a href='/'>[취소]</a>
    """
