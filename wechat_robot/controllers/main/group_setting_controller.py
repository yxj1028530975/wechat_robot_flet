# filepath: /d:/gr_project/wechat_robot_flet/wechat_robot/controllers/main/group_setting_controller.py
import flet as ft
from wechat_robot.views.group.group_setting_view import GroupSettingView

class GroupSettingController:
    def __init__(self, page: ft.Page, group_id: str, group_name: str):
        self.page = page
        self.group_id = group_id
        self.group_name = group_name
        self.group_setting_view = GroupSettingView(self)
    
    def go_back(self, e):
        if len(self.page.views) > 1:
            self.page.views.pop()
            self.page.go(self.page.views[-1].route)