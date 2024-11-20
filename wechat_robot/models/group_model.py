from sqlalchemy import Column, String, Text
from .db_manager import Base
from sqlalchemy.orm import Session
from .db_manager import SessionLocal

class Group(Base):
    __tablename__ = 'group'

    group_id = Column(String, primary_key=True, unique=True, index=True)
    group_name = Column(String)
    out_setting = Column(Text)
    welcome_setting = Column(Text)
    fun_setting = Column(Text)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class GroupCRUD:
    @staticmethod
    def add_group(data):
        session = SessionLocal()
        try:
            group = Group(**data)
            session.add(group)
            session.commit()
        except Exception as e:
            session.rollback()
            print(f"添加群组失败：{e}")
        finally:
            session.close()

    @staticmethod
    def get_group_by_id(group_id):
        session = SessionLocal()
        try:
            return session.query(Group).filter(Group.group_id == group_id).first()
        finally:
            session.close()

    @staticmethod
    def update_group(group_id, update_data):
        session = SessionLocal()
        try:
            group = session.query(Group).filter(Group.group_id == group_id).first()
            if group:
                for key, value in update_data.items():
                    setattr(group, key, value)
                session.commit()
            else:
                print("群组不存在")
        except Exception as e:
            session.rollback()
            print(f"更新群组失败：{e}")
        finally:
            session.close()

    @staticmethod
    def delete_group(group_id):
        session = SessionLocal()
        try:
            group = session.query(Group).filter(Group.group_id == group_id).first()
            if group:
                session.delete(group)
                session.commit()
            else:
                print("群组不存在")
        except Exception as e:
            session.rollback()
            print(f"删除群组失败：{e}")
        finally:
            session.close()