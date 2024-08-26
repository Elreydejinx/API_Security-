from functools import wraps
from flask import request, jsonify
from utils.util import decode_token
from models import User


def role_required(required_role):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            token = request.headers.get('Authorization')
            if not token:
                return jsonify({'message': 'Token is missing'}), 401
            
            try:
                payload = decode_token(token)
                user_role = User.query.filter_by(id=payload['user_id']).first().role
                if user_role != required_role:
                    return jsonify({'message': 'Unauthorized'}), 403
            except Exception as e:
                return jsonify({'message': str(e)}), 401
            
            return f(*args,**kwargs)
        return wrapper
    return decorator