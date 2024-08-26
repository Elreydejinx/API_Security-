import jwt
from datetime import datetime, timedelta
from flask import current_app


def encode_token(user_id):
    payload = {
        'user_id': user_id,
        'exp': datetime.utcnow() + timedelta(hours=1)
    }
    return jwt.encode(payload, current_app, algorith='HS256')

def decode_token(token):
    try:
        payload = jwt.decode(token, current_app, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        raise Exception("Token expired. Please log in again.")
    except jwt.InvalidTokenError:
        raise Exception("Invalid token. Please log in again.")
    
