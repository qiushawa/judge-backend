from quart import jsonify, request
from app.util.database import *

async def handle_create_question(data):
    await create_question(
        data.get("title"),
        data.get("description"),
        data.get("SampleInput"),
        data.get("SampleOutput"),
        data.get("Input"),
        data.get("Output"),
    )
    return jsonify({"message": "Question created successfully"})

async def handle_get_all_questions():
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
    
    return jsonify({
        "id": question.id,
        "title": question.title,
        "description": question.description,
        "sample_input": question.SampleInput,
        "sample_output": question.SampleOutput,
    }), 200

async def handle_delete_question(data):
    question_id = data.get("id")
    if question_id is None:
        return jsonify({"error": "Invalid ID format"}), 400
    question = await get_question(question_id)
    if question is None:
        return jsonify({"error": "Question not found."}), 404
    await delete_question(question_id)
    return jsonify({"message": "Question deleted successfully."}), 200
__all__ = ["handle_create_question", "handle_get_all_questions", "get_question_route", "handle_delete_question"]