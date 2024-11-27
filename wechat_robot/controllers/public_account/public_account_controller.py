import flet as ft
from wechat_robot.views.public_account.public_account_view import PublicAccountView
from wechat_robot.utils.wechat_http_interface import wechat_api    

class PublicAccountController:
    def __init__(self, page: ft.Page):
        self.page = page
        self.public_account_list = self.init_public_account_list()
        self.public_account_view = PublicAccountView(self)
        
    def init_public_account_list(self):
        try:
            # 获取微信好友列表
            return_data = wechat_api.pull_wechat_list(3)
            if not return_data:
                self.show_error_message("未能获取到公众号列表，可能是微信掉线或请求失败。请重启软件登录微信")
                return []
            public_accounts_data = return_data.get('data', {}).get('list', [])
            return_data_list = []
            for public_account in public_accounts_data:
                public_account_id = public_account['wx_id']
                public_account_name = public_account['nick_name']
                public_account_data = {
                    'wx_id': public_account_id,
                    'nick_name': public_account_name,
                }
                return_data_list.append(public_account_data)
            return return_data_list

        except Exception as e:
            self.show_error_message(f"获取公众号列表失败: {str(e)}")
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
    
    def on_click_public_account_list(self, ft_public_account_list_data_line, data):
        if self.public_account_view.selected_row and self.public_account_view.selected_row != ft_public_account_list_data_line:
            if self.public_account_view.selected_row in self.public_account_view.ft_lv.controls:
                self.public_account_view.selected_row.bgcolor = None
                self.public_account_view.selected_row.update()
        self.public_account_view.selected_row = ft_public_account_list_data_line
        ft_public_account_list_data_line.bgcolor = ft.colors.BLUE_GREY_100
        self.public_account_view.ft_lv.update()
        self.public_account_view.selected_row = ft_public_account_list_data_line