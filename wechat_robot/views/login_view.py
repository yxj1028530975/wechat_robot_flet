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
                title=ft.Text(f"微信版本不对，请安装{wechat_version}版本"),
            )
            self.page.open(dlg)
        else:
            self.controller.on_login(user, password)
    
    
    def setup_page(self):
        self.page.controls.clear()
        self.page.window.center()
        self.page.fonts = {
            "alifont": "/fonts/AlibabaPuHuiTi-3-55-Regular.ttf",
        }
        self.page.theme = ft.Theme(
            font_family="alifont",
        )
        self.page.window.icon = "img/robot_icon.ico"
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
        self.page.vertical_alignment = ft.MainAxisAlignment.START
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER  
        # 添加背景图片
        # self.page.bgcolor = ft.colors.WHITE
        # self.page.theme = ft.Theme(color_scheme_seed="bule")
        # self.page.window.resizable = True
        self.page.window.always_on_top = False
        # self.page.window.movable = True
        # self.page.window.bgcolor = ft.Colors.TRANSPARENT
        # self.page.bgcolor = ft.Colors.TRANSPARENT
        # self.page.window.title_bar_hidden = True
        # self.page.window.title_bar_buttons_hidden = False
        # self.page.window.frameless = True
        # self.page.title = get_config("wechat_robot", "name")
        # self.page.window.bgcolor = ft.Colors.BLUE_100
        # # self.page.bgcolor = ft.Colors.TRANSPARENT
        # self.page.window.title_bar_hidden = True
        # self.page.window.frameless = True
        # self.page.window.left = 400
        # self.page.window.top = 200
        # self.page.add(ft.ElevatedButton("I'm a floating button!"))
        
        
        self.page.update()
        
    def login_page_ui(self):
        # 头像
        ft_img = ft.Image(
            src="img/logo.png",
            width=60,
            height=60,
        )
        
        # 名称
        ft_name = ft.Text(value="智微助手", size=20, weight=ft.FontWeight.BOLD)
        
        # 登录标题
        ft_title = ft.Text(
            "用户身份验证",
            size=12,
            color=ft.colors.BLACK,
            weight=ft.FontWeight.BOLD,
        )

        # 用户名输入框
        ft_user = ft.TextField(
            label='用户名',
            hint_text='请输入用户名',
            height=40,
            width=300,
            text_size=12,
            color=ft.colors.BLACK,
            border_color="#8EA5C0",
            # border_width=1,
        )

        # 密码输入框
        ft_password = ft.TextField(
            label='密码',
            hint_text='请输入密码',
            text_size=12,
            height=40,
            width=300,
            color=ft.colors.BLACK,
            border_color="#8EA5C0",
            password=True,
            can_reveal_password=True
        )
        
        # 登录按钮
        ft_bt_login = ft.ElevatedButton(
            "登录",
            on_click=lambda e: self.wechat_version_warning(ft_user.value, ft_password.value),
            width=300,
            height=40,
        )

        # 注册账号按钮
        ft_register = ft.TextButton(
            "注册账号",
            on_click=lambda _: self.controller.on_signup(),
        )

        # 忘记密码按钮
        forgot_password = ft.TextButton(
            "忘记密码？",
            on_click=lambda _: self.controller.on_forgot_password(),
        )

        # 底部按钮行：注册账号、忘记密码
        bottom_button_row = ft.Row(
            controls=[ft_register, forgot_password],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            width=300,
        )
        # 图标和名称
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
                ft_user,
                ft_password,
                ft_bt_login,
                bottom_button_row,
            ],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        )

        self.page.add(main_container)
        self.page.update()
