import flet as ft
from wechat_robot.utils.ft_utils import setup_base_page


class MainView:
    def __init__(self, page: ft.Page, controller):
        self.page = page
        self.controller = controller
        self.selected_index = 0
        self.content = ft.Container()
        setup_base_page(self)

    def build(self):
        # 导航栏
        rail = ft.NavigationRail(
            selected_index=self.selected_index,
            label_type=ft.NavigationRailLabelType.ALL,
            min_width=200,
            min_extended_width=400,
            group_alignment=-0.9,
            destinations=[
                ft.NavigationRailDestination(icon=ft.icons.GROUP, label="群组列表"),
                ft.NavigationRailDestination(icon=ft.icons.PERSON, label="好友列表"),
                ft.NavigationRailDestination(icon=ft.icons.PUBLIC, label="公众号"),
                ft.NavigationRailDestination(icon=ft.icons.SETTINGS, label="全局设置"),
                ft.NavigationRailDestination(icon=ft.icons.APPS, label="应用插件"),
            ],
            height=400,
            width=200,
            on_change=self.on_navigation_change,
            expand=True,
            bgcolor=ft.colors.WHITE,
        )
        
        # 主布局
        return ft.Row(
            [
                ft.Column(
                    alignment=ft.MainAxisAlignment.START,
                    controls=[ self.show_account_name(),rail],
                ),
                # ft.VerticalDivider(width=1),
                self.content,  # 确保 self.content 被添加到布局中
            ],
            expand=True,
            # width=200,height=720
        )

    # 应用图片和名称
    def show_logo_name(self):
        ft_img = ft.Image(
            src="img/logo.png",
            width=60,
            height=60,
            # border_radius=ft.border_radius.all(50),
        )
        ft_name = ft.Text(value="智微助手", size=20,weight=ft.FontWeight.BOLD)
        return ft.Container(
            alignment=ft.alignment.bottom_center,
            width=200,
            height=60,
            content=ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                # horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[ft_img, ft_name],
                spacing=2,
            ),
            padding=ft.padding.only(bottom=10),
        )
    def show_account_name(self):
        ft_img = ft.Image(
            src=self.controller.avatar_url,
            width=50,
            height=50,
            border_radius=ft.border_radius.all(50),
            badge=ft.Badge(small_size=10, text="智微"),
        )
        ft_name = ft.Text(self.controller.nick_name, size=15)
        return ft.Container(
            alignment=ft.alignment.bottom_center,
            width=200,
            height=100,
            content=ft.Column(
                alignment=ft.MainAxisAlignment.END,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[ft_img, ft_name],
                spacing=2,
            ),
            padding=ft.padding.only(bottom=10),
        )

    def on_navigation_change(self, e):
        old_index = self.selected_index
        self.selected_index = e.control.selected_index
        self.controller.switch_navigation_rail(old_index, self.selected_index)

    def update_content(self, new_content):
        self.content.content = new_content
        if self.content.page:
            self.content.update()
