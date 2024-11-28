# filepath: /d:/gr_project/wechat_robot_flet/wechat_robot/views/group/group_setting_view.py
import flet as ft
from wechat_robot.utils.config_utils import get_config


class GroupSettingView:
    def __init__(self, controller, page: ft.Page):
        self.controller = controller
        self.page = page  # 添加这一行
        self.group_id = controller.group_id
        self.group_name = controller.group_name
        self.out_setting = controller.out_setting
        self.welcome_setting = controller.welcome_setting
        self.fun_setting = controller.fun_setting
        self.out_setting_tip = controller.out_setting_tip
        self.welcome_setting_tip = controller.welcome_setting_tip
        self.fun_setting_tip = controller.fun_setting_tip
        self.out_setting_template = controller.out_setting_template
        self.welcome_setting_template = controller.welcome_setting_template
        self.fun_setting_template = controller.fun_setting_template

    def build(self):
        # 创建返回按钮

        ft_back_button = ft.IconButton(
            icon=ft.icons.ARROW_BACK,
            on_click=self.controller.go_back,
            # 增加文字
        )
        # 显示群名
        ft_group_name = ft.Text(
            f"当前群：{self.group_name}",
            size=20,
            color=ft.colors.RED_800,
            weight=ft.FontWeight.BOLD,
        )

        ft_line = ft.Row(
            controls=[ft_back_button, ft_group_name],
            # 左右两边各放一个
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        )
        # 创建 Tabs
        ft_tab = self.setting_tab()
        ft_bt_save = self.save_button()
        return ft.Column(controls=[ft_line, ft_tab, ft_bt_save], expand=True)

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
            expand=True,
            # alignment=ft.alignment.center
        )

    # 保存按钮
    def save_button(self):
        ft_save_all = ft.ElevatedButton(
            "保存到所有群",
            width=200,
            # height=30,
        )
        ft_save = ft.ElevatedButton(
            "保存",
            width=80,
            # height=30,
            on_click=lambda e: self.controller.save_group_setting(),
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
        self.tf_out_group_setting = self.tip_group_setting(
            "退群提醒",
            "关闭提醒",
            self.out_setting_tip,
            self.out_setting_template,
            self.out_setting,
        )
        self.tf_welcome_group_setting = self.tip_group_setting(
            "新人欢迎语",
            "关闭欢迎语",
            self.welcome_setting_tip,
            self.welcome_setting_template,
            self.welcome_setting,
        )
        self.tf_fun_group_setting = self.tip_group_setting(
            "功能样式",
            "关闭样式",
            self.fun_setting_tip,
            self.fun_setting_template,
            self.fun_setting,
        )
        return ft.Container(
            content=ft.Column(
                controls=[
                    self.tf_out_group_setting,
                    self.tf_welcome_group_setting,
                    self.tf_fun_group_setting,
                ],
            ),
            height=450,
            padding=ft.padding.all(10),
        )

    # 群内提醒界面
    def tip_group_setting(self, label, close_label, tip, templet, value):

        # 点击first_text给tf_tip赋值
        tf_tip = self.tip_group_setting_text(tip)

        first_text = ft.TextField(
            label="模板一",
            icon=ft.icons.EMOJI_EMOTIONS,
            width=800,
            multiline=True,
            value=value,
        )
        first = self.tip_group_setting_title_first(
            label, close_label, templet, first_text
        )

        return ft.Container(
            content=ft.Row(
                controls=[
                    ft.Container(
                        content=ft.Column(
                            controls=[first, first_text],
                            # alignment=ft.MainAxisAlignment.END  # 水平右对齐
                        )
                    ),
                    tf_tip,
                ]
            ),
            # height=400,
            # alignment=ft.alignment.bottom_right,    # 垂直底部对齐
            # padding=ft.padding.all(10),
        )

    # 群内提醒界面标题
    def tip_group_setting_title_first(self, label, close_label, templet, first_text):
        ft_title = ft.Text(
            label,
            size=18,
            color=ft.colors.BLACK,
            weight=ft.FontWeight.BOLD,
        )

        def click_templet(templet):
            # 给tf_tip下的first_text赋值
            first_text.value = templet
            first_text.update()

        ft_templet_1 = ft.TextButton(
            text="模板一", on_click=lambda e: click_templet(templet)
        )
        close_templet_1 = ft.TextButton(text=close_label)

        return ft.Container(
            content=ft.Row(
                controls=[ft_title, ft_templet_1, close_templet_1],
                alignment=ft.MainAxisAlignment.START,
            ),
            alignment=ft.alignment.bottom_right,  # 垂直底部对齐
            padding=ft.padding.all(10),
            expand=True,
        )

    # 群内提醒文字提示
    def tip_group_setting_text(self, tip):
        ft_tip = ft.Text(
            tip,
            # size=20,
            color=ft.colors.RED_800,
            # weight=ft.FontWeight.BOLD,
            width=300,
        )
        return ft.Container(
            content=ft_tip,
            alignment=ft.alignment.bottom_right,  # 垂直底部对齐
            padding=ft.padding.all(10),
            expand=True,
        )

    # 保存成功提示，弹窗显示
    def show_success(self):
        def handle_close(e):
            dlg_modal.open = False
            self.page.update()

        dlg_modal = ft.AlertDialog(
            modal=True,
            title=ft.Text("操作成功"),
            content=ft.Text("设置已保存成功！"),
            actions=[
                ft.TextButton("确定", on_click=handle_close),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        # 使用新的方式添加对话框
        self.page.overlay.append(dlg_modal)
        dlg_modal.open = True
        self.page.update()
