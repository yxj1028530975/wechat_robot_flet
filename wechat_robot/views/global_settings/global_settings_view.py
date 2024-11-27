import flet as ft


class GlobalSettingsView:
    def __init__(self, controller):
        self.controller = controller
        # self.view_pull_wechat_list = view_pull_wechat_list

        self.data_list = [
            {
                "name": "全局设置",
                "id": 1,
                "icon_list": [
                    {"name": "智能聊天", "id": 11, "path": "/ai_chat", "icon":"WINDOW_OUTLINED"},
                    {"name": "本地词库", "id": 12, "path": "/local_library", "icon":"WINDOW_OUTLINED"},
                    {"name": "防封设置", "id": 13, "path": "/anti_seal", "icon":"WINDOW_OUTLINED"},
                    {"name": "软件定时", "id": 14, "path": "/software_timing", "icon":"WINDOW_OUTLINED"},
                ],
            },
            {
                "name": "群管设置",
                "id": 2,
                "icon_list": [
                    {"name": "群聊总开关", "id": 21, "path": "/ai_chat", "icon":"WINDOW_OUTLINED"},
                    {"name": "分群词库", "id": 22, "path": "/local_library", "icon":"WINDOW_OUTLINED"},
                    {"name": "群欢迎语", "id": 23, "path": "/anti_seal", "icon":"WINDOW_OUTLINED"},
                    {"name": "自动进群", "id": 24, "path": "/auto_join_group", "icon":"WINDOW_OUTLINED"},
                    {"name": "群黑名单", "id": 25, "path": "/group_blacklist", "icon":"WINDOW_OUTLINED"},
                    {"name": "群聊设置", "id": 26, "path": "/group_chat_settings", "icon":"WINDOW_OUTLINED"},
                    {"name": "更新功能", "id": 27, "path": "/update_function", "icon":"WINDOW_OUTLINED"},
                ],
            },
            {
                "name": "群管设置",
                "id": 3,
                "icon_list": [
                    {"name": "私聊总开关", "id": 31, "path": "/chat_switch", "icon":"WINDOW_OUTLINED"},
                    {"name": "私聊词库", "id": 32, "path": "/private_chat_library", "icon":"WINDOW_OUTLINED"},
                    {"name": "友欢迎语", "id": 33, "path": "/friend_welcome", "icon":"WINDOW_OUTLINED"},
                    {"name": "邀请进群", "id": 34, "path": "/invite_group", "icon":"WINDOW_OUTLINED"},
                    {"name": "好友进群", "id": 35, "path": "/friend_join_group", "icon":"WINDOW_OUTLINED"},
                    {"name": "私聊设置", "id": 36, "path": "/feed_settings", "icon":"WINDOW_OUTLINED"},
                    {"name": "更新昵称", "id": 37, "path": "/update_nickname", "icon":"WINDOW_OUTLINED"},
                ],
            },
        ]
    def build(self):
        return ft.Container(
            content=ft.Column(
                controls=[
                    self.build_container(),
                ],
                scroll="auto",  # 添加垂直滚动
            ),
        )

    # 构建页面
    def build_container(self):
        ft_column = ft.Column(controls=[], spacing=20)
        for data in self.data_list:
            ft_title = self.global_settings_title(data['name'])
            ft_app_list = self.global_settings_app_list(data['icon_list'])
            ft_column.controls.append(ft_title)
            ft_column.controls.append(ft_app_list)
        return ft.Container(
            content=ft_column,
        )
            
    # 标题
    def global_settings_title(self, title):
        return ft.Column(
            controls=[
                ft.Text(title, size=20, weight="bold"),
                ft.Container(
                    height=1,
                    bgcolor=ft.colors.BLACK,
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
            scroll="auto",  # 添加水平滚动
        )
        for app in data:
            ft_row.controls.append(self.global_settings_app(app))
        return ft.Container(
            content=ft_row,
        )
            
    # 单个应用
    def global_settings_app(self, data):
        ft_icon = ft.Icon(name=getattr(ft.icons, data['icon']), size=50)
        ft_text = ft.Text(data['name'], size=16)
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft_icon,
                    ft_text,
                ],
                alignment=ft.MainAxisAlignment.CENTER,          # 垂直居中
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # 水平居中
            ),
            width=120,
            height=120,
            padding=10,
            border=ft.border.all(1, ft.colors.GREY),
            border_radius=ft.border_radius.all(8),
            alignment=ft.alignment.center,  # 容器居中
            # on_click=lambda e: self.controller.navigate_to(data['path']),  # 添加点击事件
        )
