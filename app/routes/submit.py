from quart import jsonify, request
from app.util.apivalid import require_api_key
from app.util.database import get_question
from app.config import logger, executors
from app.util.encoders import decode_base64

@require_api_key
async def submit_code():
    question_id = request.args.get("id", None)
    data = await request.get_json()
    code = data.get("code")
    language = data.get("language")
    if not question_id or not code:
        return jsonify({"status": "error", "message": "Invalid input"}), 400
    question = await get_question(question_id)
    Input = decode_base64(question.Input)
    COutput = decode_base64(question.Output)
    module = executors.get(language)
    if module:
        from importlib import import_module
        run_code = import_module(module).run_code
    else:
        return jsonify({"status": "error", "message": "Invalid language"}), 400

    output, error = run_code(code, Input)
    if error:
        return jsonify({"result": error["type"], "message": error["message"]})
    else:
        result = "Accept" if output == COutput else "Wrong Answer"
        return jsonify({"result": result, "message": output})
__all__ = ["submit_code"]
