from lxml import etree
#好友申请消息解析
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
    return fromusername, encryptusername, ticket,content