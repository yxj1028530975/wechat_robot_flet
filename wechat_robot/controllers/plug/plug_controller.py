import flet as ft
from wechat_robot.views.plug.plug_view import PlugView
from wechat_robot.utils.wechat_http_interface import wechat_api    
from wechat_robot.models.fun_model import FunCRUD
class PlugController:
    def __init__(self, page: ft.Page):
        self.page = page
        self.init_plug_list()
        self.plug_view = PlugView(self)
        
        
    # 初始化插件列表
    def init_plug_list(self):
        try:
            # TODO 获取插件列表 暂时使用假数据
            pull_data = [
                {
                    "fun_id": 1,
                    "fun_name": "腾讯新闻",
                    "icon": "BUILD",
                    "status": 1,
                    "trigger_keyword": "腾讯新闻",
                    "description": "腾讯新闻插件，可以查看腾讯新闻",
                    "trigger_type": 1,
                    "code": '''
# 功能代码示例：获取新闻信息
search_name = user_input.strip()
if search_name:
    base_url = "http://api.livetools.top"
    news_dict = {
        "腾讯新闻": "/general_api/qq-news?limit=10",
        "新浪新闻": "/general_api/sina-news?limit=10",
        "网易新闻": "/general_api/netease-news?limit=10",
        "今日头条": "/general_api/toutiao?limit=10",
    }
    if search_name in news_dict:
        url = f'{base_url}{news_dict[search_name]}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data.get("code") == 200 and data.get("data"):
                return_data = data.get('data')
                title = data.get("title", search_name)
                return_new_data = f"【{title}】\\n"
                for news in return_data:
                    return_new_data += f"{news.get('title')}\\n{news.get('url')}\\n"
                wechat_api.send_wechat_msg(wx_id, return_new_data)
            else:
                print("未找到相关的新闻信息")
        else:
            print("请求新闻信息失败")
    else:
        print("请输入正确的新闻名称，如：腾讯新闻、新浪新闻、网易新闻、今日头条")
else:
    print("请输入要查询的新闻名称")
'''
                },{
                    "fun_id": 2,
                    "fun_name": "网易新闻",
                    "icon": "BUILD",
                    "status": 1,
                    "trigger_keyword": "网易新闻",
                    "description": "网易新闻插件，可以查看网易新闻",
                    "trigger_type": 1,
                    "code": '''
# 功能代码示例：获取新闻信息
search_name = user_input.strip()
if search_name:
    base_url = "http://api.livetools.top"
    news_dict = {
        "腾讯新闻": "/general_api/qq-news?limit=10",
        "新浪新闻": "/general_api/sina-news?limit=10",
        "网易新闻": "/general_api/netease-news?limit=10",
        "今日头条": "/general_api/toutiao?limit=10",
    }
    if search_name in news_dict:
        url = f'{base_url}{news_dict[search_name]}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data.get("code") == 200 and data.get("data"):
                return_data = data.get('data')
                title = data.get("title", search_name)
                return_new_data = f"【{title}】\\n"
                for news in return_data:
                    return_new_data += f"{news.get('title')}\\n"
                    # return_new_data += f"{news.get('title')}\\n{news.get('url')}\\n"
                wechat_api.send_wechat_msg(wx_id, return_new_data)
            else:
                print("未找到相关的新闻信息")
        else:
            print("请求新闻信息失败")
    else:
        print("请输入正确的新闻名称，如：腾讯新闻、新浪新闻、网易新闻、今日头条")
else:
    print("请输入要查询的新闻名称")
'''
                },{
                    "fun_id": 3,
                    "fun_name": "今日头条",
                    "icon": "BUILD",
                    "status": 1,
                    "trigger_keyword": "今日头条",
                    "description": "今日头条插件，可以查看今日头条",
                    "trigger_type": 1,
                    "code": '''
# 功能代码示例：获取新闻信息
search_name = user_input.strip()
if search_name:
    base_url = "http://api.livetools.top"
    news_dict = {
        "腾讯新闻": "/general_api/qq-news?limit=10",
        "新浪新闻": "/general_api/sina-news?limit=10",
        "网易新闻": "/general_api/netease-news?limit=10",
        "今日头条": "/general_api/toutiao?limit=10",
    }
    if search_name in news_dict:
        url = f'{base_url}{news_dict[search_name]}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data.get("code") == 200 and data.get("data"):
                return_data = data.get('data')
                title = data.get("title", search_name)
                return_new_data = f"【{title}】\\n"
                for news in return_data:
                    return_new_data += f"{news.get('title')}\\n{news.get('url')}\\n"
                wechat_api.send_wechat_msg(wx_id, return_new_data)
            else:
                print("未找到相关的新闻信息")
        else:
            print("请求新闻信息失败")
    else:
        print("请输入正确的新闻名称，如：腾讯新闻、新浪新闻、网易新闻、今日头条")
else:
    print("请输入要查询的新闻名称")
'''
                },{
                    "fun_id": 4,
                    "fun_name": "新浪新闻",
                    "icon": "BUILD",
                    "status": 1,
                    "trigger_keyword": "新浪新闻",
                    "description": "新浪新闻插件，可以查看新浪新闻",
                    "trigger_type": 1,
                    "code": '''
# 功能代码示例：获取新闻信息
search_name = user_input.strip()
if search_name:
    base_url = "http://api.livetools.top"
    news_dict = {
        "腾讯新闻": "/general_api/qq-news?limit=10",
        "新浪新闻": "/general_api/sina-news?limit=10",
        "网易新闻": "/general_api/netease-news?limit=10",
        "今日头条": "/general_api/toutiao?limit=10",
    }
    if search_name in news_dict:
        url = f'{base_url}{news_dict[search_name]}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data.get("code") == 200 and data.get("data"):
                return_data = data.get('data')
                title = data.get("title", search_name)
                return_new_data = f"【{title}】\\n"
                for news in return_data:
                    return_new_data += f"{news.get('title')}\\n{news.get('url')}\\n"
                wechat_api.send_wechat_msg(wx_id, return_new_data)
            else:
                print("未找到相关的新闻信息")
        else:
            print("请求新闻信息失败")
    else:
        print("请输入正确的新闻名称，如：腾讯新闻、新浪新闻、网易新闻、今日头条")
else:
    print("请输入要查询的新闻名称")
'''
                },{
                    "fun_id": 5,
                    "fun_name": "点歌(qq音乐)",
                    "icon": "BUILD",
                    "status": 1,
                    "trigger_keyword": "点歌",
                    "description": "点歌插件，可以点歌qq音乐",
                    "trigger_type": 2,
                    "code": '''
# 获取点歌内容
search_name = content[2:]
if search_name:
    base_url = "http://api.livetools.top"
    url = f'{base_url}/music_api/get_qq_song_info?name={search_name}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data.get("code") == 200 and data.get("data"):
            return_data = data['data'][0]
            if return_data:
                title = return_data["name"]
                des = return_data["singer"]
                png = return_data["image_url"] if return_data["image_url"] else "https://y.qq.com/favicon.ico?max_age=2592000"
                mp3 = return_data["download_url"]
                web =  "https://y.qq.com/n/ryqq/songDetail"
                var_list = [wx_id, title, des, png, mp3, web]
                # 检测有没有变量为None的，这会导致微信崩溃
                xml_strs = f'<msg><appmsg appid="" sdkver="0"><title>{title}</title><des>{des}</des><action>view</action><type>76</type><url>{web}</url><lowurl>{web}</lowurl><dataurl>{mp3}</dataurl><lowdataurl>{mp3}</lowdataurl><thumburl>{png}</thumburl><songalbumurl>{png}</songalbumurl><songlyric><![CDATA[null]]></songlyric><androidsource>3</androidsource><statextstr>GhQKEnd4OGRkNmVjZDgxOTA2ZmQ4NA==</statextstr></appmsg><fromusername>{my_wxid}</fromusername><appinfo><version></version><appname></appname></appinfo></msg>'
                print(xml_strs)
                wechat_api.api_send_xml_message(wx_id=wx_id,xml_str=xml_strs)
'''
                },
            ]
            # 增加功能列表输出
            """
                🌟 **功能状态概览** 🌟
            𝟬𝟭 > [原神功能]  𝟬𝟮 > [王者功能]
            𝟬𝟯 > [活跃统计]  𝟬𝟰 > [智能聊天]
            𝟬𝟱 > [画画功能]  𝟬𝟲 > [赛博算命]
            𝟬𝟳 > [语音功能]  𝟬𝟴 > [音乐视频]
            𝟬𝟵 > [签到功能]  𝟭𝟬 > [游戏功能]
            𝟭𝟭 > [其他功能]  𝟭𝟮 > [开关功能]
            """
            
            # self.plugins_data = [
            #     {"name": "腾讯新闻", "icon": "BUILD", "enabled": False},
            #     {"name": "网易新闻", "icon": "SETTINGS", "enabled": True},
            #     {"name": "新浪新闻", "icon": "SETTINGS", "enabled": True},
            #     {"name": "今日头条", "icon": "SETTINGS", "enabled": True},
            # ]
            plugins_data = []
            # 将数据库的内容覆盖
            FunCRUD.delete_all_fun()
            for data in pull_data:
                FunCRUD.add_fun(data)
                plugins_data.append({
                    "name": data["fun_name"],
                    "icon": data["icon"],
                    "enabled": bool(data["status"])
                })
            self.plugins_data = plugins_data

            
            
            
            
        except Exception as e:
            self.show_error_message(f"获取插件列表失败: {str(e)}")
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