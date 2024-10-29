import logging
import logging.handlers
from datetime import datetime

logger = logging.getLogger("judge")
logger.setLevel(logging.DEBUG)
file_handler = logging.handlers.RotatingFileHandler(
    filename=f"logs/{datetime.now().strftime('%Y.%m.%d')}.log",
    encoding="utf-8",
    maxBytes=32 * 1024 * 1024,
    backupCount=5,
)
console_handler = logging.StreamHandler()
dt_fmt = "%Y-%m-%d %H:%M:%S"
formatter = logging.Formatter(
    "[{asctime}] [{levelname:<8}] {name}: {message}", dt_fmt, style="{"
)
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(console_handler)
PORT = 5000
HOST = "0.0.0.0"
API_KEY = "A21WFJHNJREGG8784WDMKM"
DATABASE_PATH = "app/database/database.db"
ALLOW_ORIGIN = ("http://localhost:8080",)  # 允許的來源
logger.info(f"start server on {HOST}:{PORT}")
