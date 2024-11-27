import flet as ft
from wechat_robot.views.plug.plug_view import PlugView
from wechat_robot.utils.wechat_http_interface import wechat_api    

class PlugController:
    def __init__(self, page: ft.Page):
        self.page = page
        self.plug_view = PlugView(self)