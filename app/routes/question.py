from quart import jsonify, request
from app.handlers.question_handler import *
from app.util.apivalid import require_api_key


@require_api_key
async def question_methods(action):
    if not request.is_json and request.method != "GET":
        return jsonify({"error": "Request data must be in JSON format"}), 400
    
    data = await request.json
    if action == "create":
        return await handle_create_question(data)
    elif action == "delete":
        return await handle_delete_question(data)
    elif action == "all":
        return await handle_get_all_questions()


__all__ = ["question_methods", "get_question_route"]
