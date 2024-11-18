import flet as ft # type: ignore
from wechat_robot.utils.ft_utils import create_app_bar

class SignUpView:
    def __init__(self, page: ft.Page, controller):
        self.controller = controller
        self.page = page
        self.setup_page()
        self.signup_page_ui()
        self.page.add(create_app_bar("注册", self.controller.on_back))


    def setup_page(self):
        self.page.bgcolor = ft.colors.WHITE
        self.page.window.width = 350
        self.page.window.height = 600
        self.page.window.resizable = True
        self.page.window.always_on_top = True
        self.page.title = '注册'
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def signup_page_ui(self):
        self.page.controls.clear() 
        
        lb_cadastro = ft.Text(
        "用户注册",
        size=12,
        color=ft.colors.BLACK,
        weight=ft.FontWeight.BOLD,
        )

        tf_firstname = ft.TextField(
            height=40,
            text_size=12,
            color=ft.colors.BLACK,
            label="用户名",
        )
        tf_email = ft.TextField(
            height=40,
            text_size=12,
            label='邮箱',
            color=ft.colors.BLACK,
        )
        tf_telefone = ft.TextField(
            label='手机号码',
            height=40,
            text_size=12,
            color=ft.colors.BLACK,
        )
        tf_password = ft.TextField(
            label='密码',
            height=40,
            text_size=12,
            color=ft.colors.BLACK,
            password=True,
            can_reveal_password=True
        )
        tf_confirmpassword = ft.TextField(
            label='再次输入您的密码',
            height=40,
            text_size=12,
            color=ft.colors.BLACK,
            password=True,
            can_reveal_password=True
        )

        bt_signup = ft.ElevatedButton(
            "注册",
            on_click=lambda e: self.controller.on_signup(tf_firstname.value,  tf_email.value,
                                              tf_telefone.value, tf_password.value, tf_confirmpassword.value),
            width=120,
            height=40
        )


        self.page.add(
                      lb_cadastro, 
                      tf_firstname, 
                      tf_email, 
                      tf_telefone, 
                      tf_password, 
                      tf_confirmpassword,
                      bt_signup)
        self.page.update()
