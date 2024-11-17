import flet as ft
from wechat_robot.views.main_view import MainView
from wechat_robot.views.group.group_view import GroupView
from wechat_robot.utils.wechat_http_interface import pull_wechat_list,pull_wechat_list_members

class MainController:
    def __init__(self, page: ft.Page,app):
        self.page = page
        self.app = app
        self.group_id = ''
        self.group_name = ''
        self.group_list = self.init_wechat_list()
        self.group_view = GroupView(self)
        self.main_view = MainView(page, self)
        self.page.add(self.main_view.build())
        self.switch_navigation_rail(-1, 0)  # 初始索引设为 -1，当前索引为 0
        self.page.update()
         

    # 切换导航栏展示
    def switch_navigation_rail(self, old_index, index):
        if old_index == index:
            return
        print("切换导航栏展示", index)
        if index == 0:
            self.main_view.update_content(self.group_view.build())
        else:
            self.main_view.update_content(ft.Text("其他内容"))
        self.page.update()

    # 获取微信列表
    def view_pull_wechat_list(self):
        return_data = pull_wechat_list(2)
        self.group_list = return_data['data']['list']
        self.update_group_list(return_data['data']['list'])
        
    # 更新群列表视图
    def update_group_list(self, group_list):
        self.group_view.group_list = group_list
        self.group_view.ft_lv.controls.clear()
        for index, group in enumerate(group_list):
            self.group_view.ft_lv.controls.append(
                self.group_view.group_list_data_line(group,index)
            )
        self.group_view.ft_lv.update()

    # 群列表点击事件处理函数
    def on_click_group_list(self,ft_group_list_data_line,data):
        if self.group_view.selected_row and self.group_view.selected_row != ft_group_list_data_line:
            if self.group_view.selected_row in self.group_view.ft_lv.controls:
                self.group_view.selected_row.bgcolor = None
                self.group_view.selected_row.update()
        self.group_view.selected_row = ft_group_list_data_line
        ft_group_list_data_line.bgcolor = ft.colors.BLUE_GREY_100
        self.group_view.ft_lv.update()
        self.group_view.selected_row = ft_group_list_data_line
        self.update_group_members(data['wx_id'], data['nick_name'])
    
    
    # 初始化微信列表
    def init_wechat_list(self):
        return_data = pull_wechat_list(2)
        return return_data['data']['list']
    
    # 查找功能，模糊匹配群名称，如果为空则显示全部
    def search_wechat_list(self, keyword):
        if keyword:
            # 过滤群列表
            new_group_list = [group for group in self.group_list if keyword in group['nick_name']]
        else:
            new_group_list = self.group_list
        # 更新群列表视图
        self.update_group_list(new_group_list)
    
    
    # 更新群成员列表
    def update_group_members(self, group_id, group_name):
        self.group_id = group_id
        self.group_name = group_name
        return_data = pull_wechat_list_members(group_id)
        # 获取群成员数据（假设有对应的接口方法）
        members = return_data['data']['list']
        self.group_view.group_member_text.value = f"[群名称:{self.group_name}]"
        self.group_view.group_member_text.update()
        # 更新群成员视图
        self.update_group_members_list(members)
    # 更新群列表视图
    def update_group_members_list(self, members):
        self.group_view.member_list = members
        self.group_view.ft_lv_member_list.controls.clear()
        for index, group in enumerate(members):
            self.group_view.ft_lv_member_list.controls.append(
                self.group_view.group_member_data_line(group,index)
            )
        self.group_view.ft_lv_member_list.update()