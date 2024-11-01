import base64

def decode_base64(encoded_str):
    """將Base64編碼的字串解碼"""
    return base64.b64decode(str(encoded_str).encode("utf-8")).decode("utf-8")

def encode_base64(decoded_str):
    """將字串編碼為Base64"""
    return base64.b64encode(str(decoded_str).encode("utf-8")).decode("utf-8")