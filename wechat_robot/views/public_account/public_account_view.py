import flet as ft
from wechat_robot.utils.config_utils import get_config


class PublicAccountView:
    def __init__(self, controller):
        self.controller = controller
        self.selected_row = None
        self.public_account_list = self.controller.public_account_list
        self.member_list = []
        self.public_account_name = ""
        self.public_account_id = ""

    def build(self):
        self.ft_public_account_list_title = self.public_account_list_title()
        self.ft_public_account_list_button = self.public_account_list_button()
        self.ft_public_account_list_data_title = self.public_account_list_data_title()
        self.ft_public_account_list_data = self.public_account_list_data()

        return ft.Tabs(
            selected_index=0,
            animation_duration=300,
            tabs=[
                ft.Tab(
                    text="公众号管理",
                    content=ft.Container(
                        content=ft.Column(
                            controls=[
                                self.build_public_account_list_view(),
                            ],
                            expand=True,
                        ),
                        padding=10,
                        expand=True,
                    ),
                ),
                ft.Tab(
                    text="帮助说明",
                    content=ft.Text("This is Tab 4"),
                ),
            ],
            expand=True,
            width=1100,
        )

    # 公众号列表
    def build_public_account_list_view(self):
        return ft.Container(
            content=ft.Column(
                controls=[
                    # self.ft_public_account_list_title,
                    self.ft_public_account_list_button,
                    self.ft_public_account_list_data_title,
                    self.ft_public_account_list_data,
                ],
                spacing=10,
                expand=True,
            ),
            border=ft.border.all(1, ft.colors.BLACK87),
            border_radius=ft.border_radius.all(5),
            padding=10,
            expand=True,
        )

    # 标题，靠左
    def public_account_list_title(self):
        return ft.Container(
            content=ft.Row(
                controls=[
                    ft.Text("公众号列表", style="titleLarge"),
                ],
                alignment=ft.MainAxisAlignment.START,
            ),
        )

    # 按钮
    def public_account_list_button(self):
        ft_find = ft.TextField(
            label="查找",
            autofill_hints=ft.AutofillHint.NAME,
            text_size=18,
            height=30,
            width=150,
        )
        ft_find_button = ft.ElevatedButton(
            "查找",
            width=80,
            height=30,
            on_click=lambda e: self.controller.search_wechat_list(ft_find.value),
        )
        ft_refresh = ft.TextButton(
            text="刷新", on_click=lambda e: self.controller.view_pull_wechat_list()
        )
        return ft.Container(
            content=ft.Row(
                controls=[ft_find, ft_find_button, ft_refresh],
                spacing=10,
                alignment=ft.MainAxisAlignment.START,
            ),
        )

    # 公众号列表数据标题
    def public_account_list_data_title(self):
        return ft.Container(
            content=ft.Row(
                controls=[
                    ft.Container(ft.Text("序号", weight=ft.FontWeight.BOLD), expand=1),
                    ft.Container(
                        ft.Text("群名称", weight=ft.FontWeight.BOLD), expand=3
                    ),
                    ft.Container(
                        ft.Text("公众号ID", weight=ft.FontWeight.BOLD), expand=2
                    ),
                ],
                alignment=ft.MainAxisAlignment.START,
            ),
            padding=ft.padding.only(bottom=5),
            border=ft.border.only(bottom=ft.BorderSide(1, ft.colors.BLACK87)),
        )

    # 公众号列表数据
    def public_account_list_data(self):
        self.ft_lv = ft.ListView(expand=1, spacing=5)
        for index, data in enumerate(self.public_account_list, start=1):
            self.ft_lv.controls.append(self.public_account_list_data_line(data, index))
        return ft.Container(
            expand=True,
            content=self.ft_lv,
            border=ft.border.all(1, ft.colors.BLACK87),
            border_radius=ft.border_radius.all(5),
        )

    def public_account_list_data_line(self, data, index):
        ft_index = ft.Container(
            content=ft.Row(
                controls=[
                    # 选择框
                    ft.Checkbox(value=False),
                    ft.Text(str(index)),
                ],
                alignment=ft.MainAxisAlignment.START,
            ),
            expand=1,
        )
        ft_nick_name = ft.Container(ft.Text(data.get("nick_name", "")), expand=3)
        ft_wx_id = ft.Container(ft.Text(data.get("wx_id", "")), expand=2)

        ft_public_account_list_data_line = ft.Container(
            content=ft.Row(
                controls=[
                    ft_index,
                    ft_nick_name,
                    ft_wx_id,
                ],
                alignment=ft.MainAxisAlignment.START,
            ),
            padding=ft.padding.symmetric(vertical=5),
            on_click=lambda e: self.controller.on_click_public_account_list(
                ft_public_account_list_data_line, data
            ),
            ink=True,
            border=ft.border.only(bottom=ft.BorderSide(1, ft.colors.BLACK87)),
        )
        return ft_public_account_list_data_line
