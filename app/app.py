from quart import Quart
from quart_cors import cors
from app.routes.question import *
from app.routes.submit import *
from app.routes.user import *
from app.routes.welcome_message import *
from app.util.database import create_tables
from app.config import ALLOW_ORIGIN, HOST, PORT

app = Quart(__name__)
app = cors(app, allow_origin='*')

# app = cors(app, allow_origin=ALLOW_ORIGIN)


# --------------------------------------------------
# 後端 API 路由
# --------------------------------------------------

app.add_url_rule("/api/user/<action>", methods=["POST", "GET"], view_func=user_methods)
app.add_url_rule("/api/question/<action>", methods=["POST", "GET"], view_func=question_methods)
app.add_url_rule("/api/question", methods=["GET"], view_func=get_question_route)
app.add_url_rule("/api/submit", methods=["POST"], view_func=submit_code)


# --------------------------------------------------
# 初始化資料表
# --------------------------------------------------
@app.before_serving
async def initialize():
    await create_tables()


# --------------------------------------------------
# 啟動伺服器
# --------------------------------------------------
async def start_server():
    await app.run_task(host=HOST, port=PORT, debug=True)
