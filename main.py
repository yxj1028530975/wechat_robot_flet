import logging
import logging.config
import uvicorn
import flet.fastapi as flet_fastapi
import flet as ft
import threading
from wechat_robot.main import App
from typing import Any,Dict
# # 定义详细的日志配置
# logging_config = {
#     "version": 1,
#     "disable_existing_loggers": False,  # 保留现有日志器
#     "formatters": {
#         "default": {  # 定义 'default' 格式化器
#             "format": "%(asctime)s - %(levelname)s - %(message)s",
#         },
#     },
#     "handlers": {
#         "file": {
#             "class": "logging.FileHandler",
#             "filename": "app.log",
#             "formatter": "default",
#             "encoding": "utf-8",
#         },
#     },
#     "loggers": {
#         "uvicorn": {  # 配置 uvicorn 日志器
#             "handlers": ["file"],
#             "level": "INFO",
#             "propagate": False,
#         },
#         "uvicorn.access": {  # 配置 uvicorn.access 日志器
#             "handlers": ["file"],
#             "level": "INFO",
#             "propagate": False,
#         },
#     },
#     "root": {  # 配置根日志器
#         "level": "INFO",
#         "handlers": ["file"],
#     },
# }

# # 应用日志配置
# logging.config.dictConfig(logging_config)
logger = logging.getLogger(__name__)

# 创建 FastAPI 应用
app = flet_fastapi.FastAPI()

    
@app.post("/msg")
async def rec_msg(item: Dict[str, Any]):
    print(item)
    return {"status": "Message received", "data": item}

# 在后台运行 FastAPI 服务器的函数
def start_api():
    try:
        logger.info("Starting FastAPI server...")
        uvicorn.run(app, host="127.0.0.1", port=9000)
    except Exception as e:
        logger.error(f"Error starting FastAPI: {e}")

def main(page: ft.Page):
    App(page)
    # 您的 Flet 应用代码

if __name__ == "__main__":
    # 创建并启动线程来运行 FastAPI 服务器
    api_thread = threading.Thread(target=start_api, daemon=True)
    api_thread.start()
    
    # 运行 Flet 桌面应用程序
    ft.app(target=main, view=ft.AppView.FLET_APP,assets_dir="assets")