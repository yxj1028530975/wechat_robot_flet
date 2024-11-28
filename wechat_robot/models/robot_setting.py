from sqlalchemy import Column, String, Text, Integer
from .db_manager import Base
from .db_manager import SessionLocal
class Setting(Base):
    __tablename__ = 'setting'

    id = Column(Integer, primary_key=True)  # 添加主键列
    out_setting = Column(
        Text,
        default="╒══退 群 提 示══╗\n启禀群主,有一成员退群\n昵称:[name]\n╘══【温 馨 提 示】══╝"
    )
    
    out_setting_tip = Column(
        Text,
        default="退群提醒只支持文字、emoji表情,换行in或[enter群用户:[name]"
    )
    
    welcome_setting = Column(
        Text,
        default="欢迎 [name] 加入本群！"
    )
    
    welcome_setting_tip = Column(
        Text,
        default="新人进群提醒只支持文字、emoji表情,换行in或[enter群用户:[name]"
    )
    
    fun_setting = Column(
        Text,
        default="╒══功能提示══╗"
    )
    
    fun_setting_tip = Column(
        Text,
        default="功能提示只支持文字、emoji表情,换行in或[enter群用户:[name]"
    )
    
    # 好友审核申请开关
    friend_verify = Column(
        Integer,
        default=1
    )
    
    # 好友审核延迟
    friend_verify_delay = Column(
        Integer,
        default=0
    )
    
    # 好友申请暗号
    friend_verify_code = Column(
        String,
        default=""
    )
    
    # 通过好友欢迎语
    friend_verify_welcome = Column(
        Text,
        default="你好，我是智微机器人，很高兴认识你！可以发送群邀请链接给我，我会直接加入群聊为你服务！"
    )
    
    # 微信头像
    wechat_avatar = Column(
        String,
        default="https://wx.qlogo.cn/mmhead/ver_1/HjRriajHlqX2VuichMnCAIde96eJAnck5uPSqzWM26gVZuhniaGK2U7VXYpElRmVQicuIe5w6TuDp9WnYiaAdhbuk6XcUXp8N8ZBPreibTicBxkfNds3Ww4bDVGK1skkuY2t6dv/0"
    )
    # 微信昵称
    wechat_name = Column(
        String,
        default="星辰"
    )
        
class SettingCRUD:
    @staticmethod
    def get_setting():
        session = SessionLocal()
        setting = session.query(Setting).first()
        if not setting:
                # 如果不存在设置记录，创建一条默认记录
                setting = Setting()
                session.add(setting)
                session.commit()
                session.refresh(setting)
        return setting
    
    @staticmethod
    def update_setting(update_data: dict):
        session = SessionLocal()
        setting = SettingCRUD().get_setting()
        for key, value in update_data.items():
            setattr(setting, key, value)
        session.commit()
        return setting