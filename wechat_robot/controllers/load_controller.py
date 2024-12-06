import flet as ft
from wechat_robot.views.load_view import LoadView
from wechat_robot.utils.wechat_utils import start_wechat
from wechat_robot.utils.wechat_http_interface import wechat_api
from wechat_robot.models.robot_setting import SettingCRUD
import logging
logger = logging.getLogger(__name__)

class LoadController:
    def __init__(self, page: ft.Page, app):   
        self.page = page
        self.app = app
        self.view = LoadView(page,self)

    def load_start_wechat(self):
        return start_wechat()
    def go_to_main(self):
        self.app.navigate("/main")
        
        
    # 登陆成功，获取个人信息写入数据库
    def get_user_info(self):
        return_data = wechat_api.get_user_info()
        if not return_data:
            return False
        update_data = {
            "wechat_avatar": return_data['data']['avatar_url'],
            "wechat_name": return_data['data']['nick_name'],
            "wechat_wx_id": return_data['data']['wx_id'],
            "wechat_account": return_data['data']['wx_account'],
        }
        SettingCRUD().update_setting(update_data=update_data)

        
    def check_wechat_login_status(self):
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
        try:
            if not (return_data := wechat_api.check_wechat_login_status()):
                logger.error("未能获取到微信登录状态")
                return False
            # 处理响应
            logger.info("登陆中")
            data = return_data.get("data")
            if isinstance(data, dict):
                status = data.get("status")
                if isinstance(status, int):
                    return status == 1
            return False
        except Exception as e:
            return False