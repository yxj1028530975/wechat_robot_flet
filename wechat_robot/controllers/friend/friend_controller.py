import flet as ft
from wechat_robot.models.friend_model import FriendCRUD
from wechat_robot.views.friend.friend_view import FriendView
from wechat_robot.utils.wechat_http_interface import wechat_api    

class FriendController:
    def __init__(self, page: ft.Page):
        self.page = page
        self.friend_crud = FriendCRUD()
        self.friend_list = self.init_friend_list()
        self.friend_view = FriendView(self)
        
    def init_friend_list(self):
        try:
            # 获取微信好友列表
            return_data = wechat_api.pull_wechat_list(1)
            if not return_data:
                self.show_error_message("未能获取到好友列表，可能是微信掉线或请求失败。请重启软件登录微信")
                return []
            # 获取本地数据库中的好友
            local_friends = self.friend_crud.get_all_friend()
            local_friend_dict = {friend.friend_id: friend for friend in local_friends}

            # 处理微信返回的好友列表
            friends_data = return_data.get('data', {}).get('list', [])
            return_data_list = []
            for friend in friends_data:
                friend_id = friend['wx_id']
                friend_name = friend['nick_name']
                if friend_id in local_friend_dict:
                    # 如果好友在本地数据库中，使用本地数据库的内容为主，增加状态字段
                    local_friend = local_friend_dict[friend_id]
                    friend_data = {
                        'wx_id': friend_id,
                        'nick_name': friend_name,
                        'status': local_friend.status or '开启'  # 默认为开启
                    }
                else:
                    # 如果好友不在本地数据库中，添加它，状态默认为开启
                    friend_data = {
                        'wx_id': friend_id,
                        'nick_name': friend_name,
                        'status': '开启'  # 默认为开启
                    }
                return_data_list.append(friend_data)

            return return_data_list

        except Exception as e:
            self.show_error_message(f"获取好友列表失败: {str(e)}")
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
    
    def on_click_friend_list(self, ft_friend_list_data_line, data):
        if self.friend_view.selected_row and self.friend_view.selected_row != ft_friend_list_data_line:
            if self.friend_view.selected_row in self.friend_view.ft_lv.controls:
                self.friend_view.selected_row.bgcolor = None
                self.friend_view.selected_row.update()
        self.friend_view.selected_row = ft_friend_list_data_line
        ft_friend_list_data_line.bgcolor = ft.colors.BLUE_GREY_100
        self.friend_view.ft_lv.update()
        self.friend_view.selected_row = ft_friend_list_data_line