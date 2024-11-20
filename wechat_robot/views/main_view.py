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
                ft.NavigationRailDestination(icon=ft.icons.PERSON, label="公众号"),
                ft.NavigationRailDestination(icon=ft.icons.PERSON, label="全局管理"),
                ft.NavigationRailDestination(icon=ft.icons.PERSON, label="高级功能"),
                ft.NavigationRailDestination(icon=ft.icons.PERSON, label="应用插件"),
                # 更多导航项...
            ],
            on_change=self.on_navigation_change,
        )
        # 主布局
        return ft.Row(
            [
                rail,
                ft.VerticalDivider(width=1),
                self.content,  # 确保 self.content 被添加到布局中
            ],
            expand=True,
        )

    def on_navigation_change(self, e):
        old_index = self.selected_index
        self.selected_index = e.control.selected_index
        self.controller.switch_navigation_rail(old_index, self.selected_index)

    def update_content(self, new_content):
        self.content.content = new_content
        if self.content.page:
            self.content.update()