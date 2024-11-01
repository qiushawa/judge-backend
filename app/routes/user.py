from quart import jsonify, request
from app.util.apivalid import require_api_key
from app.util.database import get_user, create_user, delete_user
from app.handlers.user_handler import handle_create_user, handle_delete_user

@require_api_key
async def user_methods(action):
    if not request.is_json:
        return jsonify({"error": "Request data must be in JSON format"}), 400
    data = await request.json
    discord_id = data.get("discord_id")
    if action == "create":
        return await handle_create_user(data, discord_id)
    elif action == "delete":
        return await handle_delete_user(discord_id)
    else:
        return jsonify({"error": "Invalid action"}), 400

__all__ = ["user_methods"]
