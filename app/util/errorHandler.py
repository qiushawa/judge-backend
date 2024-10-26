from functools import wraps
from quart import jsonify


def handle_error_status(error_code, error_message=None):
    if error_code == 400:
        return jsonify({"error": "Missing required fields"}), 400
    elif error_code == 403:
        return jsonify({"error": "Permission denied"}), 403
    elif error_code == 409:
        return jsonify({"error": "User already exists"}), 409
    elif error_code == 422:
        return jsonify({"error": "Invalid data structure, missing keys"}), 422
    elif error_code == 500:
        return jsonify({"error": f"An error occurred: {error_message}"}), 500
    elif error_code == 504:
        return jsonify({"error": "Request timed out"}), 504
    elif error_code == 501:
        return jsonify({"error": "Not implemented"}), 501
    else:
        return (
            jsonify({"error": f"Unknown error occurred: {error_message}"}),
            error_code,
        )


def error_handler(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except ConnectionResetError as e:
            return handle_error_status(500, f"Connection reset: {e}")
        except ValueError as ve:
            return handle_error_status(400, f"Invalid data: {ve}")
        except TimeoutError:
            return handle_error_status(504)
        except PermissionError:
            return handle_error_status(403)
        except NotImplementedError:
            return handle_error_status(501)
        except KeyError:
            return handle_error_status(422)
        except Exception as e:
            return handle_error_status(500, f"An error occurred: {e}")

    return wrapper