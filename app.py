# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return {"message": "Welcome to the Flask Blog Home!"}

if __name__ == '__main__':
    app.run(debug=True)