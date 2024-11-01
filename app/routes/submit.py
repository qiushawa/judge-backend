from quart import jsonify, request
from app.handlers.submit_code_handler import *
from app.util.apivalid import require_api_key
from app.util.database import get_question
from app.config import logger, executors
from app.util.encoders import decode_base64
from importlib import import_module



@require_api_key
async def submit_code():
    question_id, code, language = await get_request_data()
    if not question_id or not code:
        return jsonify({"status": "error", "message": "Invalid input"}), 400

    Input, COutput = await fetch_question(question_id)
    run_code = get_executor(language)
    if not run_code:
        return jsonify({"status": "error", "message": "Invalid language"}), 400

    output, error = await execute_code(run_code, code, Input)
    if error:
        return jsonify({"result": error["type"], "message": error["message"]})
    else:
        result = "Accept" if output == COutput else "Wrong Answer"
        return jsonify({"result": result, "message": output})

__all__ = ["submit_code"]
