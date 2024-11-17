import flet as ft

def main(page: ft.Page):
    page.add(ft.Text(f"Initial route: {page.route}"))

    def route_change(e: ft.RouteChangeEvent):
        page.add(ft.Text(f"New route: {e.route}"))

    page.on_route_change = route_change
    page.update()

ft.app(main, view=ft.AppView.WEB_BROWSER)