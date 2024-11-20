# filepath: /d:/gr_project/wechat_robot_flet/wechat_robot/controllers/main/group_setting_controller.py
import flet as ft
from wechat_robot.views.group.group_setting_view import GroupSettingView
from wechat_robot.models.group_model import GroupCRUD
from wechat_robot.utils.config_utils import get_config
class GroupSettingController:
    def __init__(self, page: ft.Page, group_id: str, group_name: str):
        self.page = page
        self.group_id = group_id
        self.group_name = group_name
        self.out_setting = ''
        self.welcome_setting = ''
        self.fun_setting = ''
        self.out_setting_tip = get_config("group_template", "out_setting_tip")
        self.welcome_setting_tip = get_config("group_template", "welcome_setting_tip")
        self.fun_setting_tip = get_config("group_template", "fun_setting_tip")
        self.out_setting_template = get_config("group_template", "out_setting")
        self.welcome_setting_template = get_config("group_template", "welcome_setting")
        self.fun_setting_template = get_config("group_template", "fun_setting")
        self.init_data()
        self.group_setting_view = GroupSettingView(self, self.page)
    
    def go_back(self, e):
        if len(self.page.views) > 1:
            self.page.views.pop()
            self.page.go(self.page.views[-1].route)
    
    # 初始化数据
    def init_data(self):
        if existing_group := GroupCRUD.get_group_by_id(self.group_id):
            self.out_setting = existing_group.out_setting
            self.welcome_setting = existing_group.welcome_setting
            self.fun_setting = existing_group.fun_setting
        else:
            data = {
                'group_id': self.group_id,
                'group_name': self.group_name,
                'out_setting': self.out_setting,
                'welcome_setting': self.welcome_setting,
                'fun_setting': self.fun_setting,
            }
            GroupCRUD.add_group(data)
    # 保存群设置
    def save_group_setting(self):
        group_data = {
            'group_id': self.group_id,
            'group_name': self.group_name,
            'out_setting': self.group_setting_view.tf_out_group_setting.content.controls[0].content.controls[1].value,
            'welcome_setting': self.group_setting_view.tf_welcome_group_setting.content.controls[0].content.controls[1].value,
            'fun_setting': self.group_setting_view.tf_fun_group_setting.content.controls[0].content.controls[1].value,
        }
        GroupCRUD.update_group(self.group_id, group_data)
        self.group_setting_view.show_success()
        