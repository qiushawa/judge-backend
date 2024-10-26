from quart import jsonify, request
from functools import wraps

from app.util.apiUtil import require_api_key
from app.util.database import get_user, create_user, delete_user
from app.config import API_KEY
from app.util.errorHandler import error_handler, handle_error_status


@require_api_key
@error_handler
async def user_methods(action):
    if not request.is_json:
        return handle_error_status(400)

    data = await request.json
    discord_id = data.get("discord_id")

    # ---------------------------------------------------
    #                   Create User                    #
    # ---------------------------------------------------

    if action == "create":
        student_id = data.get("student_id")
        name = data.get("name")

        if not discord_id or not student_id or not name:
            return handle_error_status(400)  # 缺少必要欄位

        if await get_user(discord_id):
            return handle_error_status(409)  # 用戶已存在

        await create_user(discord_id, student_id, name)
        return jsonify({"message": "User created successfully."}), 200

    # ---------------------------------------------------
    #                   Delete User                    #
    # ---------------------------------------------------

    elif action == "delete":
        try:
            r = await delete_user(discord_id)
            if r:
                return jsonify({"message": "User deleted successfully."}), 200
            else:
                return jsonify({"error": f"User Not Found"}), 404
        except ConnectionResetError as e:
            return jsonify({"error": f"Connection reset: {e}"}), 500
        except ValueError as ve:
            return jsonify({"error": f"Invalid data: {ve}"}), 400


__all__ = ["user_methods"]
