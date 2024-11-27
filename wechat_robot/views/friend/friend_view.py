import flet as ft
from wechat_robot.utils.config_utils import get_config  

class FriendView:
    def __init__(self, controller):
        self.controller = controller
        # self.view_pull_wechat_list = view_pull_wechat_list
        self.selected_row = None
        self.friend_list = self.controller.friend_list
        self.member_list = []
        self.friend_name = ""
        self.friend_id = ""

    def build(self):
        # 构建好友列表视图和群成员视图
        self.ft_friend_list_title = self.friend_list_title()
        self.ft_friend_list_button = self.friend_list_button()
        self.ft_friend_list_data_title = self.friend_list_data_title()
        self.ft_friend_list_data = self.friend_list_data()
        self.friend_list_view = self.build_friend_list_view()

        # 返回整个群组视图
        return ft.Tabs(
            selected_index=0,
            animation_duration=300,
            tabs=[
                ft.Tab(
                    text="好友管理",
                    content=ft.Container(
                        content=ft.Row(
                            controls=[
                                self.build_friend_list_view(),
                            ]
                        ),
                    ),
                ),
                ft.Tab(
                    text="帮助说明",
                    icon=ft.icons.SETTINGS,
                    content=ft.Text("This is Tab 4"),
                ),
            ],
            expand=1,
            height=600,
            width=1100,
        )

    # 好友列表
    def build_friend_list_view(self):
        return ft.Container(
            content=ft.Column(
                controls=[
                    self.ft_friend_list_title,
                    self.ft_friend_list_button,
                    self.ft_friend_list_data_title,
                    self.ft_friend_list_data,
                ]
            ),
            height=600,
            width=1100,
            padding=10,
            # 增加边框
            border=ft.border.all(1, ft.colors.GREY),
        )

    # 第一行标题,靠左
    def friend_list_title(self):
        return ft.Container(
            content=ft.Row(
                [
                    ft.Text("好友列表"),
                ]
            ),
        )

    # 按钮
    def friend_list_button(self):
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
        # ft_import = ft.TextButton(text="导出")
        ft_delete = ft.TextButton(
            text="刷新", on_click=lambda e: self.controller.view_pull_wechat_list()
        )
        return ft.Container(
            content=ft.Row([ft_find, ft_find_button, ft_delete]),
            width=550,
        )

    # 好友列表数据标题
    def friend_list_data_title(self):
        return ft.Container(
            content=ft.Row(
                controls=[
                    ft.Container(width=10),
                    ft.Container(content=ft.Text("序号"), width=100),
                    ft.Container(content=ft.Text("群名称", selectable=True), width=120),
                    ft.Container(content=ft.Text("群状态", selectable=True), width=200),
                    ft.Container(content=ft.Text("微信ID", selectable=True), width=200),
                ],
                spacing=0,
            ),
            width=500,
        )

    # 好友列表数据
    def friend_list_data(self):
        self.ft_lv = ft.ListView(expand=1, padding=1)
        count = 1
        # 生成测试数据，序号，昵称，备注
        for index, i in enumerate(self.friend_list):
            self.ft_lv.controls.append(self.friend_list_data_line(i, index))
            count += 1
        return ft.Container(
            height=430,
            width=1100,
            content=ft.Column(
                controls=[
                    self.ft_lv,
                ],
            ),
            border=ft.border.all(1, ft.colors.GREY),
        )

    def friend_list_data_line(self, data, index):
        # 每行增加边框
        def check_item_clicked(e):
            e.control.checked = not e.control.checked
            self.page.update()

        ft_check = ft.Checkbox(label=index, value=False)
        ft_nick_name = ft.Text(data["nick_name"], size=20)
        ft_wx_id = ft.Text(data["wx_id"], size=20)
        # ft_status = ft.Text(data["status"], size=20)
        ft_status = ft.Container(content=ft.Text(data["status"], size=20, width=200, height=30))
        pb = ft.PopupMenuButton(
            items=[
                ft.PopupMenuItem(text="开启/关闭", on_click=lambda e: self.controller.open_or_close(ft_status, data)),
                ft.PopupMenuItem(),  # divider
                ft.PopupMenuItem(
                    text="群设置",
                    on_click=lambda e: self.controller.open_friend_setting(),
                ),
            ],
            on_open=lambda e: self.controller.on_click_friend_list(
                ft_friend_list_data_line, data
            ),
        )
        ft_friend_list_data_line = ft.Container(
            content=ft.Row(
                controls=[
                    ft.Container(
                        content=ft_check,
                        width=50,
                        height=30,
                        alignment=ft.alignment.center_left,
                    ),
                    ft.Container(
                        content=ft_nick_name,
                        width=150,
                        height=60,
                        alignment=ft.alignment.center_left,
                    ),
                    
                    
                    
                    ft_status,
                    
                    ft.Container(
                        content=ft_wx_id,
                        width=150,
                        height=60,
                        alignment=ft.alignment.center_left,
                    ),
                    ft.Container(content=pb, width=80, height=30),
                    # ft.Container(content=ft.Text(data['status'], size=10), width=100),
                ],
            ),  # 绑定点击事件处理函数
            on_click=lambda e: self.controller.on_click_friend_list(
                ft_friend_list_data_line, data
            ),
            border=ft.border.all(1, ft.colors.GREY),
        )
        return ft_friend_list_data_line