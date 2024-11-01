from quart import jsonify, request
from app.util.apivalid import require_api_key
from app.handlers.user_handler import handle_create_user, handle_delete_user
from app.util.logger import setup_logger

logger = setup_logger(__name__)

@require_api_key
async def user_methods(action):
    logger.info(f"Received request for action: {action}")
    
    if not request.is_json:
        logger.error("Request data is not in JSON format")
        return jsonify({"error": "Request data must be in JSON format"}), 400
    
    data = await request.json
    discord_id = data.get("discord_id")
    logger.info(f"Request data: {data}")
    
    if action == "create":
        result = await handle_create_user(data, discord_id)
        logger.info(f"User created with discord_id: {discord_id}")
        return result
    elif action == "delete":
        result = await handle_delete_user(discord_id)
        logger.info(f"User deleted with discord_id: {discord_id}")
        return result
    else:
        logger.error("Invalid action")
        return jsonify({"error": "Invalid action"}), 400

__all__ = ["user_methods"]
