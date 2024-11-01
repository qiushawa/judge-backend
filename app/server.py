from quart import Quart
import asyncio
from quart_cors import cors
from app.routes.question import question_methods, get_question_route
from app.routes.submit import submit_code
from app.routes.user import user_methods
from app.routes.welcome_message import welcome
from app.util.database import create_tables
from app.config import ALLOW_ORIGIN, HOST, PORT
from app.util.logger import setup_logger

logger = setup_logger(__name__)
app = Quart(__name__)
app = cors(app, allow_origin=ALLOW_ORIGIN)

# --------------------------------------------------
# 後端 API 路由
# --------------------------------------------------
logger.info("Setting up routes")
app.add_url_rule("/", methods=["GET"], view_func=welcome)
app.add_url_rule("/api/user/<action>", methods=["POST", "GET"], view_func=user_methods)
app.add_url_rule("/api/question/<action>", methods=["POST", "GET"], view_func=question_methods)
app.add_url_rule("/api/question", methods=["GET"], view_func=get_question_route)
app.add_url_rule("/api/submit", methods=["POST"], view_func=submit_code)

# --------------------------------------------------
# 初始化資料表
# --------------------------------------------------
@app.before_serving
async def initialize():
    logger.info("Initializing database tables")
    await create_tables()

# --------------------------------------------------
# 啟動伺服器
# --------------------------------------------------
async def start_server():
    logger.info(f"Starting server on {HOST}:{PORT}")
    await app.run_task(host=HOST, port=PORT)

if __name__ == "__main__":
    logger.info("Running main application")
    asyncio.run(start_server())
