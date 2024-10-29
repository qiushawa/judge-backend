from asyncio.log import logger
from quart import jsonify, request

from app.util.apivalid import require_api_key
from app.util.database import get_question, create_question, get_all_question_id


@require_api_key
async def question_methods(action):
    if not request.is_json and request.method != "GET":
        return jsonify({"error": "Request data must be in JSON format"}), 400
    data = await request.json
    if action == "create":
        await create_question(
            data.get("title"),
            data.get("description"),
            data.get("SampleInput"),
            data.get("SampleOutput"),
            data.get("Input"),
            data.get("Output"),
        )
        return jsonify({"message": "Question created successfully"})
    elif action == "delete":
        # 問題刪除邏輯
        ...
    elif action == "all":
        #  合併 get_all_question_route
        question_list = await get_all_question_id()
        return jsonify({"question_list": question_list}), 200


async def get_question_route():
    question_id = request.args.get("id", None)
    if question_id is not None:
        try:
            question_id = int(question_id)
        except ValueError:
            return jsonify({"error": "Invalid ID format"}), 400
    question = await get_question(question_id)
    if question is None:
        return jsonify({"error": "Question not found."}), 404
    return (
        jsonify(
            {
                "id": question.id,
                "title": question.title,
                "description": question.description,
                "sample_input": question.SampleInput,
                "sample_output": question.SampleOutput,
            }
        ),
        200,
    )


__all__ = ["question_methods", "get_question_route"]
