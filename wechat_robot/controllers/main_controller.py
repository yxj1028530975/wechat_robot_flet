import flet as ft
from wechat_robot.views.main_view import MainView
from wechat_robot.controllers.group.group_controller import GroupController
from wechat_robot.controllers.friend.friend_controller import FriendController
from wechat_robot.controllers.public_account.public_account_controller import PublicAccountController
from wechat_robot.controllers.global_settings.global_settings_controller import GlobalSettingsController
from wechat_robot.controllers.plug.plug_controller import PlugController

class MainController:
    def __init__(self, page: ft.Page,app):
        self.page = page
        self.app = app
        self.group_view = GroupController(self.page).group_view.build()
        self.friend_view = FriendController(self.page).friend_view.build()
        self.public_account_view = PublicAccountController(self.page).public_account_view.build()
        self.global_settings_view = GlobalSettingsController(self.page).global_settings_view.build()
        self.plug_view = PlugController(self.page).plug_view.build()
        # self.group_view = GroupView(self)
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
            self.main_view.update_content(self.group_view)
        elif index == 1:
            self.main_view.update_content(self.friend_view)
        elif index == 2:
            self.main_view.update_content(self.public_account_view)
        elif index == 3:
            self.main_view.update_content(self.global_settings_view)
        elif index == 4:
            self.main_view.update_content(self.plug_view)
        else:
            self.main_view.update_content(ft.Text("其他内容"))
        self.page.update()