from quart import jsonify

from app.util.database import create_user, delete_user, get_user


async def handle_create_user(data, discord_id):
    student_id = data.get("student_id")
    name = data.get("name")

    if not discord_id or not student_id or not name:
        return jsonify({"error": "Invalid input"}), 400

    if await get_user(discord_id):
        return jsonify({"error": "User already exists."}), 409

    await create_user(discord_id, student_id, name)
    return jsonify({"message": "User created successfully."}), 200

async def handle_delete_user(discord_id):
    try:
        r = await delete_user(discord_id)
        if r:
            return jsonify({"message": "User deleted successfully."}), 200
        else:
            return jsonify({"error": "User Not Found"}), 404
    except ConnectionResetError as e:
        return jsonify({"error": f"Connection reset: {e}"}), 500
    except ValueError as ve:
        return jsonify({"error": f"Invalid data: {ve}"}), 400
    
__all__ = ["handle_create_user", "handle_delete_user"]