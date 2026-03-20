from flask import Blueprint, request, session
login_bp = Blueprint('login', __name__)

TEST_ID = 'dev'
TEST_PWD = '12345'

@login_bp.route('/login', methods=['GET', 'POST'])
def login():
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
    session.clear()
    return 'LOGOUT_SUCCESS', 200
