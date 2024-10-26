import base64
from functools import wraps
from quart import jsonify, request
from app.config import API_KEY
import secrets


def generate_api_key():
    return secrets.token_hex(24)

def require_api_key(f):
    @wraps(f)
    async def decorated_function(*args, **kwargs):
        api_key = request.headers.get("X-API-KEY")
        if api_key != API_KEY:
            return jsonify({"error": "Unauthorized"}), 401
        return await f(*args, **kwargs)

    return decorated_function





def decode_base64(encoded_str):
    return base64.b64decode(str(encoded_str).encode("utf-8")).decode("utf-8")