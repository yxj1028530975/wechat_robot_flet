# 文件路径: /d:/gr_project/wechat_robot_flet/fastapi_server.py

import logging
import logging.config
import os
import threading
import uvicorn
import flet.fastapi as flet_fastapi
import flet as ft
from typing import Any,Dict
from wechat_robot.fastapi.wechat_msg import wechat_msg_handle  # 导入新文件中的 start_api 函数

# 定义 data 目录的路径
data_dir = os.path.join(os.path.abspath("."), "data")

# 如果 data 目录不存在，则创建
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

# 定义日志文件的路径
log_file_path = os.path.join(data_dir, "app.log")

# 定义详细的日志配置
logging_config = {
    "version": 1,
    "disable_existing_loggers": False,  # 保留现有日志器
    "formatters": {
        "default": {  # 定义 'default' 格式化器
            "format": "%(asctime)s - %(levelname)s - %(message)s",
        },
    },
    "handlers": {
        "file": {
            "class": "logging.FileHandler",
            "filename": log_file_path,
            "formatter": "default",
            "encoding": "utf-8",
        },
    },
    "loggers": {
        "uvicorn": {  # 配置 uvicorn 日志器
            "handlers": ["file"],
            "level": "INFO",
            "propagate": False,
        },
        "uvicorn.access": {  # 配置 uvicorn.access 日志器
            "handlers": ["file"],
            "level": "INFO",
            "propagate": False,
        },
    },
    "root": {  # 配置根日志器
        "level": "INFO",
        "handlers": ["file"],
    },
}

# # 应用日志配置
logging.config.dictConfig(logging_config)
logger = logging.getLogger(__name__)
# 创建 FastAPI 应用
app = flet_fastapi.FastAPI()

@app.post("/msg")
async def rec_msg(data: Dict[str, Any]):
    # 处理接收到的消息
    logger.info(f"收到消息: {data}")
    wechat_msg_handle(data)

# 在后台运行 FastAPI 服务器的函数
def start_api():
    try:
        logger.info("Starting FastAPI server...")
        uvicorn.run(app, host="127.0.0.1", port=9000,log_config=logging_config)
    except Exception as e:
        logger.error(f"Error starting FastAPI: {e}")