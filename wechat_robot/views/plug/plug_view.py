import flet as ft


class PlugView:
    def __init__(self, controller):
        self.controller = controller
        self.plugins_data = self.controller.plugins_data

    def build(self):
        # 构建插件面板
        plugin_controls = []
        for plugin in self.plugins_data:
            switch = ft.Switch(value=plugin["enabled"], on_change=self.toggle_plugin)
            icon = ft.Icon(name=getattr(ft.icons, plugin["icon"]), size=40)
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
                    width=250,  # 设置固定宽度
                    alignment=ft.alignment.center_left,  # 内容左对齐
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
        # # 将所有插件控件添加到页面
        # return ft.Column(controls=plugin_controls)

    def toggle_plugin(self, e):
        # 插件开关的回调函数
        pass