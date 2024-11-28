import flet as ft
from wechat_robot.utils.ft_utils import setup_base_page
from wechat_robot.utils.config_utils import get_config
import threading
import time

class LoadView:
    def __init__(self, page: ft.Page,controller):
        self.controller = controller
        self.page = page
        setup_base_page(self)
        self.setup_page()
        self.load_page_ui()
        # self.app_bar = nav_app_bar("主页")
        # print(create_app_bar("Login", on_back))
        # self.page.add(self.app_bar)
        # 启动后台线程监听登录状态
        self.port = get_config("wechat","port")
        self.check_login_thread = threading.Thread(target=self.check_login_status)
        self.check_login_thread.start()

    
    def check_login_status(self):
        """
        后台检查微信登录状态，登录成功后跳转到主页面。
        """
        while True:
            if login_success := self.controller.check_wechat_login_status(self.port):
                # 切换到主页面，需要在主线程中执行
                self.controller.get_user_info()
                self.controller.go_to_main()
                # 使用 page 的函数在主线程中执行页面更新
                # self.page.invoke(navigate_to_main)
                break
            print("等待登录中...")
            time.sleep(1)  # 每秒检查一次登录状态
            
    def setup_page(self):
        ...

    def load_page_ui(self):
        background = ft.Container(
            width=self.page.window.width,
            height=self.page.window.height,
            content=ft.Stack(
                [
                    ft.Image(
                        src="img/background.jpg",  # 背景图片路径
                        width=self.page.window.width,
                        height=self.page.window.height,
                        fit=ft.ImageFit.COVER,
                    ),
                    ft.Column(
                        [
                            ft.Text("正在加载中...", size=24, color=ft.colors.WHITE),
                            # 增加一个按钮测试
                            ft.CupertinoButton(
                                content=ft.Text("启动微信", color=ft.colors.YELLOW),
                                bgcolor=ft.colors.PRIMARY,
                                alignment=ft.alignment.top_left,
                                border_radius=ft.border_radius.all(15),
                                opacity_on_click=0.5,
                                on_click=lambda e: self.controller.load_start_wechat(),
                            ),

                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                ],alignment=ft.alignment.center, 
            ),
        )
        self.page.add(background)
        self.page.update()
