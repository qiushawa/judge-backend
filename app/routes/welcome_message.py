from quart import jsonify

async def welcome():
    return jsonify({
        "status": "success",
        "message": "api server is running",
        "help": {
            "user": {
                "create": "/api/user/create",
                "delete": "/api/user/delete"
            },
            "question": {
                "create": "/api/question/create",
                "delete": "/api/question/delete",
                "all": "/api/question/all"
            },
            "submit": "/api/submit"
        }
    })
__all__ = [
    "welcome"
]