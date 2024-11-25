# filepath: /d:/gr_project/wechat_robot_flet/wechat_robot/controllers/main_group_controller.py
import flet as ft
from wechat_robot.models.group_model import GroupCRUD
from wechat_robot.views.group.group_view import GroupView
from wechat_robot.controllers.group.group_setting_controller import GroupSettingController
from wechat_robot.utils.wechat_http_interface import wechat_api

class GroupController:
    def __init__(self, page: ft.Page):
        self.page = page
        self.group_crud = GroupCRUD()
        self.group_list = self.init_wechat_list()
        self.group_view = GroupView(self)
        self.group_setting_view = None  # 初始化为 None

    def init_wechat_list(self):
        try:
            # 获取微信群列表
            return_data = wechat_api.pull_wechat_list(2)
            if not return_data:
                self.show_error_message("未能获取到群列表，可能是微信掉线或请求失败。请重启软件登录微信")
                return []

            # 获取本地数据库中的群组
            local_groups = self.group_crud.get_all_group()
            local_group_dict = {group.group_id: group for group in local_groups}

            # 处理微信返回的群列表
            groups_data = return_data.get('data', {}).get('list', [])
            return_data_list = []
            for group in groups_data:
                group_id = group['wx_id']
                group_name = group['nick_name']
                if group_id in local_group_dict:
                    # 如果群在本地数据库中，使用本地数据库的内容为主，增加状态字段
                    local_group = local_group_dict[group_id]
                    group_data = {
                        'wx_id': group_id,
                        'nick_name': group_name,
                        'status': local_group.status or '开启'  # 默认为开启
                    }
                else:
                    # 如果群不在本地数据库中，添加它，状态默认为开启
                    group_data = {
                        'wx_id': group_id,
                        'nick_name': group_name,
                        'status': '开启'  # 默认为开启
                    }
                return_data_list.append(group_data)

            return return_data_list

        except Exception as e:
            self.show_error_message(f"获取群列表失败: {str(e)}")
            return []

    def show_error_message(self, message: str):
        """显示错误消息对话框"""
        def close_dlg(e):
            dlg_modal.open = False
            self.page.update()

        dlg_modal = ft.AlertDialog(
            modal=True,
            title=ft.Text("错误"),
            content=ft.Text(message),
            actions=[
                ft.TextButton("确定", on_click=close_dlg),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        
        self.page.dialog = dlg_modal
        dlg_modal.open = True
        self.page.update()

    def close_dialog(self, e):
        e.control.parent.open = False
        self.page.update()

    def view_pull_wechat_list(self):
        return_data = wechat_api.pull_wechat_list(2)
        if not (return_data := wechat_api.pull_wechat_list(2)):
            self.show_error_message("未能获取到群列表，可能是微信掉线或请求失败。请重启软件登陆微信")
            return []
        # 获取本地数据库中的群组
        local_groups = self.group_crud.get_all_group()
        local_group_dict = {group.group_id: group for group in local_groups}

        # 处理微信返回的群列表
        groups_data = return_data.get('data', {}).get('list', [])
        return_data_list = []
        for group in groups_data:
            group_id = group['wx_id']
            group_name = group['nick_name']
            if group_id in local_group_dict:
                # 如果群在本地数据库中，使用本地数据库的内容为主，增加状态字段
                local_group = local_group_dict[group_id]
                group_data = {
                    'wx_id': group_id,
                    'nick_name': group_name,
                    'status': local_group.status or '开启'  # 默认为开启
                }
            else:
                # 如果群不在本地数据库中，添加它，状态默认为开启
                group_data = {
                    'wx_id': group_id,
                    'nick_name': group_name,
                    'status': '开启'  # 默认为开启
                }
            return_data_list.append(group_data)
        self.group_list = return_data_list
        self.update_group_list(return_data_list)

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
        return_data = wechat_api.pull_wechat_list_members(group_id)
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


    def open_group_setting(self):
            # self.on_click_group_list(ft_group_list_data_line, data)
        # 从当前选中的群中获取参数，例如群ID和群名称
            # 创建 GroupSettingController，并传递参数
            group_setting_controller = GroupSettingController(self.page, self.group_view.group_id, self.group_view.group_name)
            # 创建新的视图
            new_view = ft.View(
                route="/group_setting",
                controls=[
                    group_setting_controller.group_setting_view.build()
                ]
            )
            self.page.views.append(new_view)
            self.page.go("/group_setting")