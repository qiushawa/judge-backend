from app.controllers.user import user_methods
from app.controllers.welcome_message import welcome
from app.controllers.question import question_methods, get_question_route
from app.controllers.submit import submit_code
from quart import Quart, request
from app.util.logger import setup_logger

logger = setup_logger(__name__)

def log_request():
    logger.info(f"Request: {request.method} {request.path}")

def setup_routes(app: Quart):
    app.before_request(log_request)
    app.add_url_rule("/", methods=["GET"], view_func=welcome)
    app.add_url_rule("/api/user/<action>", methods=["POST", "GET"], view_func=user_methods)
    app.add_url_rule("/api/question/<action>", methods=["POST", "GET"], view_func=question_methods)
    app.add_url_rule("/api/question", methods=["GET"], view_func=get_question_route)
    app.add_url_rule("/api/submit", methods=["POST"], view_func=submit_code)
