import logging
import logging.handlers
from datetime import datetime
from app.util.logger import logger

PORT = 5000
HOST = "0.0.0.0"
API_KEY = "A21WFJHNJREGG8784WDMKM"
DATABASE_PATH = "app/database/database.db"
ALLOW_ORIGIN = "http://localhost:8080"
logger.info(f"start server on {HOST}:{PORT}")
EXECUTOR_TIMEOUT = 5

executors = {
    "python": "app.executors.python_executors",
    "cpp": "app.executors.cpp_executors",
    "c": "app.executors.c_executors",
}
