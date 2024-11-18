import flet as ft
from wechat_robot.views.main_view import MainView
from wechat_robot.controllers.main.group_controller import GroupController

class MainController:
    def __init__(self, page: ft.Page,app):
        self.page = page
        self.app = app
        self.group_view = GroupController(self.page).group_view.build()
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
        else:
            self.main_view.update_content(ft.Text("其他内容"))
        self.page.update()