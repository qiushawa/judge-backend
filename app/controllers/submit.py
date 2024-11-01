from asyncio.log import logger
from quart import jsonify
from app.handlers.submit_code_handler import *
from app.util.apivalid import require_api_key
from app.util.logger import setup_logger

logger = setup_logger(__name__)

@require_api_key
async def submit_code():
    logger.info("Received a request to submit code")
    question_id, code, language = await get_request_data()
    logger.debug(f"Request data - question_id: {question_id}, language: {language}")

    if not question_id or not code:
        logger.error("Invalid input: question_id or code is missing")
        return jsonify({"status": "error", "message": "Invalid input"}), 400
    
    logger.info(f"Fetching question with id: {question_id}")
    Input, COutput = await fetch_question(question_id)
    logger.debug(f"Fetched question - Input: {Input}, Expected Output: {COutput}")

    logger.info(f"Getting executor for language: {language}")
    run_code = get_executor(language)
    if not run_code:
        logger.error("Invalid language")
        return jsonify({"status": "error", "message": "Invalid language"}), 400

    logger.info("Executing code")
    output, error = await execute_code(run_code, code, Input)
    if error:
        logger.error(f"Code execution error: {error['message']}")
        return jsonify({"result": error["type"], "message": error["message"]})
    else:
        logger.info("Code executed successfully")
        logger.debug(f"Execution output: {output}")
        result = "Accept" if output == COutput else "Wrong Answer"
        logger.info(f"Result: {result}")
        return jsonify({"result": result, "message": output})

__all__ = ["submit_code"]
