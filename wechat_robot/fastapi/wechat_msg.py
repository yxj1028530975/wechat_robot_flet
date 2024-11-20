# 微信消息处理逻辑
from wechat_robot.models.group_model import GroupCRUD
from wechat_robot.utils.wechat_http_interface import send_wechat_msg
from wechat_robot.utils.config_utils import get_config



# 处理微信消息入口
def wechat_msg_handle(data):
    if data.get("msg_type") == 10000 and "邀请" in data.get("content") and data.get("type") ==100:
        # 进群提醒
        welcome_msg_handle(data)



# 进群欢迎语处理
def welcome_msg_handle(data):
    # 获取群组信息
    # {'at_list': [], 'content': '"木不易成楊！"邀请"月光"加入了群聊', 'file_path': 'D:\\wechatFile\\WeChat Files\\', 'is_pc_msg': 0, 'is_self_msg': 0, 'local_id': '53089', 'msg_id': '1779041963595470200', 'msg_type': 10000, 'port': 30001, 'self_wx_id': 'wxid_tjlscvvc60a022', 'sender': '', 'time_stamp': 1732089882, 'type': 100, 'wx_id': '34901437633@chatroom'}
    group_id = data["wx_id"]
    name = data["content"].split('"')[1]
    inviter = data["content"].split('"')[3]
    if group := GroupCRUD.get_group_by_id(group_id):
        welcome_setting = group.welcome_setting
        welcome_setting = "\n你好\r你也好"
        print(welcome_setting)
        welcome_setting = welcome_setting.replace("[name]",name).replace("[inviter]",inviter)
        # 将\n\UE315 替换成换行符,发送给微信无法换行是
        
    else:
        welcome_setting = str(get_config("group_template", "welcome_setting").replace("[name]",name).replace("[inviter]",inviter).replace("\n","\n"))
    # welcome_setting = "\n你好\r你也好"

    send_wechat_msg(data["wx_id"],welcome_setting)