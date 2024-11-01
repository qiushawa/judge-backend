from quart import jsonify, request
from app.handlers.question_handler import *
from app.util.apivalid import require_api_key
from app.util.logger import setup_logger

logger = setup_logger(__name__)

@require_api_key
async def question_methods(action):
    logger.info(f"Entered question_methods with action: {action}")
    try:
        if not request.is_json and request.method != "GET":
            logger.error("Request data must be in JSON format")
            return jsonify({"error": "Request data must be in JSON format"}), 400
        logger.info(f"Request method: {request.method}")
        data = await request.json
        if action == "create":
            logger.info("Creating question")
            response = await handle_create_question(data)
        elif action == "delete":
            logger.info("Deleting question")
            response = await handle_delete_question(data)
        elif action == "all":
            logger.info("Getting all questions")
            response = await handle_get_all_questions()
        else:
            logger.error(f"Invalid action: {action}")
            return jsonify({"error": "Invalid action"}), 400
        logger.info(f"Action {action} completed successfully")
        return response
    except Exception as e:
        logger.exception(f"An error occurred in question_methods: {e}")
        return jsonify({"error": "An internal error occurred"}), 500
    finally:
        logger.info(f"Exiting question_methods with action: {action}")

__all__ = ["question_methods", "get_question_route"]
