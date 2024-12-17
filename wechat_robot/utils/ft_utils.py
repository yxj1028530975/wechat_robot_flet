import flet as ft
from wechat_robot.utils.config_utils import get_config      
def create_app_bar(title: str, go_back: callable = None) -> ft.AppBar:
    bt_back = ft.IconButton(
        icon=ft.icons.ARROW_BACK, on_click=go_back, width=120, height=50
    )
    return ft.AppBar(title=ft.Text(title), leading=bt_back)

def setup_base_page(self):
    
    self.page.fonts = {
            "alifont": "/fonts/AlibabaPuHuiTi-3-55-Regular.ttf",
        }
    self.page.theme = ft.Theme(
        font_family="alifont",
    )
    # self.page.window.title_bar_hidden = True
    self.page.controls.clear()
    self.page.window.icon = "img/robot_icon.ico"
    self.page.bgcolor = ft.colors.WHITE
    self.page.window.width = get_config("wechat_robot","main_height")
    self.page.window.height = get_config("wechat_robot","main_width")
    self.page.padding = 0
    # self.page.window.resizable = False
    # self.page.window.always_on_top = False
    # self.page.window.movable = True
    # self.page.window.bgcolor = ft.Colors.TRANSPARENT
    # self.page.bgcolor = ft.Colors.TRANSPARENT
    # self.page.window.title_bar_hidden = True
    # self.page.window.title_bar_buttons_hidden = True
    # self.page.window.frameless = True
    self.page.title = get_config("wechat_robot", "name")
    # self.page.window.bgcolor = ft.Colors.BLUE_100
    # # self.page.bgcolor = ft.Colors.TRANSPARENT
    # self.page.window.title_bar_hidden = True
    # self.page.window.frameless = True
    # self.page.window.left = 400
    # self.page.window.top = 200
    # self.page.add(ft.ElevatedButton("I'm a floating button!"))
def nav_app_bar(title: str) -> ft.AppBar:
    return ft.AppBar(
        leading=ft.Icon(ft.icons.PALETTE),
        leading_width=40,
        title=ft.Text(title),
        center_title=False,
        bgcolor=ft.colors.SURFACE_VARIANT,
        actions=[
            ft.IconButton(ft.icons.WB_SUNNY_OUTLINED),
            # ft.IconButton(ft.icons.FILTER_3),
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="Item 1"),
                    # ft.PopupMenuItem(),  # divider
                    ft.PopupMenuItem(
                        text="Checked item",
                        checked=False,
                        on_click=lambda e: print("Checked item clicked!"),
                    ),
                ]
            ),
        ],
    )


def msg_erro(msg: str, open: bool = True) -> ft.Banner:
    banner = ft.Banner(
        open=open,
        bgcolor=ft.colors.AMBER_100,
        leading=ft.Icon(ft.icons.DANGEROUS_SHARP, color=ft.colors.RED_400, size=40),
        content=ft.Text(msg, color=ft.colors.BLACK, size=10),
    )
    return banner


