from quart import Quart
import asyncio
from quart_cors import cors
from app.routes import setup_routes
from app.util.database import create_tables
from app.config import ALLOW_ORIGIN, HOST, PORT
from app.util.logger import setup_logger

logger = setup_logger(__name__)
app = Quart(__name__)
app = cors(app, allow_origin=ALLOW_ORIGIN)
setup_routes(app)
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
