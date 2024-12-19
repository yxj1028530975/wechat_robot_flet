import flet as ft
from wechat_robot.views.signup_view import SignUpView
from wechat_robot.utils.ft_utils import msg_erro
from wechat_robot.utils.config_utils import get_config
from wechat_robot.utils.httpx_handle import HttpxHandle

class SignUpController:
    def __init__(self, page: ft.Page, app):
        self.page = page
        self.app = app
        self.view = SignUpView(page, self)
    
    def on_signup(self, name,  email, phone, password, confirm_password):
        user_data = {
            'name': name,
            'email': email,
            'phone': phone,
            'password': password,
        }
        for val in user_data.values():
            if not val:
                self.error("所有字段都必须填写")
                return
        if password != confirm_password:
            self.error("密码必须相同")
            print("密码必须相同")
            return
        else:
            print("用户注册成功！")
        base_url = get_config("wechat_robot_server", "login_url")
        client = HttpxHandle(base_url=base_url, timeout=2)
        res_data = client.request(
            "POST", "/api/register", json_data=user_data
        )
        if res_data.get("code") == 200:
            print("注册成功")
            self.app.navigate("/")
        else:
            self.error(res_data.get("msg", "注册失败"))
                
    def on_back(self):
        self.app.navigate("/")
        print("你点击了返回")

    def close_error(self, e):
        self.banner.open = False
        self.banner.update()
        print('已进入关闭函数')

    def error(self, text):
        self.banner = msg_erro(text, True)
        # 我在控制器内部创建了这个视图，可能在其他更合适的位置创建更好
        self.banner.actions = [
            ft.TextButton(
                content=ft.Container(
                    content=ft.Column(
                        [
                            ft.Text(
                                value='我明白了',
                                size=10,
                                color=ft.colors.RED,
                            )
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=5,
                    ),
                    padding=ft.padding.all(10),
                ),
                on_click=lambda e: self.close_error(e)
            ),
        ]
        self.view.page.add(self.banner)