from lxml import etree
from wechat_robot.utils.httpx_handle import HttpxHandle

# 好友申请消息解析
def friend_request_xml_jx(message):
    xml = etree.fromstring(message)
    """
    <msg fromusername="wxid_tjlscvvc60a022"
        encryptusername="v3_020b3826fd03010000000000a02e2e9345c2e9000000501ea9a3dba12f95f6b60a0536a1adb686dc96bfb8ffe2abda03886e00848510d74601e536d27a00a3ee3c561196b736bdec93ae9ebec49abe3b6f0accb9f542fd239a704a06accdffb6029a52@stranger"
        fromnickname="星辰"
        content="杨雄君"
        fullpy="xingchen"
        shortpy="XC"
        imagestatus="3" scene="14"
        country="" province="" city="" sign="" percard="0" sex="0" alias="" weibo="" albumflag="0" albumstyle="0"
        albumbgimgid="" snsflag="257" snsbgimgid="" snsbgobjectid="0"
        mhash="6d6b74c0bdc5bcb1582180e3f6a844ac" mfullhash="6d6b74c0bdc5bcb1582180e3f6a844ac"
        bigheadimgurl="http://wx.qlogo.cn/mmhead/ver_1/zpaya5Zt3MDvPo8qduY1Ft2TPnXhwa8mep7kKcoLDv1yy107Kc6RUjeUtVVtfwbTJzF39MODicU54mAmicuDVqu4WEicRC0TGia32Lr4IIB0JbDUzb1bqAaatJBtA8iaQYlVZ/0"
        smallheadimgurl="http://wx.qlogo.cn/mmhead/ver_1/zpaya5Zt3MDvPo8qduY1Ft2TPnXhwa8mep7kKcoLDv1yy107Kc6RUjeUtVVtfwbTJzF39MODicU54mAmicuDVqu4WEicRC0TGia32Lr4IIB0JbDUzb1bqAaatJBtA8iaQYlVZ/132" ticket="v4_000b708f0b040000010000000000d5daf8102a76b4953be3282fe9651000000050ded0b020927e3c97896a09d47e6e9e54be26c9b6d164ba0f3369bb592008a40952c57fc9eda0815198ae6b5fea5f6840a21c93bcce960b920ac59e64aa9cfcb2702f9f0d9b3eea95f1424f5a665e06efb1fea24f2c70de5259d4b9ba87fc5ffb5bc8a49616c12df587209d86f17d28c5351308890ec6cd64@stranger"
        opcode="2" googlecontact="" qrticket=""
        chatroomusername="34390022827@chatroom" sourceusername=""
        sourcenickname="" sharecardusername="" sharecardnickname="" cardversion="" extflag="0">
        <brandlist count="0" ver="822771760"></brandlist>
    </msg>
    """
    fromusername = xml.get("fromusername")
    encryptusername = xml.get("encryptusername")
    ticket = xml.get("ticket")
    fromnickname = xml.get("fromnickname")
    content = xml.get("content")
    scene = xml.get("scene")
    smallheadimgurl = xml.get("smallheadimgurl")
    return fromusername, encryptusername, ticket, content


# 邀请进群解析
def chatroom_invite_xml_jx(message):
    xml = etree.fromstring(message)
    """
    {
    "at_list": [],
    "content": "<msg><emoji fromusername = \"wxid_2lallno9qrhi22\" tousername = \"47948179679@chatroom\" type=\"2\" idbuffer=\"media:0_0\" md5=\"8a77b7acd4e2df348dd1612aa612b018\" len = \"837807\" productid=\"\" androidmd5=\"8a77b7acd4e2df348dd1612aa612b018\" androidlen=\"837807\" s60v3md5 = \"8a77b7acd4e2df348dd1612aa612b018\" s60v3len=\"837807\" s60v5md5 = \"8a77b7acd4e2df348dd1612aa612b018\" s60v5len=\"837807\" cdnurl = \"http://vweixinf.tc.qq.com/110/20401/stodownload?m=8a77b7acd4e2df348dd1612aa612b018&amp;filekey=30440201010430302e02016e0402535a0420386137376237616364346532646633343864643136313261613631326230313802030cc8af040d00000004627466730000000132&amp;hy=SZ&amp;storeid=2669bde3a0003e0a77a6eb6100000006e01004fb1535a09ef0011570160409&amp;ef=1&amp;bizid=1022\" designerid = \"\" thumburl = \"\" encrypturl = \"http://vweixinf.tc.qq.com/110/20402/stodownload?m=ac6d61cff6f17e02bfca4c9da82bebcb&amp;filekey=30440201010430302e02016e0402535a0420616336643631636666366631376530326266636134633964613832626562636202030cc8b0040d00000004627466730000000132&amp;hy=SZ&amp;storeid=2669bde3a0005099b7a6eb6100000006e02004fb2535a09ef0011570160420&amp;ef=2&amp;bizid=1022\" aeskey= \"dbb7a23f88f14789b81a5d934b80b327\" externurl = \"http://vweixinf.tc.qq.com/110/20403/stodownload?m=14c5f4970fa4d44e45f93b139a24eb54&amp;filekey=30440201010430302e02016e0402535a042031346335663439373066613464343465343566393362313339613234656235340203031480040d00000004627466730000000132&amp;hy=SZ&amp;storeid=2669bde3a00062a437a6eb6100000006e03004fb3535a09ef0011570160433&amp;ef=3&amp;bizid=1022\" externmd5 = \"08f743e4efc74e0967a1255cb919f644\" width= \"300\" height= \"303\" tpurl= \"\" tpauthkey= \"\" attachedtext= \"\" attachedtextcolor= \"\" lensid= \"\" emojiattr= \"\" linkid= \"\" desc= \"\" ></emoji> </msg>",
    "file_path": "D:\\wechatFile\\WeChat Files\\8A77B7ACD4E2DF348DD1612AA612B018",
    "is_pc_msg": 0,
    "is_self_msg": 0,
    "local_id": "67083",
    "msg_id": "293966221245869311",
    "msg_type": 47,
    "port": 30001,
    "self_wx_id": "wxid_tjlscvvc60a022",
    "sender": "wxid_2lallno9qrhi22",
    "time_stamp": 1733125839,
    "type": 100,
    "wx_id": "47948179679@chatroom"
}
    """
    return xml.xpath("//url")[0].text

# 获取点歌内容
# def get_qq_song_info(search_name="世界第一等"):
#     url = 'https://api.livetools.top/music_api/get_qq_song_info' + f"?name={search_name}"
#     data = HttpxHandle(
#                 base_url=url, timeout=2
#             )
#     if data.get("code") == 200 and data.get("data"):
#         return_data = data['data'][0]
#         if return_data:
#             self.send_music(
#                 self.wechat_wxid,
#                 return_data["name"],
#                 return_data["singer"],
#                 return_data["image_url"] if return_data["image_url"] else "https://y.qq.com/favicon.ico?max_age=2592000",
#                 return_data["download_url"],
#                 f"https://y.qq.com/n/ryqq/songDetail",
#                 mod="76"
#             )