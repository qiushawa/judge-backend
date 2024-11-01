from quart import request
from app.util.database import get_question
from app.config import executors
from app.util.encoders import decode_base64
from importlib import import_module


async def get_request_data():
    question_id = request.args.get("id", None)
    data = await request.get_json()
    code = data.get("code")
    language = data.get("language")
    return question_id, code, language

async def fetch_question(question_id):
    question = await get_question(question_id)
    Input = decode_base64(question.Input)
    COutput = decode_base64(question.Output)
    return Input, COutput

def get_executor(language):
    module = executors.get(language)
    if module:
        run_code = import_module(module).run_code
        return run_code
    return None

async def execute_code(run_code, code, Input):
    output, error = run_code(code, Input)
    return output, error

__all__ = ["get_request_data", "fetch_question", "get_executor", "execute_code"]