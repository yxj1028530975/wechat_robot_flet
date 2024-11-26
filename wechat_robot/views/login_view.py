import flet as ft 
from wechat_robot.utils.config_utils import get_config
from wechat_robot.utils.wechat_utils import get_current_wechat_version
class LoginView:
    def __init__(self, page: ft.Page, controller):
        self.controller = controller
        self.page = page
        self.setup_page()
        self.login_page_ui()

    def wechat_version_warning(self,user,password):
        wechat_version = get_config('wechat','version')
        current_wechat_version = get_current_wechat_version()
        if wechat_version != current_wechat_version:
            dlg = ft.AlertDialog(
                title=ft.Text("Hi, this is a non-modal dialog!"),
            )
            self.page.open(dlg)
        else:
            self.controller.on_login(user, password)
    
    
    def setup_page(self):
        self.page.controls.clear()
        self.page.window.center()
        self.page.bgcolor = ft.colors.WHITE
        self.page.window.width = 350
        self.page.window.height = 600
        # self.page.window.left = 1000  # 窗口左边距
        # self.page.window.top = 500    # 窗口上边距
        self.page.window.resizable = False
        # self.page.window.center()
        # self.page.window.icon = "wechat.ico"
        # self.page.window.always_on_top = True
        self.page.title = get_config("wechat_robot","name")
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER  
        # 添加背景图片
        # self.page.bgcolor = ft.colors.WHITE
        # self.page.theme = ft.Theme(color_scheme_seed="bule")
        self.page.update()
        
    def login_page_ui(self):
        lb_login = ft.Text(
            "用户身份验证",
            size=12,
            color=ft.colors.BLACK,
            weight=ft.FontWeight.BOLD,
        )

        tf_user = ft.TextField(
            label='用户名',
            hint_text='用户名',
            height=40,
            width=400,
            text_size=12,
            color=ft.colors.BLACK,
        )

        tf_password = ft.TextField(
            label='密码',
            hint_text='密码',
            text_size=12,
            height=40,
            width=400,
            color=ft.colors.BLACK,
            password=True,
            can_reveal_password=True
        )

        bt_login = ft.ElevatedButton(
            "登陆",
            on_click=lambda e: self.wechat_version_warning(tf_user.value, tf_password.value),
            width=100,
            height=40,
        )

        bt_criar = ft.TextButton(
            "注册",
            on_click=lambda _: self.controller.on_signup(),
            width=120,
            height=40
        )

        self.page.add(lb_login, tf_user, tf_password, bt_login, bt_criar)
        self.page.update()
