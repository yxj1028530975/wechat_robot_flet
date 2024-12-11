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

        return ft.Container(content=ft.Tabs(
            selected_index=0,
            animation_duration=300,
            label_text_style=ft.TextStyle(size=18,weight=ft.FontWeight.BOLD),
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
                        bgcolor="#F2F4F8",

                    ),
                ),
                ft.Tab(
                    text="帮助说明",
                    content=ft.Text("This is Tab 4"),
                ),
            ],
            expand=True,
            width=1150,
        ),
        padding=ft.padding.only(left=20, top=0, right=0, bottom=0),bgcolor="#F2F4F8")


    # 公众号列表
    def build_public_account_list_view(self):
        return ft.Container(
            content=ft.Column(
                controls=[
                    self.ft_public_account_list_title,
                    self.ft_public_account_list_button,
                    self.ft_public_account_list_data_title,
                    self.ft_public_account_list_data,
                ],
                spacing=10,
                expand=True,
            ),
            height=594,
            width=1000,
            padding=10,
            # 增加边框
            # border=ft.border.all(1, ft.colors.BLACK87),
            bgcolor=ft.colors.WHITE,
            border_radius=ft.border_radius.all(5),

        )

    # 标题，靠左
    def public_account_list_title(self):
        return ft.Container(
            content=ft.Row(
                controls=[
                    ft.Icon(ft.icons.PUBLIC),
                    ft.Text("公众号列表"),
                ],
            ),
        )

    # 按钮
    def public_account_list_button(self):
        ft_find = ft.TextField(
            label="昵称",
            text_size=12,
            height=25,
            width=165,
            border=ft.border.all(1, ft.colors.BLACK87),
            bgcolor="#F2F4F8",
            color="#F2F4F8",
        )
        ft_find_button = ft.ElevatedButton(
            "查找",
            height=25,
            color="#FFFFFF",
            bgcolor="#001D6C",
            on_click=lambda e: self.controller.search_wechat_list(ft_find.value),
        )
        ft_refresh = ft.ElevatedButton(
            text="刷新",
            height=25,
            on_click=lambda e: self.controller.view_pull_wechat_list(),
        )
        return ft.Container(
            content=ft.Row([ft_find, ft_find_button, ft_refresh], spacing=10),
            width=550,
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
            width=1100,
            height=40,
            bgcolor="#F2F4F8",

        )

    # 公众号列表数据
    def public_account_list_data(self):
        self.ft_lv = ft.ListView(expand=1, spacing=5)
        for index, data in enumerate(self.public_account_list):
            self.ft_lv.controls.append(self.public_account_list_data_line(data, index))
        return ft.Container(
            expand=True,
            content=self.ft_lv,
            border_radius=ft.border_radius.all(5),
        )

    def public_account_list_data_line(self, data, index):
        bgcolor = "#FFFFFF" if index % 2 == 0 else "#F2F4F8"

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
            bgcolor=bgcolor,

        )
        return ft_public_account_list_data_line
