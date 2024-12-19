import flet as ft
from wechat_robot.views.login_view import LoginView
from wechat_robot.utils.config_utils import get_config
from wechat_robot.utils.httpx_handle import HttpxHandle


class LoginController:
    def __init__(self, page: ft.Page, app):
        self.page = page
        self.app = app
        self.view = LoginView(page, self)

    def on_login(self, username, password):
        base_url = get_config("wechat_robot_server", "login_url")
        client = HttpxHandle(base_url=base_url, timeout=2)
        res_data = client.request(
            "POST", "/api/login", json_data={"identifier": username, "password": password}
        )
        if res_data.get("code") == 200:
            print("登录成功")
            self.app.navigate("/load")

    def on_signup(self):
        self.app.navigate("/signup")

    def on_back(self, event):
        self.app.navigate()
