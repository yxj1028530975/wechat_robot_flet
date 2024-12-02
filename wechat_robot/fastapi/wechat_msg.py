# 微信消息处理逻辑
from wechat_robot.models.group_model import GroupCRUD
from wechat_robot.models.robot_setting import SettingCRUD
from wechat_robot.utils.config_utils import get_config
from wechat_robot.utils.wechat_http_interface import wechat_api
from wechat_robot.fastapi.wechat_msg_handle import friend_request_xml_jx,chatroom_invite_xml_jx
import time

test_group_id = "51740029844@chatroom"

type = (
    [
        ("100", "消息"),
        ("333", "进群通知"),
        ("444", "退群通知"),
        ("1000", "微信进程结束通知"),
        ("999", "微信退出登录通知"),
        ("666", "撤回消息"),
    ],
)

msg_type = [
    ("0", "系统消息"),
    ("1", "文字"),
    ("3", "图片"),
    ("34", "语音"),
    ("36", "PC发送文件"),
    ("37", "好友请求"),
    ("40", "好友推荐"),
    ("42", "个人名片"),
    ("43", "视频消息"),
    ("44", "主动撤回"),
    ("47", "动画表情"),
    ("48", "位置"),
    ("49", "共享实时位置、等xml消息"),
    ("50", "VOIP"),
    ("51", "微信初始化"),
    ("52", "VOIP结束"),
    ("53", "VOIP邀请"),
    ("62", "小视频"),
    ("2000", "群通知"),
    ("9994", "联系人切换"),
    ("9996", "登录成功"),
    ("9997", "微信软件系统"),
    ("9998", "系统通知"),
    ("9999", "系统通知"),
    ("10000", "群通知"),
    ("10002", "撤回消息"),
]


# 处理微信消息入口
def wechat_msg_handle(data):
    msg_type = data.get("msg_type", "")
    sys_type = data.get("type", "")
    content = data.get("content", "")
    if msg_type == 37 and sys_type == 100:
        # 好友申请事件处理
        agree_friend_application_handle(data)
    elif msg_type == 10000 and "邀请你" in data.get("content") and sys_type == 100:
        # 邀请机器人进群提醒
        welcome_robot_msg_handle(data)
    
    elif msg_type == 10000 and "邀请" in data.get("content") and sys_type == 100:
        # 邀请进群提醒
        welcome_msg_handle(data)
    elif msg_type == 10000 and sys_type == 100 and "扫描" in content:
        # 扫码进群欢迎语处理
        scan_welcome_msg_handle(data)
    elif msg_type == 49 and sys_type == 100 and "邀请你加入群聊" in content:
        invite_group_handle(content)
    elif sys_type == 444:
        # 退群提醒
        out_group_msg_handle(data)


# 邀请进群欢迎语处理
def welcome_msg_handle(data):
    # 获取群组信息
    """ "
        {
        "at_list": [],
        "content": "\"木不易成楊！\"邀请\"月光\"加入了群聊",
        "file_path": "D:\\wechatFile\\WeChat Files\\",
        "is_pc_msg": 0,
        "is_self_msg": 0,
        "local_id": "53089",
        "msg_id": "1779041963595470200",
        "msg_type": 10000,
        "port": 30001,
        "self_wx_id": "wxid_tjlscvvc60a022",
        "sender": "",
        "time_stamp": 1732089882,
        "type": 100,
        "wx_id": "51740029844@chatroom"
    }
    """
    group_id = data["wx_id"]
    name = data["content"].split('"')[3]
    inviter = data["content"].split('"')[1]
    in_group_msg_common_handle(group_id, name, inviter)


# 扫码进群和分享二维码欢迎语处理
def scan_welcome_msg_handle(data):
    """
        {
        "at_list": [],
        "content": "\"风铃\"通过扫描\"爱如星火\"分享的二维码加入群聊",
        "file_path": "D:\\wechatFile\\WeChat Files\\",
        "is_pc_msg": 0,
        "is_self_msg": 0,
        "local_id": "67020",
        "msg_id": "7258048800291732532",
        "msg_type": 10000,
        "port": 30001,
        "self_wx_id": "wxid_tjlscvvc60a022",
        "sender": "",
        "time_stamp": 1733120962,
        "type": 100,
        "wx_id": "51740029844@chatroom"
    }
    """
    group_id = data["wx_id"]
    name = data["content"].split('"')[1]
    inviter = data["content"].split('"')[3]
    in_group_msg_common_handle(group_id, name, inviter)
# 邀请机器人加入群聊
def welcome_robot_msg_handle(data):
    """
    {
    "at_list": [],
    "content": "\"木不易成楊！\"邀请你加入了群聊，群聊参与人还有：神话-马拉松、COOK - 独立开发者、黎君、CHELSEA、利好、168888948、饼爷-自由、康先生短视频运营、Louwin、share、牛马--拧螺丝、广州-独立开发、任榆胭、小助理、ㅤ、GV、小助理、告白ai(有副业)、哈哈哈、Jungle、FF-工程、focus、Przeblysk、寧波小歪、灰灰、卌卝、chatgpt酱、龙谷情、haloer、析木-金融、Figo - 开发、Gzs、Mr李、多点关心，多点爱、Melon、ssnxs- ai爱好者、清风、℃、波波、李肄（yi）、夜思日行、CJ、天亮了、浩瀚人海、执著、阿敏、『超级会员』 、段超、陪衬、狸猫⃝发财版、！、冠鑫电子 庄贞武、chestnut、华～、🌈王老头有点甜、、简单。幸福、blue、摧花—体、CogitoErgoSum、欸艾、  薯条、Dylan、🇭-java、ty-自媒体、冷言、大海、🌍🗽观海听涛、阿四爱蓓蓓-金融、Mr  C、。、9527、idesign-ai设计师、铁蛋、宋你一朵小红 花🌺、夜望北辰、[微信紅包]恭喜发财，大吉大利！、广告业，视觉设计师、也-宏轩X🥜🥜、天地宽、風景綫＆、财运来-OPPO业务、室内矮人、哪吒、天涯未远  、irine tsou、红色石头（电商）、Bigbing、Danny、雨过天晴🍃、NULL.、X、初释衷年、鑫源-自媒体",
    "file_path": "D:\\wechatFile\\WeChat Files\\",
    "is_pc_msg": 0,
    "is_self_msg": 0,
    "local_id": "67103",
    "msg_id": "1262850250516318603",
    "msg_type": 10000,
    "port": 30001,
    "self_wx_id": "wxid_tjlscvvc60a022",
    "sender": "",
    "time_stamp": 1733126455,
    "type": 100,
    "wx_id": "51740029844@chatroom"
}
    """
    group_id = data["wx_id"]
    robot_setting = SettingCRUD.get_setting()
    name = robot_setting.wechat_name
    inviter = data["content"].split('"')[1]
    in_group_msg_common_handle(group_id, name, inviter)

# 进群消息相同部分提取
def in_group_msg_common_handle(group_id, name, inviter):
    group = GroupCRUD.get_group_by_id(group_id)
    if group and group.welcome_setting:
        welcome_setting = group.welcome_setting
    else:
        welcome_setting = get_config("group_template", "welcome_setting")
    welcome_setting = welcome_setting.replace("[name]", name).replace(
        "[inviter]", inviter
    )
    wechat_api.send_wechat_msg(group_id, welcome_setting)


# 退群事件处理
def out_group_msg_handle(data):
    # 获取退群人，只获取第一个
    """
           {
        "chat_room_id": "51740029844@chatroom",
        "member_list": [
            {
                "room_name": "",
                "wx_id": "wxid_h0vq4b62izaj12"
            }
        ],
        "msg": "退群事件",
        "port": 30001,
        "self_wx_id": "wxid_tjlscvvc60a022",
        "type": 444
    }
    """
    if data["member_list"]:
        wx_id = data["member_list"][0]["wx_id"]
        group_id = data["chat_room_id"]
        if return_data := wechat_api.search_wxid_info(wx_id):
            name = return_data["data"]["nick_name"]
            if group := GroupCRUD.get_group_by_id(group_id):
                out_setting = group.out_setting
            else:
                out_setting = get_config("group_template", "out_setting")
            out_setting = out_setting.replace("[name]", name)
            wechat_api.send_wechat_msg(group_id, out_setting)


# 好友申请事件处理
# TODO 后续增加延迟 friend_verify_delay
def agree_friend_application_handle(data):
    # {'at_list': [], 'content': '<msg fromusername="wxid_h0vq4b62izaj12" encryptusername="v3_020b3826fd0301000000000045b80ad5943fa9000000501ea9a3dba12f95f6b60a0536a1adb6a43395e8b56a514640a02088f23bc80031d623ef57e283c15ad7947ad7af5326a87400433a37a8268fddf06f7b8317ddf9884898f855ea13cf0c1d973b@stranger" fromnickname="天空" content="我是群聊&quot;测试社群1&quot;的天空" fullpy="tiankong" shortpy="TK" imagestatus="3" scene="14" country="" province="" city="" sign="" percard="0" sex="0" alias="zwzs55555" weibo="" albumflag="0" albumstyle="0" albumbgimgid="" snsflag="256" snsbgimgid="" snsbgobjectid="0" mhash="" mfullhash="" bigheadimgurl="http://wx.qlogo.cn/mmhead/ver_1/wah5ibmhfzpAODmk0O3xyKTash87vtmvFaepYd005KLWHx0Uqiax7n4VJjw6v1dibcMYt0EexJ0aTnNUcjXh2F1KjfgBfB22w3sCmyYRKw2wY3hTSJsID2XHpoFiaDzEia81VbnyU0CR2A3spp07I3ldQEA/0" smallheadimgurl="http://wx.qlogo.cn/mmhead/ver_1/wah5ibmhfzpAODmk0O3xyKTash87vtmvFaepYd005KLWHx0Uqiax7n4VJjw6v1dibcMYt0EexJ0aTnNUcjXh2F1KjfgBfB22w3sCmyYRKw2wY3hTSJsID2XHpoFiaDzEia81VbnyU0CR2A3spp07I3ldQEA/132" ticket="v4_000b708f0b040000010000000000dfb9f98ae58ae872fd2bfb1c4d671000000050ded0b020927e3c97896a09d47e6e9eb00c43bfc6598eb24504e03184e0455cee7ddcf4a49e32df853a763db64971bcd51d559f99945823949e62f4c760f7e951b9621590894a9b6839115f265656177c25fb178cb028ebcf677f73eb0fb4aad460d2d50b62d8e3b3937b7613b35c65a064fe2930dcf14762@stranger" opcode="2" googlecontact="" qrticket="" chatroomusername="34901437633@chatroom" sourceusername="" sourcenickname="" sharecardusername="" sharecardnickname="" cardversion="" extflag="0"><brandlist count="0" ver="883680258"></brandlist></msg>', 'file_path': 'D:\\wechatFile\\WeChat Files\\', 'is_pc_msg': 0, 'is_self_msg': 0, 'local_id': '66785', 'msg_id': '1487276773728142914', 'msg_type': 37, 'port': 30001, 'self_wx_id': 'wxid_tjlscvvc60a022', 'sender': '', 'time_stamp': 1733106939, 'type': 100, 'wx_id': 'fmessage'}
    fromusername, encryptusername, ticket, content = friend_request_xml_jx(
        data["content"]
    )
    robot_setting = SettingCRUD.get_setting()
    # 一次性取出指定字段
    friend_verify, friend_verify_delay, friend_verify_code, friend_verify_welcome = (
        robot_setting.friend_verify,
        robot_setting.friend_verify_delay,
        robot_setting.friend_verify_code,
        robot_setting.friend_verify_welcome,
    )
    if friend_verify == 0:
        # 不自动通过好友申请
        return
    if friend_verify_code:
        # 通过逗号分割文字
        friend_verify_code_list = friend_verify_code.split(",")
        if content not in friend_verify_code_list:
            # 验证不通过跳过
            return
    if friend_verify_delay:
        # 延迟通过好友申请
        time.sleep(friend_verify_delay)
    wechat_api.api_agree_friend_application(
        wx_id=fromusername, v3=encryptusername, v4=ticket
    )
    if friend_verify_welcome:
        wechat_api.send_wechat_msg(fromusername, friend_verify_welcome)
        
# 邀请进群功能
def invite_group_handle(content):
    # 获取群组信息
    """
        {
            "at_list": [],
            "content": "<?xml version=\"1.0\"?>\n<msg>\n\t<appmsg appid=\"\" sdkver=\"\">\n\t\t<title><![CDATA[邀请你加入群聊]]></title>\n\t\t<des><![CDATA[\"木不易成楊！\"邀请你加入群聊\"🧩𝐓𝐞𝐚𝐦𝐂𝐨𝐨𝐤交流群①\"，进入可查看详情。]]></des>\n\t\t<action>vi        ew</action>\n\t\t<type>5</type>\n\t\t<showtype>0</showtype>\n\t\t<content />\n\t\t<url><![CDATA[https://support.weixin.qq.com/cgi-bin/mmsupport-bin/addchatroombyinvite?ticket=AdmTgDH5B5ZhpZiBYwqU7Q%3D%3D]]></url>\n\t\t<thumburl><![CDATA[http://wx.qlogo.cn/mmcrhead/icXtjp9jsR5TRLJaDZHwHbVV6Vz57asLJtJJ8476WpOia8ibLZIg2yDXbYqjfptLGOp7sGxVkkfiaLg/0]]></thumburl>\n\t\t<lowurl />\n\t\t<appattach>\n\t\t\t<totallen>0</totallen>\n\t\t\t<attachid />\n\t\t\t<fileext />\n\t\t</appattach>\n\t\t<extinfo />\n\t</appmsg>\n\t<appinfo>\n\t\t<version />\n\t\t<appname />\n\t</appinfo>\n</msg>\n",
            "file_path": "D:\\wechatFile\\WeChat Files\\wxid_tjlscvvc60a022\\FileStorage\\Cache\\2024-12\\e8291f36cc9e42ac332fbadf38c16c04.jpg",
            "is_pc_msg": 0,
            "is_self_msg": 0,
            "local_id": "67077",
            "msg_id": "3823453897226810092",
            "msg_type": 49,
            "port": 30001,
            "self_wx_id": "wxid_tjlscvvc60a022",
            "sender": "",
            "time_stamp": 1733125636,
            "type": 100,
            "wx_id": "LoVe10285309"
        }
    """
    url = chatroom_invite_xml_jx(content)
    wechat_api.api_agree_friend_invite(url=url)
    
