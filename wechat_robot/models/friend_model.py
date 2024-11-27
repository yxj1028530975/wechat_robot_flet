from sqlalchemy import Column, String, Text
from .db_manager import Base
from .db_manager import SessionLocal

class Friend(Base):
    __tablename__ = 'friend'

    friend_id = Column(String, primary_key=True, unique=True, index=True)
    friend_name = Column(String)
    status = Column(String)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
class FriendCRUD:
    @staticmethod
    def add_friend(data):
        session = SessionLocal()
        try:
            friend = Friend(**data)
            session.add(friend)
            session.commit()
        except Exception as e:
            session.rollback()
            print(f"添加好友失败：{e}")
        finally:
            session.close()
    
    @staticmethod
    def get_friend_by_id(friend_id):
        session = SessionLocal()
        try:
            return session.query(Friend).filter(Friend.friend_id == friend_id).first()
        finally:
            session.close()
    
    @staticmethod
    def update_friend(friend_id, update_data):
        session = SessionLocal()
        try:
            friend = session.query(Friend).filter(Friend.friend_id == friend_id).first()
            if friend:
                for key, value in update_data.items():
                    setattr(friend, key, value)
                session.commit()
            else:
                print("好友不存在")
        except Exception as e:
            session.rollback()
            print(f"更新好友失败：{e}")
        finally:
            session.close()
    
    @staticmethod
    def delete_friend(friend_id):
        session = SessionLocal()
        try:
            friend = session.query(Friend).filter(Friend.friend_id == friend_id).first()
            if friend:
                session.delete(friend)
                session.commit()
            else:
                print("好友不存在")
        except Exception as e:
            session.rollback()
            print(f"删除好友失败：{e}")
        finally:
            session.close()
    
    # 获取所有好友，以列表形式返回
    @staticmethod
    def get_all_friend():
        session = SessionLocal()
        try:
            return session.query(Friend).all()
        finally:
            session.close()