import logging
from datetime import datetime
import logging.handlers

def setup_logger(logger_name: str) -> logging.Logger:
    # 建立 logger
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    # 設置格式
    formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] %(name)s: %(message)s", "%Y-%m-%d %H:%M:%S"
    )

    # 設置輪替檔案 handler
    current_date = datetime.now().strftime("%Y-%m-%d")
    file_handler = logging.handlers.RotatingFileHandler(
        filename=f"logs/{current_date}.log",
        maxBytes=32 * 1024 * 1024,  # 檔案大小上限 32MB
        backupCount=5,               # 最多保留 5 個備份檔案
        encoding="utf-8"
    )
    file_handler.setFormatter(formatter)  # 應用格式到檔案 handler
    logger.addHandler(file_handler)       # 加入到 logger

    # 控制台輸出 handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)  # 同樣應用格式
    logger.addHandler(console_handler)       # 加入到 logger

    return logger
