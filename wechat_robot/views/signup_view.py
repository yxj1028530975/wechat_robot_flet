import flet as ft  # type: ignore
from wechat_robot.utils.config_utils import get_config

class SignUpView:
    def __init__(self, page: ft.Page, controller):
        self.controller = controller
        self.page = page
        self.setup_page()
        self.signup_page_ui()

    def setup_page(self):
        self.page.bgcolor = ft.colors.WHITE
        self.page.window.width = 350
        self.page.window.height = 600
        self.page.window.resizable = True
        self.page.window.always_on_top = True
        self.page.title = get_config("wechat_robot","name") + " - 注册"
        # self.page.title = '注册'
        self.page.vertical_alignment = ft.MainAxisAlignment.START
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def signup_page_ui(self):
        self.page.controls.clear()

        # 头像
        ft_img = ft.Image(
            src="img/logo.png",
            width=60,
            height=60,
        )

        # 名称
        ft_name = ft.Text(
            value="智微助手",
            size=20,
            weight=ft.FontWeight.BOLD
        )

        # 注册标题
        lb_cadastro = ft.Text(
            "用户注册",
            size=12,
            color=ft.colors.BLACK,
            weight=ft.FontWeight.BOLD,
        )

        # 用户名输入框
        ft_firstname = ft.TextField(
            height=40,
            text_size=12,
            color=ft.colors.BLACK,
            label="用户名",
            width=300,
        )

        # 邮箱输入框
        ft_email = ft.TextField(
            height=40,
            text_size=12,
            label='邮箱',
            color=ft.colors.BLACK,
            width=300,
        )

        # 手机号码输入框
        ft_telefone = ft.TextField(
            label='手机号码',
            height=40,
            text_size=12,
            color=ft.colors.BLACK,
            width=300,
        )

        # 密码输入框
        ft_password = ft.TextField(
            label='密码',
            height=40,
            text_size=12,
            color=ft.colors.BLACK,
            password=True,
            can_reveal_password=True,
            width=300,
        )

        # 确认密码输入框
        ft_confirmpassword = ft.TextField(
            label='再次输入您的密码',
            height=40,
            text_size=12,
            color=ft.colors.BLACK,
            password=True,
            can_reveal_password=True,
            width=300,
        )

        # 注册按钮
        bt_signup = ft.ElevatedButton(
            "注册",
            on_click=lambda e: self.controller.on_signup(
                ft_firstname.value,
                ft_email.value,
                ft_telefone.value,
                ft_password.value,
                ft_confirmpassword.value
            ),
            width=300,
            height=40
        )

        # 返回登录按钮
        bt_back_to_login = ft.TextButton(
            "返回登录",
            on_click=lambda _: self.controller.on_back(),
        )

        # 顶部容器（头像和名称）
        ft_img_name = ft.Container(
            content=ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[ft_img, ft_name],
                spacing=2,
            ),
            height=150,
            expand=True,
        )

        # 主容器
        main_container = ft.Column(
            controls=[
                ft_img_name,
                lb_cadastro,
                ft_firstname,
                ft_email,
                ft_telefone,
                ft_password,
                ft_confirmpassword,
                bt_signup,
                bt_back_to_login,
            ],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10,
        )

        self.page.add(main_container)
        self.page.update()