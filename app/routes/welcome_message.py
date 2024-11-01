from quart import jsonify
from app.util.logger import setup_logger

logger = setup_logger(__name__)

async def welcome():
    logger.info("Welcome endpoint called")
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