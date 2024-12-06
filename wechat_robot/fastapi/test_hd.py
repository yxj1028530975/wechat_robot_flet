from wechat_robot.utils.wechat_http_interface import wechat_api
# 功能代码示例：获取新闻信息
wx_id = ''
requests = ''
wechat_api = ''
json = ''
content = ''
user_input = ''
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
                return_new_data = f"【{title}】\n"
                for news in return_data:
                    return_new_data += f"{news.get('title')}\n{news.get('url')}\n"
                wechat_api.send_wechat_msg(wx_id, return_new_data)
            else:
                print("未找到相关的新闻信息")
        else:
            print("请求新闻信息失败")
    else:
        print("请输入正确的新闻名称，如：腾讯新闻、新浪新闻、网易新闻、今日头条")
else:
    print("请输入要查询的新闻名称")
    
    



# 获取点歌内容

    
            