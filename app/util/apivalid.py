from functools import wraps
from quart import jsonify, request
from app.config import API_KEY
import secrets
from app.util.logger import setup_logger

logger = setup_logger(__name__)


def generate_api_key():
    return secrets.token_hex(24)

def require_api_key(f):
    @wraps(f)
    async def decorated_function(*args, **kwargs):
        api_key = request.headers.get("X-API-KEY")
        if api_key != API_KEY:
            # 記錄請求來源 IP 和失敗訊息
            client_ip = request.remote_addr
            logger.error(f"Unauthorized request from IP: {client_ip}")
            return jsonify({"error": "Unauthorized"}), 401
        return await f(*args, **kwargs)
    return decorated_function