from quart import jsonify, request
import base64
import os
from app.util.apivalid import require_api_key
from app.executors.cpp_executors import compile_code, extract_first_n_lines, run_exe_with_timeout
from app.util.database import get_question
from app.config import logger
from app.util.encoders import decode_base64
from app.util.errorHandler import error_handler
@require_api_key
@error_handler
async def submit_code():
    question_id = request.args.get("id", None)
    data = await request.get_json()
    code = data.get("code")
    if not question_id or not code:
        return jsonify({"status": "error", "message": "Invalid input"}), 400

    exe_path, compile_message = compile_code(code)
    question = await get_question(question_id)
    Input = decode_base64(question.Input)
    COutput = decode_base64(question.Output)
    logger.info(f"compile-message:{compile_message.stderr}")

    if not os.path.isfile(exe_path):
        error = extract_first_n_lines(compile_message.stderr, 50)
        return jsonify({"result": "Compile Error", "message": error})
    else:
        # 設定 timeout 時間
        output, err = run_exe_with_timeout(exe_path, Input, timeout=5)
        os.remove(exe_path)
        
        if err == "Time Limit Exceeded":
            return jsonify({"result": "Time Limit Exceeded", "message": err})
        elif err:
            return jsonify({"result": "Runtime Error", "message": err})
        else:
            result = "Accept" if output == COutput else "Wrong Answer"
            return jsonify({"result": result, "message": output})
__all__ = ["submit_code"]
