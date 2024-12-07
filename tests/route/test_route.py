import flet as ft

def main(page: ft.Page):
    page.bgcolor = ft.colors.BLUE_200
    page.padding = 0
    background = ft.Container(
        width=1280,
        height=720,
        content=ft.Stack(
            [
                ft.Image(
                    src="img/background.jpg",  # 背景图片路径
                    width=1280,
                    height=720,
                    fit=ft.ImageFit.COVER,
                ),
                ft.Column(
                    [
                        ft.Text("正在加载中...", size=24, color=ft.colors.WHITE),
                        # 增加一个按钮测试
                        ft.CupertinoButton(
                            content=ft.Text("启动微信", color=ft.colors.YELLOW),
                            bgcolor=ft.colors.PRIMARY,
                            alignment=ft.alignment.top_left,
                            border_radius=ft.border_radius.all(15),
                            opacity_on_click=0.5,
                            # on_click=lambda e: self.controller.load_start_wechat(),
                        ),

                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
            ],alignment=ft.alignment.center, 
        ),bgcolor=ft.colors.BLUE_200,padding=0
    )
    
    page.add(background)
    # page.add(ft.Text(f"Initial route: {page.route}"))

    # def route_change(e: ft.RouteChangeEvent):
    #     page.add(ft.Text(f"New route: {e.route}"))

    # page.on_route_change = route_change
    page.update()
    

    

ft.app(target=main, view=ft.AppView.FLET_APP,assets_dir="../../assets")