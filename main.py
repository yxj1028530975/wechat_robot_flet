import logging
import logging.config
import threading
import os
import flet as ft
from wechat_robot.main import App
from wechat_robot.fastapi.fastapi_server import start_api  # 导入新文件中的 start_api 函数



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
# logging.config.dictConfig(logging_config)
logger = logging.getLogger(__name__)

def main(page: ft.Page):
    App(page)
    # 您的 Flet 应用代码

if __name__ == "__main__":
    # 创建并启动线程来运行 FastAPI 服务器
    api_thread = threading.Thread(target=start_api, daemon=True)
    logger.info("启动 FastAPI 服务器")
    api_thread.start()
    
    # 运行 Flet 桌面应用程序
    ft.app(target=main, view=ft.AppView.FLET_APP_HIDDEN,assets_dir="assets")