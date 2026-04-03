from flask import Blueprint, render_template

post_bp = Blueprint('post', __name__)

@post_bp.route('/')
@post_bp.route('/home')
def home():
    return render_template('home.html')

@post_bp.route('/post/<int:post_id>')
def post_detail(post_id):
    return render_template('post_detail.html', post_id=post_id)

@post_bp.route('/create')
def create_post():
    from flask import session
    if not session.get("logged_in"):
        return "NOT_AUTHENTICATED", 401
    return render_template('create_post.html')
