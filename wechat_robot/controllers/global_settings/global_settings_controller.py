import flet as ft
from wechat_robot.views.global_settings.global_settings_view import GlobalSettingsView
from wechat_robot.utils.wechat_http_interface import wechat_api    

class GlobalSettingsController:
    def __init__(self, page: ft.Page):
        self.page = page
        self.global_settings_view = GlobalSettingsView(self)