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

        return ft.Container(content=ft.Tabs(
            selected_index=0,
            animation_duration=300,
            label_text_style=ft.TextStyle(size=18,weight=ft.FontWeight.BOLD),

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
                        bgcolor="#F2F4F8",
                    ),
                ),
                ft.Tab(
                    text="帮助说明",
                    content=ft.Text("This is Tab 4"),
                ),
            ],
            expand=True,
            # height=600,
            width=1150,
        ),
        padding=ft.padding.only(left=20, top=0, right=0, bottom=0),bgcolor="#F2F4F8")

    # 好友列表视图
    def build_friend_list_view(self):
        return ft.Container(
            content=ft.Column(
                controls=[
                    self.ft_friend_list_title,
                    self.ft_friend_list_button,
                    self.ft_friend_list_data_title,
                    self.ft_friend_list_data,
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
    def friend_list_title(self):
        return ft.Container(
            content=ft.Row(
                controls=[
                    ft.Icon(ft.icons.PERSON),
                    ft.Text("好友列表")
                ]
            ),
        )

    # 按钮
    def friend_list_button(self):
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

    # 好友列表数据标题
    def friend_list_data_title(self):
        return ft.Container(
            content=ft.Row(
                controls=[
                    ft.Container(ft.Text("序号", weight=ft.FontWeight.BOLD), expand=1, alignment=ft.alignment.center),
                    ft.Container(ft.Text("昵称", weight=ft.FontWeight.BOLD), expand=4),
                    ft.Container(ft.Text("微信ID", weight=ft.FontWeight.BOLD), expand=3),
                    ft.Container(ft.Text("状态", weight=ft.FontWeight.BOLD), expand=1, alignment=ft.alignment.center),
                    ft.Container(ft.Text("操作", weight=ft.FontWeight.BOLD), expand=1, alignment=ft.alignment.center),
                ],
                alignment=ft.MainAxisAlignment.START,
            ),
            width=1100,
            height=40,
            bgcolor="#F2F4F8",
        )

    # 好友列表数据
    def friend_list_data(self):
        self.ft_lv = ft.ListView(expand=True, spacing=0, padding=0)
        for index, data in enumerate(self.friend_list):
            self.ft_lv.controls.append(self.friend_list_data_line(data, index))
        return ft.Container(
            expand=True,
            content=self.ft_lv,
            border_radius=ft.border_radius.all(5),
        )

    def friend_list_data_line(self, data, index):
        bgcolor = "#FFFFFF" if index % 2 == 0 else "#F2F4F8"
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
        ft_nick_name = ft.Container(ft.Text(data.get("nick_name", "")), expand=4)
        ft_wx_id = ft.Container(ft.Text(data.get("wx_id", "")), expand=3)
        # 根据状态设置边框颜色
        status_text = data.get("status", "未知")
        status_color = ft.colors.GREEN if status_text == "开启" else ft.colors.RED
        ft_status = ft.Container(
            content=ft.Text(status_text),
            expand=1,
            border=ft.border.all(1, status_color),
            alignment=ft.alignment.center,
        )
        pb = ft.PopupMenuButton(
            items=[
                ft.PopupMenuItem(
                    text="开启/关闭",
                    on_click=lambda e: self.controller.open_or_close(ft_status, data)
                ),
                ft.PopupMenuItem(),  # 分隔线
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
            bgcolor=bgcolor,
        )
        return ft_friend_list_data_line