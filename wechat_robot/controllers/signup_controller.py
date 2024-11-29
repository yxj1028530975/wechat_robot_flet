import flet as ft
from wechat_robot.views.signup_view import SignUpView
from wechat_robot.utils.ft_utils import msg_erro
# from wechat_robot.models.db_manager import DatabaseManager


class SignUpController:
    def __init__(self, page: ft.Page, app):
        self.page = page
        self.app = app
        # self.db_manager = DatabaseManager()
        self.view = SignUpView(page, self)
        
    def add_user(self, first_name, last_name, email, phone, password, confirm_password):
        user_data = {
            'first_name': first_name,
            'last_name': last_name,
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
            # new_user = UserModel(user_data, self.db_manager)
            # try:
            #     new_user.add_userdb()
            #     print("用户注册成功！")
            # except ValueError as e:
            #     self.error(str(e))

        # 想法：创建高级密码检查，创建邮箱确认，为 DDD 创建代码
                
    def on_back(self, event):
        # 导航回到上一个页面
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