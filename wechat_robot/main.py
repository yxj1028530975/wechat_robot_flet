import flet as ft
from wechat_robot.controllers.login_controller import LoginController
from wechat_robot.controllers.signup_controller import SignUpController
from wechat_robot.controllers.main_controller import MainController
from wechat_robot.controllers.load_controller import LoadController
from wechat_robot.models.db_manager import Base, engine

# 打包命令
# pyinstaller --onefile --windowed     --add-data "config/config.toml;config"     --add-data "assets;assets"     main.py

# 创建所有表
Base.metadata.create_all(bind=engine)


class App:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.window.center()
        self.route_to_controller = {
            "/": LoginController,
            "/signup": SignUpController,
            "/load": LoadController,
            "/main": MainController,
            # ... other routes ...
        }
        self.history = []  
        self.navigate("/")

    def navigate(self, route):
        if route in self.route_to_controller:
            self.history.append(route)
            controller_class = self.route_to_controller[route]
            controller = controller_class(self.page, self)
            print(route)
        else:
            print("Route not found:", route)
        
        self.history.append(route)

    def go_back(self, event):  
        if len(self.history) > 1:
            self.history.pop()  
            previous_route = self.history[-1]
            self.navigate(previous_route)
            
        else:
            print("No previous page in history")
