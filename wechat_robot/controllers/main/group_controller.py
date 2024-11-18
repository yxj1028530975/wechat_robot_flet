# filepath: /d:/gr_project/wechat_robot_flet/wechat_robot/controllers/main_group_controller.py
import flet as ft
from wechat_robot.views.group.group_view import GroupView
from wechat_robot.utils.wechat_http_interface import pull_wechat_list, pull_wechat_list_members
from wechat_robot.controllers.main.group_setting_controller import GroupSettingController

class GroupController:
    def __init__(self, page: ft.Page):
        self.page = page
        self.group_list = self.init_wechat_list()
        self.group_view = GroupView(self)
        self.group_setting_view = GroupSettingController(self.page,self.group_view.group_id,self.group_view.group_name).group_setting_view.build()
        # self.page.add(self.group_view.build())

    def init_wechat_list(self):
        return_data = pull_wechat_list(2)
        return return_data['data']['list']

    def view_pull_wechat_list(self):
        return_data = pull_wechat_list(2)
        self.group_list = return_data['data']['list']
        self.update_group_list(return_data['data']['list'])

    def update_group_list(self, group_list):
        self.group_view.group_list = group_list
        self.group_view.ft_lv.controls.clear()
        for index, group in enumerate(group_list):
            self.group_view.ft_lv.controls.append(
                self.group_view.group_list_data_line(group, index)
            )
        self.group_view.ft_lv.update()

    def on_click_group_list(self, ft_group_list_data_line, data):
        if self.group_view.selected_row and self.group_view.selected_row != ft_group_list_data_line:
            if self.group_view.selected_row in self.group_view.ft_lv.controls:
                self.group_view.selected_row.bgcolor = None
                self.group_view.selected_row.update()
        self.group_view.selected_row = ft_group_list_data_line
        ft_group_list_data_line.bgcolor = ft.colors.BLUE_GREY_100
        self.group_view.ft_lv.update()
        self.group_view.selected_row = ft_group_list_data_line
        self.update_group_members(data['wx_id'], data['nick_name'])

    def search_wechat_list(self, keyword):
        if keyword:
            new_group_list = [group for group in self.group_list if keyword in group['nick_name']]
        else:
            new_group_list = self.group_list
        self.update_group_list(new_group_list)

    def update_group_members(self, group_id, group_name):
        self.group_view.group_id = group_id
        self.group_view.group_name = group_name
        return_data = pull_wechat_list_members(group_id)
        members = return_data['data']['list']
        self.group_view.group_member_text.value = f"[群名称:{group_name}]"
        self.group_view.group_member_text.update()
        self.update_group_members_list(members)

    def update_group_members_list(self, members):
        self.group_view.member_list = members
        self.group_view.ft_lv_member_list.controls.clear()
        for index, group in enumerate(members):
            self.group_view.ft_lv_member_list.controls.append(
                self.group_view.group_member_data_line(group, index)
            )
        self.group_view.ft_lv_member_list.update()


    def open_group_setting(self, ft_group_list_data_line, data):
        self.on_click_group_list(ft_group_list_data_line, data)
    # 从当前选中的群中获取参数，例如群ID和群名称
        group_id = self.group_view.group_id
        group_name = self.group_view.group_name
        # 创建 GroupSettingController，并传递参数
        group_setting_controller = GroupSettingController(self.page, group_id, group_name)
        # 创建新的视图
        new_view = ft.View(
            route="/group_setting",
            controls=[
                group_setting_controller.group_setting_view.build()
            ]
        )
        self.page.views.append(new_view)
        self.page.go("/group_setting")