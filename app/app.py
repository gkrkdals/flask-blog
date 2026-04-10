# app.py
from flask import Flask
from flasgger import Swagger
from controllers.post_controller import post_bp
from controllers.login_controller import login_bp

app = Flask(__name__)
swagger = Swagger(app)

app.secret_key = "supersecretkey"
app.register_blueprint(post_bp)
app.register_blueprint(login_bp)

if __name__ == '__main__':
    app.run(debug=True)