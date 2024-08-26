from flask import Flask, request, jsonify
from models import User
from utils.util import encode_token
from werkzeug.security import check_password_hash

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']

    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        token = encode_token(user.id)
        return jsonify({'token':token, 'message': 'Login successful'}), 200
    else:
        return jsonify({'message': 'Invalid credentials'}), 401