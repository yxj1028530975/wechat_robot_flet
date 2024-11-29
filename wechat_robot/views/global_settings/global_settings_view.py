import flet as ft
from wechat_robot.models.robot_setting import SettingCRUD


class GlobalSettingsView:
    def __init__(self, controller):
        self.controller = controller
        # 初始化好友审核开关控件
        self.friend_review_switch = ft.Switch()
        # 初始化好友欢迎语控件
        self.friend_welcome_textfield = ft.TextField(
            multiline=True,
            max_lines=5,
            # width=400,
        )

        self.data_list = [
            {
                "name": "全局设置",
                "id": 1,
                "icon_list": [
                    {
                        "name": "智能聊天",
                        "id": 11,
                        "method": "smart_chat",
                        "icon": "WINDOW_OUTLINED",
                    },
                    {
                        "name": "本地词库",
                        "id": 12,
                        "method": "local_library",
                        "icon": "WINDOW_OUTLINED",
                    },
                    {
                        "name": "防封设置",
                        "id": 13,
                        "method": "anti_seal",
                        "icon": "WINDOW_OUTLINED",
                    },
                    {
                        "name": "软件定时",
                        "id": 14,
                        "method": "software_timing",
                        "icon": "WINDOW_OUTLINED",
                    },
                ],
            },
            {
                "name": "群管设置",
                "id": 2,
                "icon_list": [
                    {
                        "name": "群聊总开关",
                        "id": 21,
                        "method": "group_chat_switch",
                        "icon": "WINDOW_OUTLINED",
                    },
                    {
                        "name": "分群词库",
                        "id": 22,
                        "method": "group_library",
                        "icon": "WINDOW_OUTLINED",
                    },
                    {
                        "name": "群欢迎语",
                        "id": 23,
                        "method": "group_welcome",
                        "icon": "WINDOW_OUTLINED",
                    },
                    {
                        "name": "自动进群",
                        "id": 24,
                        "method": "auto_join_group",
                        "icon": "WINDOW_OUTLINED",
                    },
                    {
                        "name": "群黑名单",
                        "id": 25,
                        "method": "group_blacklist",
                        "icon": "WINDOW_OUTLINED",
                    },
                    {
                        "name": "群聊设置",
                        "id": 26,
                        "method": "group_chat_settings",
                        "icon": "WINDOW_OUTLINED",
                    },
                ],
            },
            {
                "name": "好友设置",
                "id": 3,
                "icon_list": [
                    {
                        "name": "私聊总开关",
                        "id": 31,
                        "method": "private_chat_switch",
                        "icon": "WINDOW_OUTLINED",
                    },
                    {
                        "name": "私聊词库",
                        "id": 32,
                        "method": "private_chat_library",
                        "icon": "WINDOW_OUTLINED",
                    },
                    {
                        "name": "好友欢迎语",
                        "id": 33,
                        "method": "friend_welcome",
                        "icon": "WINDOW_OUTLINED",
                    },
                    {
                        "name": "邀请进群",
                        "id": 34,
                        "method": "invite_group",
                        "icon": "WINDOW_OUTLINED",
                    },
                    {
                        "name": "好友审核",
                        "id": 35,
                        "method": "friend_review_popup",
                        "icon": "WINDOW_OUTLINED",
                    },
                    {
                        "name": "私聊设置",
                        "id": 36,
                        "method": "private_chat_settings",
                        "icon": "WINDOW_OUTLINED",
                    },
                ],
            },
        ]

    def build(self):
        return ft.Container(
            content=ft.Column(
                controls=[
                    self.build_container(),
                ],
                scroll="auto",
                alignment=ft.MainAxisAlignment.START,
            ),
            
            expand=True,
            
        )

    # 构建页面
    def build_container(self):
        ft_column = ft.Column(controls=[], spacing=20)
        for data in self.data_list:
            ft_title = self.global_settings_title(data["name"])
            ft_app_list = self.global_settings_app_list(data["icon_list"])
            ft_column.controls.append(ft_title)
            ft_column.controls.append(ft_app_list)
        return ft.Container(
            content=ft_column,
        )

    # 标题
    def global_settings_title(self, title):
        return ft.Column(
            controls=[
                ft.Text(title, weight="bold"),
                ft.Container(
                    height=1,
                    bgcolor=ft.colors.BLACK87,
                    width="100%",
                ),
            ],
            spacing=5,
        )

    # 应用列表
    def global_settings_app_list(self, data):
        ft_row = ft.Row(
            controls=[],
            alignment=ft.MainAxisAlignment.START,
            spacing=10,
            scroll="auto",
        )
        for app in data:
            ft_row.controls.append(self.global_settings_app(app))
        return ft.Container(
            content=ft_row,
        )

    # 单个应用
    def global_settings_app(self, data):
        ft_icon = ft.Icon(name=getattr(ft.icons, data["icon"]), size=60)
        ft_text = ft.Text(data["name"])
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft_icon,
                    ft_text,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            width=150,
            height=150,
            padding=10,
            border=ft.border.all(1, ft.colors.BLACK87),
            border_radius=ft.border_radius.all(8),
            alignment=ft.alignment.center,
            on_click=lambda e, method_name=data.get("method"): (
                getattr(self, method_name)() if method_name else None
            ),
        )

    # 好友审核弹窗
    def friend_review_popup(self):
        # 从数据库获取初始化数据
        setting = SettingCRUD.get_setting()
        self.friend_review_switch.value = bool(setting.friend_verify)
        self.friend_review_delay = ft.TextField(
            label="延迟（秒）",
            value=str(setting.friend_verify_delay),
        )
        self.friend_review_code = ft.TextField(
            label="暗号（多个用英文逗号隔开）",
            value=setting.friend_verify_code,
        )

        # 构建提示信息
        tips = ft.Text(
            value=(
                "1. 开启，则有人加好友，默认延迟5秒自动通过审核（手机必须开启好友验证）\n"
                "2. 关闭，则不会自动通过。\n"
                "3. 延迟时间（秒），在设置的时间内随机，默认为5秒\n"
                "4. 暗号：设置关键词，多个用英文逗号隔开，被加好友时，备注必须含暗号关键词，才能自动通过。"
            ),
            size=20,
        )

        # 构建弹窗内容
        dialog = ft.AlertDialog(
            title=ft.Row(
                controls=[
                    ft.Text("好友申请 - ", weight="bold"),
                    ft.Text("自动审核", weight="bold"),
                ]
            ),
            content=ft.Column(
                controls=[
                    tips,
                    ft.Row(
                        controls=[
                            ft.Text("功能开关："),
                            self.friend_review_switch,
                        ],
                        alignment=ft.MainAxisAlignment.START,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    self.friend_review_delay,
                    self.friend_review_code,
                ],
                spacing=10,
            ),
            actions=[
                ft.TextButton(
                    text="取消",
                    on_click=lambda e: self.close_dialog(e),
                ),
                ft.TextButton(
                    text="保存",
                    on_click=lambda e: self.save_friend_review(e),
                ),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        self.controller.page.dialog = dialog
        dialog.open = True
        self.controller.page.update()

    def close_dialog(self, e):
        self.controller.page.dialog.open = False
        self.controller.page.update()

    def save_friend_review(self, e):
        # 获取用户设置
        friend_verify = int(self.friend_review_switch.value)
        friend_verify_delay = (
            int(self.friend_review_delay.value)
            if self.friend_review_delay.value.isdigit()
            else 5
        )
        friend_verify_code = self.friend_review_code.value
        # 更新数据库
        SettingCRUD.update_setting(
            update_data={
                "friend_verify": friend_verify,
                "friend_verify_delay": friend_verify_delay,
                "friend_verify_code": friend_verify_code,
            }
        )
        # 关闭弹窗
        self.close_dialog(e)

    # 添加好友欢迎语弹窗方法
    def friend_welcome(self):
        # 从数据库获取初始化数据
        setting = SettingCRUD.get_setting()
        self.friend_welcome_textfield.value = (
            setting.friend_verify_welcome or "欢迎 [name] 加入！"
        )

        # 构建弹窗内容
        dialog = ft.AlertDialog(
            title=ft.Text("好友欢迎语设置", weight="bold", size=20),
            content=ft.Column(
                controls=[
                    ft.Text("请输入好友欢迎语：", size=20),
                    self.friend_welcome_textfield,
                    ft.Text("提示：可以使用占位符 [name] 表示好友昵称。", size=20),
                ],
                spacing=10,
            ),
            actions=[
                ft.TextButton(
                    text="取消",
                    on_click=lambda e: self.close_dialog(e),
                ),
                ft.TextButton(
                    text="保存",
                    on_click=lambda e: self.save_friend_welcome(e),
                ),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        self.controller.page.dialog = dialog
        dialog.open = True
        self.controller.page.update()

    # 保存好友欢迎语设置
    def save_friend_welcome(self, e):
        # 获取用户输入
        friend_welcome_text = self.friend_welcome_textfield.value
        # 更新数据库
        SettingCRUD.update_setting(
            update_data={
                "friend_verify_welcome": friend_welcome_text,
            }
        )
        # 关闭弹窗
        self.close_dialog(e)

    def private_chat_switch(self):
        # 获取当前设置
        setting = SettingCRUD.get_setting()
        self.private_chat_switch_control = ft.Switch(value=bool(setting.private_chat_enabled))
        
        # 构建弹窗内容
        dialog = ft.AlertDialog(
            title=ft.Text("私聊总开关"),
            content=ft.Column(
                controls=[
                    ft.Text("开启或关闭私聊功能："),
                    self.private_chat_switch_control,
                ],
            ),
            actions=[
                ft.TextButton("取消", on_click=self.close_dialog),
                ft.TextButton("保存", on_click=self.save_private_chat_switch),
            ],
        )
        self.controller.page.dialog = dialog
        dialog.open = True
        self.controller.page.update()

    def save_private_chat_switch(self, e):
        # 更新数据库
        private_chat_enabled = int(self.private_chat_switch_control.value)
        SettingCRUD.update_setting(update_data={"private_chat_enabled": private_chat_enabled})
        self.close_dialog(e)

    def private_chat_library(self):
        # 实现私聊词库的界面和功能
        # 示例：显示私聊词库的设置界面
        dialog = ft.AlertDialog(
            title=ft.Text("私聊词库"),
            content=ft.Text("这里是私聊词库的设置界面"),
            actions=[
                ft.TextButton("关闭", on_click=self.close_dialog),
            ],
        )
        self.controller.page.dialog = dialog
        dialog.open = True
        self.controller.page.update()
    
    def invite_group(self):
        # 实现邀请进群的界面和功能
        dialog = ft.AlertDialog(
            title=ft.Text("邀请进群"),
            content=ft.Text("这里是邀请进群的设置界面"),
            actions=[
                ft.TextButton("关闭", on_click=self.close_dialog),
            ],
        )
        self.controller.page.dialog = dialog
        dialog.open = True
        self.controller.page.update()
    def private_chat_settings(self):
        # 实现私聊设置的界面和功能
        dialog = ft.AlertDialog(
            title=ft.Text("私聊设置"),
            content=ft.Text("这里是私聊设置的界面"),
            actions=[
                ft.TextButton("关闭", on_click=self.close_dialog),
            ],
        )
        self.controller.page.dialog = dialog
        dialog.open = True
        self.controller.page.update()