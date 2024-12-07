import flet as ft


class GroupView:
    def __init__(self, controller):
        self.controller = controller
        # self.view_pull_wechat_list = view_pull_wechat_list
        self.selected_row = None
        self.group_list = self.controller.group_list
        self.member_list = self.controller.group_members_list
        self.group_name = self.controller.group_name
        self.group_id = self.controller.group_id

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
        return ft.Container(content=
                            ft.Tabs(
            selected_index=0,
            animation_duration=300,
            label_text_style=ft.TextStyle(size=18,weight=ft.FontWeight.BOLD),
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
                    content=ft.Text("This is Tab 4"),
                ),
            ],
            expand=True,
            # height=600,
            width=1150,
        ),padding=ft.padding.only(left=20, top=0, right=0, bottom=0),bgcolor="#F2F4F8")


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
            height=594,
            width=495,
            padding=10,
            # 增加边框
            # border=ft.border.all(1, ft.colors.BLACK87),
            bgcolor=ft.colors.WHITE,
            border_radius=ft.border_radius.all(5),
            # box-shadow: 2px 2px 2px 0px #69707733;

            # shadow=ft.BoxShadow(
            #     spread_radius=1,
            #     # blur_radius=15,
            #     color="#69707733",
            #     # offset=ft.Offset(0, 0),
            #     # blur_style=ft.ShadowBlurStyle.OUTER,
            # )
        )

    # 第一行标题,靠左
    def group_list_title(self):
        return ft.Container(
            content=ft.Row(
                [   ft.Icon(ft.icons.GROUP),
                    ft.Text("群列表"),
                ]
            ),
        )

    # 按钮
    def group_list_button(self):
        ft_find = ft.TextField(
            label="群名称",
            autofill_hints=ft.AutofillHint.NAME,
            text_size=12,
            height=25,
            width=165,
            border=ft.border.all(1, ft.colors.BLACK87),
            bgcolor="#F2F4F8",
            color="#F2F4F8",
        )
        ft_find_button = ft.ElevatedButton(
            "查找",
            width=55,
            height=25,
            color="#FFFFFF",
            bgcolor="#001D6C",
            on_click=lambda e: self.controller.search_wechat_list(ft_find.value),
        )
        # ft_import = ft.TextButton(text="导出")
        ft_update = ft.ElevatedButton(
            width=55,
            height=25,
            text="刷新", on_click=lambda e: self.controller.view_pull_wechat_list()
        )
        return ft.Container(
            content=ft.Row([ft_find, ft_find_button, ft_update]),
            width=550,
        )

    # 群列表数据标题
    def group_list_data_title(self):
        return ft.Container(
            content=ft.Row(
                controls=[
                    ft.Container(ft.Text("序号", weight=ft.FontWeight.BOLD), expand=2,alignment=ft.alignment.center),
                    ft.Container(
                        ft.Text("群名称", weight=ft.FontWeight.BOLD), expand=4
                    ),
                    ft.Container(
                        ft.Text("状态", weight=ft.FontWeight.BOLD), expand=1
                    ),
                    ft.Container(ft.Text("", weight=ft.FontWeight.BOLD), expand=1),
                ],
                alignment=ft.MainAxisAlignment.START,
            ),
            width=470,
            height=40,
            bgcolor="#F2F4F8",
            # padding=0,
        )

    # 群列表数据
    def group_list_data(self):
        self.ft_lv = ft.ListView(expand=True, padding=0)
        # 生成测试数据，序号，昵称，备注
        for index, data in enumerate(self.group_list):
            self.ft_lv.controls.append(self.group_list_data_line(data, index))
        return ft.Container(
            expand=True,
            content=self.ft_lv,
            border_radius=ft.border_radius.all(5),
        )

    def group_list_data_line(self, data, index):
        bgcolor = "#FFFFFF" if index % 2 == 0 else "#F2F4F8"
        # 每行增加边框
        ft_index = ft.Container(
            content=ft.Row(
                controls=[
                    ft.Checkbox(value=False),
                    ft.Text(str(index)),
                ],
                alignment=ft.MainAxisAlignment.START,
            ),
            expand=2,
        )
        ft_nick_name = ft.Container(ft.Text(data["nick_name"]), expand=4)
        # ft_status = ft.Text(data["status"], size=20)
        ft_status = ft.Container(content=ft.Text(data["status"]), expand=1)
        pb = ft.PopupMenuButton(
            items=[
                ft.PopupMenuItem(text="开启/关闭", on_click=lambda e: self.controller.open_or_close(ft_status, data)),
                ft.PopupMenuItem(),  # divider
                ft.PopupMenuItem(
                    text="群设置",
                    on_click=lambda e: self.controller.open_group_setting(),
                ),
            ],
            on_open=lambda e: self.controller.on_click_group_list(
                ft_group_list_data_line, data,bgcolor
            ),
        )
        ft_action = ft.Container(content=pb, expand=1)
        
        ft_group_list_data_line = ft.Container(
            content=ft.Row(
                controls=[
                    ft_index,
                    ft_nick_name,
                    ft_status,
                    ft_action,
                    # ft.Container(content=ft.Text(data['status'], size=10), width=100),
                ],
                alignment=ft.MainAxisAlignment.START,
            ),  # 绑定点击事件处理函数
            on_click=lambda e: self.controller.on_click_group_list(
                ft_group_list_data_line, data,bgcolor
            ),
            padding=ft.padding.symmetric(vertical=5),
            ink=True,
            # border=ft.border.only(bottom=ft.BorderSide(1, ft.colors.BLACK87)),
            height=50,
            width=470,
            bgcolor=bgcolor,
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
            height=594,
            width=495,
            padding=10,
            # 增加边框
            # border=ft.border.all(1, ft.colors.BLACK87),
            bgcolor=ft.colors.WHITE,
            border_radius=ft.border_radius.all(5),
        )

    # 群成员标题
    def group_member_title(self):

        self.group_member_text = ft.Text(
            f"[当前:{self.group_name}]", color="#001D6C",
        )
        return ft.Container(
            content=ft.Row(
                controls=[
                    ft.Container(
                        ft.Row(controls=[
                        ft.Icon(ft.icons.GROUPS),
                        ft.Text("群成员"),]),),
                    ft.Container(
                        self.group_member_text,
                        alignment=ft.alignment.center_right,
                        expand=3,
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            ),
        )

    # 按钮
    def group_member_button(self):
        ft_find = ft.TextField(
            label="昵称",
            autofill_hints=ft.AutofillHint.NAME,
            text_size=12,
            height=25,
            width=165,
            color="#001D6C",
        )
        ft_find_button = ft.ElevatedButton(
            text="查找",
            width=55,
            height=25,
            color="#FFFFFF",
            bgcolor="#001D6C",
        )
        # ft_import = ft.TextButton(text="导出")
        ft_update = ft.ElevatedButton(text="刷新",width=55,height=25,)
        return ft.Container(
            content=ft.Row([ft_find, ft_find_button, ft_update]),
            width=500,
            # alignment=ft.Alignment.bottom_left
        )

    # 群成员数据标题
    def group_member_data_title(self):
        return ft.Container(
            content=ft.Row(
                controls=[
                    ft.Container(ft.Text("序号", weight=ft.FontWeight.BOLD), expand=1,alignment=ft.alignment.center),
                    ft.Container(ft.Text("昵称", weight=ft.FontWeight.BOLD), expand=3),
                    ft.Container(ft.Text("状态", weight=ft.FontWeight.BOLD), expand=1),
                ],
                alignment=ft.MainAxisAlignment.START,
            ),
            width=470,
            height=40,
            # padding=ft.padding.only(bottom=5),
            bgcolor="#F2F4F8",
            # border=ft.border.only(bottom=ft.BorderSide(1, ft.colors.BLACK87)),
        )

    # 群成员数据
    def group_member_data(self):
        self.ft_lv_member_list = ft.ListView(expand=True, padding=0)
        # 生成测试数据，序号，昵称，备注
        for index, data in enumerate(self.member_list):
            self.ft_lv_member_list.controls.append(
                self.group_member_data_line(data, index)
            )
        return ft.Container(
            expand=True,
            content=self.ft_lv_member_list,
            # border=ft.border.all(1, ft.colors.BLACK87),
            border_radius=ft.border_radius.all(5),
        )

    def group_member_data_line(self, data, index):
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
        ft_nick_name = ft.Container(ft.Text(data.get("nick_name", "")), expand=3)
        ft_wx_id = ft.Container(ft.Text("开启"), expand=1)
        return ft.Container(
            content=ft.Row(
                controls=[
                    ft_index,
                    ft_nick_name,
                    ft_wx_id,
                ],
            ),
            padding=ft.padding.symmetric(vertical=5),
            ink=True,
            bgcolor=bgcolor,
            height=50,
            # border=ft.border.only(bottom=ft.BorderSide(1, ft.colors.BLACK87)),
        )
