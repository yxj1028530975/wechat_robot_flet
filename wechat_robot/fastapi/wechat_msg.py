# 微信消息处理逻辑
from wechat_robot.models.group_model import GroupCRUD
from wechat_robot.utils.wechat_http_interface import send_wechat_msg,search_wxid_info
from wechat_robot.utils.config_utils import get_config



# 处理微信消息入口
def wechat_msg_handle(data):
    if data.get("msg_type") == 10000 and "邀请" in data.get("content") and data.get("type") ==100:
        # 进群提醒
        welcome_msg_handle(data)
    if data.get("type") == 444:
        # 退群提醒
        out_group_msg_handle(data)



# 进群欢迎语处理
def welcome_msg_handle(data):
    # 获取群组信息
    # {'at_list': [], 'content': '"木不易成楊！"邀请"月光"加入了群聊', 'file_path': 'D:\\wechatFile\\WeChat Files\\', 'is_pc_msg': 0, 'is_self_msg': 0, 'local_id': '53089', 'msg_id': '1779041963595470200', 'msg_type': 10000, 'port': 30001, 'self_wx_id': 'wxid_tjlscvvc60a022', 'sender': '', 'time_stamp': 1732089882, 'type': 100, 'wx_id': '34901437633@chatroom'}
    group_id = data["wx_id"]
    name = data["content"].split('"')[3]
    inviter = data["content"].split('"')[1]
    if group := GroupCRUD.get_group_by_id(group_id):
        welcome_setting = group.welcome_setting
        welcome_setting = welcome_setting
    else:
        welcome_setting = get_config("group_template", "welcome_setting")
    welcome_setting = welcome_setting.replace("[name]",name).replace("[inviter]",inviter)
    send_wechat_msg(data["wx_id"],welcome_setting)
    
# 退群事件处理
def out_group_msg_handle(data):
    # 获取退群人，只获取第一个
    if data['member_list']:
        wx_id = data['member_list'][0]['wx_id']
        # {'chat_room_id': '51740029844@chatroom', 'member_list': [{'room_name': '', 'wx_id': 'wxid_h0vq4b62izaj12'}], 'msg': '退群事件', 'port': 30001, 'self_wx_id': 'wxid_tjlscvvc60a022', 'type': 444}
        group_id = data["chat_room_id"]
        if return_data := search_wxid_info(wx_id):
            name = return_data['data']['nick_name']
            if group := GroupCRUD.get_group_by_id(group_id):
                out_setting = group.out_setting
            else:
                out_setting = get_config("group_template", "out_setting")
            out_setting = out_setting.replace('[name]',name)
            send_wechat_msg(group_id,out_setting)