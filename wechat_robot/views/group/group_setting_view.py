# filepath: /d:/gr_project/wechat_robot_flet/wechat_robot/views/group/group_setting_view.py
import flet as ft


class GroupSettingView:
    def __init__(self, controller):
        self.controller = controller
        self.group_id = controller.group_id
        self.group_name = controller.group_name

    def build(self):
        # 创建返回按钮
        back_button = ft.IconButton(
            icon=ft.icons.ARROW_BACK, on_click=self.controller.go_back
        )
        # 创建 Tabs
        ft_tab = self.setting_tab()
        ft_bt_save = self.save_button()
        return ft.Column(controls=[back_button, ft_tab, ft_bt_save], expand=True)

    # Tab界面
    def setting_tab(self):
        first_temp = self.tip_group_setting_build()

        tabs = ft.Tabs(
            tabs=[
                ft.Tab(
                    text="群内提醒",
                    content=ft.Container(content=first_temp),
                ),
                ft.Tab(
                    text="群内设置",
                    content=ft.Container(
                        content=ft.Text(f"这是群 {self.group_name} 的设置页面")
                    ),
                ),
                ft.Tab(
                    text="踢人设置",
                    content=ft.Container(content=ft.Text("踢人设置内容")),
                ),
            ]
        )
        return ft.Container(
            content=tabs,
            height=500,
            # alignment=ft.alignment.center
        )

    # 保存按钮
    def save_button(self):
        ft_save_all = ft.ElevatedButton(
            "保存到所有群",
            width=200,
            height=30,
        )
        ft_save = ft.ElevatedButton(
            "保存",
            width=80,
            height=30,
        )
        return ft.Container(
            content=ft.Row(
                controls=[ft_save_all, ft_save],
                alignment=ft.MainAxisAlignment.SPACE_AROUND,  # 水平右对齐
            ),
            alignment=ft.alignment.bottom_right,  # 垂直底部对齐
            padding=ft.padding.all(10),
        )

    def tip_group_setting_build(self):
        tf_tip_group_setting = self.tip_group_setting()

        return ft.Container(
            content=ft.Column(
                controls=[
                    tf_tip_group_setting,
                    tf_tip_group_setting,
                    tf_tip_group_setting,
                ],
                # alignment=ft.MainAxisAlignment.END  # 水平右对齐
            ),
            # height=400,
            # alignment=ft.alignment.bottom_right,    # 垂直底部对齐
            padding=ft.padding.all(10),
        )

    # 群内提醒界面
    def tip_group_setting(self):
        first = self.tip_group_setting_title_first()
        first_text = ft.TextField(
            label="模板一", icon=ft.icons.EMOJI_EMOTIONS, width=800
        )
        tf_tip = self.tip_group_setting_text()
        return ft.Container(
            content=ft.Row(
                controls=[
                    ft.Container(
                        ft.Column(
                            controls=[first, first_text],
                            # alignment=ft.MainAxisAlignment.END  # 水平右对齐
                        )
                    ),
                    tf_tip,
                ]
            ),
            # height=400,
            # alignment=ft.alignment.bottom_right,    # 垂直底部对齐
            padding=ft.padding.all(10),
        )

    # 群内提醒界面标题
    def tip_group_setting_title_first(self):
        ft_title = ft.Text(
            "退群提示",
            size=18,
            color=ft.colors.BLACK,
            weight=ft.FontWeight.BOLD,
        )
        ft_templet_1 = ft.TextButton(text="模板一")
        close_templet_1 = ft.TextButton(text="关闭提醒")

        return ft.Container(
            content=ft.Row(
                controls=[ft_title, ft_templet_1, close_templet_1],
                alignment=ft.MainAxisAlignment.START,
            ),
            alignment=ft.alignment.bottom_right,  # 垂直底部对齐
            padding=ft.padding.all(10),
        )

    # 群内提醒文字提示
    def tip_group_setting_text(self):
        ft_tip = ft.Text(
            "只支持文字、emoji表情，换行in或[enter群用户:[name]，强制开启:[开启]",
            size=20,
            color=ft.colors.RED_800,
            # weight=ft.FontWeight.BOLD,
            width=300,
        )
        return ft.Container(
            content=ft_tip,
            alignment=ft.alignment.center,  # 垂直底部对齐
            padding=ft.padding.all(10),
        )
