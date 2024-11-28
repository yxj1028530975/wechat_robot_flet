import flet as ft


class PlugView:
    def __init__(self, controller):
        self.controller = controller

    def build(self):
        # 创建插件数据
        plugins_data = [
            {"name": "插件一", "icon": ft.icons.EXTENSION, "enabled": True},
            {"name": "插件二", "icon": ft.icons.BUILD, "enabled": False},
            {"name": "插件三", "icon": ft.icons.SETTINGS, "enabled": True},
            # 可以添加更多插件
        ]

        # 构建插件面板
        plugin_controls = []
        for plugin in plugins_data:
            switch = ft.Switch(value=plugin["enabled"], on_change=self.toggle_plugin)
            icon = ft.Icon(name=plugin["icon"], size=40)
            text = ft.Text(plugin["name"], size=16)
            plugin_controls.append(
                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Row(
                                controls=[icon, text],
                                spacing=10,
                                alignment=ft.MainAxisAlignment.START,
                            ),
                            switch,
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    padding=10,
                    border=ft.border.all(1, ft.colors.BLACK87),
                    border_radius=ft.border_radius.all(8),
                )
            )

        # 应用市场描述
        app_market_description = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text("应用市场", size=20, weight="bold"),
                    ft.Text("在这里您可以浏览和管理您的插件。", size=14),
                ],
                spacing=10,
                alignment=ft.MainAxisAlignment.START,
            ),
            padding=10,
            width=200,
        )

        # 构建界面布局
        return ft.Row(
            controls=[
                ft.Container(
                    content=ft.Column(
                        controls=plugin_controls,
                        spacing=10,
                        alignment=ft.MainAxisAlignment.START,
                    ),
                    expand=True,
                ),
                ft.VerticalDivider(),
                app_market_description,
            ],
            alignment=ft.MainAxisAlignment.START,
            expand=True,
        )

    def toggle_plugin(self, e):
        # 插件开关的回调函数
        pass