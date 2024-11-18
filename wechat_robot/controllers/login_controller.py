import flet as ft
from wechat_robot.views.login_view import LoginView


class LoginController:
    def __init__(self, page: ft.Page, app):   
        self.page = page
        self.app = app
        self.view = LoginView(page, self)

    def on_login(self, username, password):
        print(username, password)
        if username == "" or password == "":
            print("请输入账号或密码")
        elif username == "1" and password == "1":
            print("登录成功")
            self.app.navigate("/load")
        else:
            print("登录失败")
       
    def on_signup(self):
        self.app.navigate("/signup")

    def on_back(self, event):
        self.app.navigate()