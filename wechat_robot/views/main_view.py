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
            min_width=100,
            min_extended_width=400,
            group_alignment=-0.9,
            destinations=[
                ft.NavigationRailDestination(icon=ft.icons.GROUP, label="群列表"),
                ft.NavigationRailDestination(icon=ft.icons.PERSON, label="好友列表"),
                ft.NavigationRailDestination(icon=ft.icons.PUBLIC, label="公众号"),
                ft.NavigationRailDestination(icon=ft.icons.SETTINGS, label="全局设置"),
                ft.NavigationRailDestination(icon=ft.icons.APPS, label="应用插件"),
            ],
            height=500,
            width=130,
            on_change=self.on_navigation_change,
            expand=True,
        )
        
        # 主布局
        return ft.Row(
            [
                ft.Column(
                    alignment=ft.MainAxisAlignment.END,
                    controls=[rail, self.show_logo_name()],
                ),
                # rail,
                ft.VerticalDivider(width=1),
                self.content,  # 确保 self.content 被添加到布局中
            ],
            expand=True,
        )

    def show_logo_name(self):
        ft_img = ft.Image(
            src=self.controller.avatar_url,
            width=50,
            height=50,
            border_radius=ft.border_radius.all(50),
        )
        #
        bag = ft.Badge(content=ft_img, text="智微")

        left_bottom_user = ft.Container(
            alignment=ft.alignment.bottom_center,
            width=130,
            height=200,
            content=ft.Column(
                alignment=ft.MainAxisAlignment.END,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[bag, ft.Text(self.controller.nick_name, size=15)],
                spacing=2,
            ),
            # bgcolor=ft.colors.BLUE
            # 向上偏移10
            padding=ft.padding.only(bottom=10),
        )
        return left_bottom_user

    def on_navigation_change(self, e):
        old_index = self.selected_index
        self.selected_index = e.control.selected_index
        self.controller.switch_navigation_rail(old_index, self.selected_index)

    def update_content(self, new_content):
        self.content.content = new_content
        if self.content.page:
            self.content.update()
