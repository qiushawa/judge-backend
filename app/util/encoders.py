import base64
import bcrypt

def decode_base64(encoded_str):
    """將Base64編碼的字串解碼"""
    return base64.b64decode(str(encoded_str).encode("utf-8")).decode("utf-8")


def encode_base64(decoded_str):
    """將字串編碼為Base64"""
    return base64.b64encode(str(decoded_str).encode("utf-8")).decode("utf-8")


def hash_bcrypt(data):
    """使用 bcrypt 生成帶鹽值的哈希值"""
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(data.encode("utf-8"), salt)
    return hashed

def verify_bcrypt(data, hashed):
    """驗證 bcrypt 哈希值"""
    return bcrypt.checkpw(data.encode("utf-8"), hashed)
