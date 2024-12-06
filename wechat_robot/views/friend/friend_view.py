import flet as ft
from wechat_robot.utils.config_utils import get_config  

class FriendView:
    def __init__(self, controller):
        self.controller = controller
        self.selected_row = None
        self.friend_list = self.controller.friend_list
        self.member_list = []
        self.friend_name = ""
        self.friend_id = ""

    def build(self):
        self.ft_friend_list_title = self.friend_list_title()
        self.ft_friend_list_button = self.friend_list_button()
        self.ft_friend_list_data_title = self.friend_list_data_title()
        self.ft_friend_list_data = self.friend_list_data()

        return ft.Tabs(
            selected_index=0,
            animation_duration=300,
            tabs=[
                ft.Tab(
                    text="好友管理",
                    content=ft.Container(
                        content=ft.Column(
                            controls=[
                                self.build_friend_list_view(),
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

    # 好友列表
    def build_friend_list_view(self):
        return ft.Container(
            content=ft.Column(
                controls=[
                    # self.ft_friend_list_title,
                    self.ft_friend_list_button,
                    self.ft_friend_list_data_title,
                    self.ft_friend_list_data,
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
    def friend_list_title(self):
        return ft.Container(
            content=ft.Row(
                controls=[
                    ft.Text("好友列表", style="titleLarge"),
                ],
                alignment=ft.MainAxisAlignment.START,
            ),
        )

    # 按钮
    def friend_list_button(self):
        ft_find = ft.TextField(
            label="查找",
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
            text="刷新",
            on_click=lambda e: self.controller.view_pull_wechat_list(),
        )
        return ft.Container(
            content=ft.Row(
                controls=[ft_find, ft_find_button, ft_refresh],
                spacing=10,
                alignment=ft.MainAxisAlignment.START,
            ),
        )

    # 好友列表数据标题
    def friend_list_data_title(self):
        return ft.Container(
            content=ft.Row(
                controls=[
                    ft.Container(ft.Text("序号", weight=ft.FontWeight.BOLD), expand=1),
                    ft.Container(ft.Text("昵称", weight=ft.FontWeight.BOLD), expand=2),
                    ft.Container(ft.Text("微信ID", weight=ft.FontWeight.BOLD), expand=2),
                    ft.Container(ft.Text("状态", weight=ft.FontWeight.BOLD), expand=1),
                    ft.Container(ft.Text("", weight=ft.FontWeight.BOLD), expand=1),
                ],
                alignment=ft.MainAxisAlignment.START,
            ),
            padding=ft.padding.only(bottom=5),
            border=ft.border.only(bottom=ft.BorderSide(1, ft.colors.BLACK87)),
        )

    # 好友列表数据
    def friend_list_data(self):
        self.ft_lv = ft.ListView(expand=True, spacing=5)
        for index, data in enumerate(self.friend_list, start=1):
            self.ft_lv.controls.append(self.friend_list_data_line(data, index))
        return ft.Container(
            expand=True,
            content=self.ft_lv,
            border=ft.border.all(1, ft.colors.BLACK87),
            border_radius=ft.border_radius.all(5),
        )

    def friend_list_data_line(self, data, index):
        ft_index = ft.Container(
            content=ft.Row(
                controls=[
                    ft.Checkbox(value=False),
                    ft.Text(str(index)),
                ],
                alignment=ft.MainAxisAlignment.START,
            ),
            expand=1,
        )
        ft_nick_name = ft.Container(ft.Text(data.get("nick_name", "")), expand=2)
        ft_wx_id = ft.Container(ft.Text(data.get("wx_id", "")), expand=2)
        ft_status = ft.Container(ft.Text(data.get("status", "")), expand=1)
        pb = ft.PopupMenuButton(
            items=[
                ft.PopupMenuItem(
                    text="开启/关闭",
                    on_click=lambda e: self.controller.open_or_close(ft_status, data)
                ),
                ft.PopupMenuItem(),  # divider
                ft.PopupMenuItem(
                    text="好友设置",
                    on_click=lambda e: self.controller.open_friend_setting(),
                ),
            ],
        )
        ft_action = ft.Container(content=pb, expand=1)

        ft_friend_list_data_line = ft.Container(
            content=ft.Row(
                controls=[
                    ft_index,
                    ft_nick_name,
                    ft_wx_id,
                    ft_status,
                    ft_action,
                ],
                alignment=ft.MainAxisAlignment.START,
            ),
            padding=ft.padding.symmetric(vertical=5),
            on_click=lambda e: self.controller.on_click_friend_list(
                ft_friend_list_data_line, data
            ),
            ink=True,
            border=ft.border.only(bottom=ft.BorderSide(1, ft.colors.BLACK87)),
        )
        return ft_friend_list_data_line