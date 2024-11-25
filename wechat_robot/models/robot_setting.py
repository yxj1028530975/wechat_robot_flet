from sqlalchemy import Column, String, Text, Integer
from .db_manager import Base
from sqlalchemy.orm import Session
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