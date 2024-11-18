import flet as ft
from wechat_robot.views.load_view import LoadView
from wechat_robot.utils.wechat_utils import start_wechat
from wechat_robot.utils.httpx_handle import HttpxHandle
import logging
logger = logging.getLogger(__name__)

class LoadController:
    def __init__(self, page: ft.Page, app):   
        self.page = page
        self.app = app
        self.view = LoadView(page,self)

    def load_start_wechat(self):
        print("start wechat")
        return start_wechat()
    def go_to_main(self):
        self.app.navigate("/main")
    def check_wechat_login_status(self,port):
        """
        检查微信是否登录成功。

        参数:
            port (int): 启动微信时使用的端口号。

        返回:
            bool: 如果已登录则返回 True，否则返回 False。
        """
        # 实现您的登录状态检查逻辑，例如：
        # 通过请求本地服务器接口，或者检查特定的进程或文件。
        # 这里提供一个示例，实际实现需根据您的项目需求。


        http_client = HttpxHandle(base_url=f"http://127.0.0.1:{port}", timeout=1)

        if response := http_client.request(
            "POST", "/api", json_data={"type": 1}
        ):
            logger.info(f"返回数据： {response}")
            data = response.get("data")
            if isinstance(data, dict):
                status = data.get("status")
                if isinstance(status, int):
                    return status == 1
                else:
                    logger.error(f"响应中的 'status' 类型错误，期待 int 类型，但收到 {type(status)} 类型。")
            else:
                logger.error("响应中的 'data' 字段为空或格式不正确。")
        else:
            logger.error("请求失败或响应为空。")
        return False