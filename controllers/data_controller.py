from flask import Flask, jsonify, request
from decorators.role_required import role_required

app = Flask(__name__)

@app.route('/create-data', methods=['POST'])
@role_required('admin')
def create_data():
    return jsonify({'message': 'Data created successfully'}), 201

@app.route('/view-data', methods=['GET'])
@role_required('user')
def view_data():
    return jsonify({'message': 'Data retrived successfully'}), 200