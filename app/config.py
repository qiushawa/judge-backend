import logging
import logging.handlers


logger = logging.getLogger("judge")
logger.setLevel(logging.DEBUG)

handler = logging.handlers.RotatingFileHandler(
    filename="logs/judge.log",
    encoding="utf-8",
    maxBytes=32 * 1024 * 1024,
    backupCount=5,
)
dt_fmt = "%Y-%m-%d %H:%M:%S"
formatter = logging.Formatter(
    "[{asctime}] [{levelname:<8}] {name}: {message}", dt_fmt, style="{"
)
handler.setFormatter(formatter)
logger.addHandler(handler)

PORT = 5000
HOST = "0.0.0.0"
API_KEY = "A21WFJHNJREGG8784WDMKM"


DATABASE_PATH = "app/database/database.db"

ALLOW_ORIGIN = "http://localhost:8080", # 允許的來源

    
