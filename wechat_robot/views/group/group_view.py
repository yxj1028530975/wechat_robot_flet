import flet as ft


class GroupView:
    def __init__(self, controller):
        self.controller = controller
        # self.view_pull_wechat_list = view_pull_wechat_list
        self.selected_row = None
        self.group_list = self.controller.group_list
        self.member_list = []
        self.group_name = ""
        self.group_id = ""

    def build(self):
        # 构建群列表视图和群成员视图
        self.ft_group_list_title = self.group_list_title()
        self.ft_group_list_button = self.group_list_button()
        self.ft_group_list_data_title = self.group_list_data_title()
        self.ft_group_list_data = self.group_list_data()
        self.ft_group_member_title = self.group_member_title()
        self.ft_group_member_button = self.group_member_button()
        self.ft_group_member_data_title = self.group_member_data_title()
        self.ft_group_member_data = self.group_member_data()

        self.group_list_view = self.build_group_list_view()
        self.group_member_view = self.build_group_member_view()

        # 返回整个群组视图
        return ft.Tabs(
            selected_index=0,
            animation_duration=300,
            tabs=[
                ft.Tab(
                    text="群管理",
                    content=ft.Container(
                        content=ft.Row(
                            controls=[
                                self.build_group_list_view(),
                                self.build_group_member_view(),
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

    # 群列表
    def build_group_list_view(self):
        return ft.Container(
            content=ft.Column(
                controls=[
                    self.ft_group_list_title,
                    self.ft_group_list_button,
                    self.ft_group_list_data_title,
                    self.ft_group_list_data,
                ]
            ),
            height=600,
            width=550,
            padding=10,
            # 增加边框
            border=ft.border.all(1, ft.colors.GREY),
        )

    # 第一行标题,靠左
    def group_list_title(self):
        return ft.Container(
            content=ft.Row(
                [
                    ft.Text("群列表"),
                ]
            ),
        )

    # 按钮
    def group_list_button(self):
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

    # 群列表数据标题
    def group_list_data_title(self):
        return ft.Container(
            content=ft.Row(
                controls=[
                    ft.Container(width=10),
                    ft.Container(content=ft.Text("序号"), width=100),
                    ft.Container(content=ft.Text("群名称"), width=120),
                    ft.Container(content=ft.Text("群ID"), width=200),
                ],
                spacing=0,
            ),
            width=500,
        )

    # 群列表数据
    def group_list_data(self):
        self.ft_lv = ft.ListView(expand=1, padding=1)
        count = 1
        # 生成测试数据，序号，昵称，备注
        for index, i in enumerate(self.group_list):
            self.ft_lv.controls.append(self.group_list_data_line(i, index))
            count += 1
        return ft.Container(
            height=430,
            width=550,
            content=ft.Column(
                controls=[
                    self.ft_lv,
                ],
            ),
            border=ft.border.all(1, ft.colors.GREY),
        )

    def group_list_data_line(self, data, index):
        # 每行增加边框
        ft_check = ft.Checkbox(label=index, value=False)
        ft_nick_name = ft.Text(data["nick_name"], size=20)
        ft_wx_id = ft.Text(data["wx_id"], size=20)
        ft_bt = ft.ElevatedButton(
                            "设置",
                            width=80,
                            height=30,
                            on_click=lambda e: self.controller.open_group_setting(
                                ft_group_list_data_line,data
                            ),
                        )
        ft_group_list_data_line = ft.Container(
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
                    ft.Container(
                        content=ft_wx_id, width=200, height=30
                    ),
                    ft.Container(
                        content=ft_bt, width=80, height=30
                    ),
                    # ft.Container(content=ft.Text(data['status'], size=10), width=100),
                ],
            ),  # 绑定点击事件处理函数
            on_click=lambda e: self.controller.on_click_group_list(
                ft_group_list_data_line, data
            ),
            border=ft.border.all(1, ft.colors.GREY),
        )
        return ft_group_list_data_line

    # 群成员
    def build_group_member_view(self):
        return ft.Container(
            content=ft.Column(
                controls=[
                    self.ft_group_member_title,
                    self.ft_group_member_button,
                    self.ft_group_member_data_title,
                    self.ft_group_member_data,
                ]
            ),
            height=600,
            width=550,
            padding=10,
            # 增加边框
            border=ft.border.all(1, ft.colors.GREY),
        )

    # 群成员标题
    def group_member_title(self):
        
        self.group_member_text = ft.Text(f"[群名称:{self.group_name}]", color=ft.colors.RED_500)
        return ft.Container(
            content=ft.Row(
                controls=[
                    ft.Container(
                        ft.Text("群成员"),
                        alignment=ft.alignment.center_left,
                        width=200,
                    ),
                    ft.Container(
                        self.group_member_text,
                        alignment=ft.alignment.center_left,
                        width=300,
                    ),
                ]
            ),
            width=550,
        )

    # 按钮
    def group_member_button(self):
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
        )
        # ft_import = ft.TextButton(text="导出")
        ft_delete = ft.TextButton(text="刷新")
        return ft.Container(
            content=ft.Row([ft_find, ft_find_button, ft_delete]),
            width=500,
            # alignment=ft.Alignment.bottom_left
        )

    # 群成员数据标题
    def group_member_data_title(self):
        return ft.Container(
            content=ft.Row(
                controls=[
                    ft.Container(width=20),
                    ft.Container(content=ft.Text("序号"), width=100),
                    ft.Container(content=ft.Text("昵称"), width=120),
                    ft.Container(content=ft.Text("wxid"), width=100),
                    # ft.Container(content=ft.Text("管理员"), width=100),
                ],
                spacing=0,
            ),
        )

    # 群成员数据
    def group_member_data(self):
        self.ft_lv_member_list = ft.ListView(expand=1, spacing=1, padding=1)
        count = 1
        # 生成测试数据，序号，昵称，备注
        for index, i in enumerate(self.member_list):
            self.ft_lv_member_list.controls.append(
                self.group_member_data_line(i, index)
            )
            count += 1
        return ft.Container(
            height=430,
            width=550,
            content=ft.Column(
                [
                    self.ft_lv_member_list,
                ],
            ),
            border=ft.border.all(1, ft.colors.GREY),
        )

    def group_member_data_line(self, data, index):
        return ft.Container(
            content=ft.Row(
                controls=[
                    ft.Container(
                        content=ft.Checkbox(label=index, value=False),
                        width=50,
                        height=30,
                    ),
                    ft.Container(
                        content=ft.Text(data["nick_name"], size=20),
                        width=150,
                        height=60,
                        alignment=ft.alignment.center_left,
                    ),
                    ft.Container(
                        content=ft.Text(data["wx_id"], size=20),
                        width=200,
                        height=60,
                        alignment=ft.alignment.center_left,
                    ),
                    # ft.Container(content=ft.Text(data['admin'], size=10), width=100),
                ],
            ),
            border=ft.border.all(1, ft.colors.GREY),
        )
