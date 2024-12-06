from sqlalchemy import Column, String, Text,Integer,DateTime
from .db_manager import Base
from .db_manager import SessionLocal

class Fun(Base):
    __tablename__ = 'fun'

    fun_id = Column(String, primary_key=True, unique=True, index=True)
    fun_name = Column(String)
    trigger_keyword = Column(String)
    # 0: 关闭 1: 开启
    status = Column(Integer, default=0)
    # 描述
    description = Column(Text)
    # 触发类型
    # 1 关键词触发 2 前缀匹配
    trigger_type = Column(Integer)
    # 新增 code 字段，存储功能代码
    code = Column(Text)
    icon = Column(String)
    # 是否默认启用
    is_default = Column(Integer, default=0)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
class FunCRUD:
    @staticmethod
    def add_fun(data):
        session = SessionLocal()
        try:
            fun = Fun(**data)
            session.add(fun)
            session.commit()
        except Exception as e:
            session.rollback()
            print(f"添加功能失败：{e}")
        finally:
            session.close()

    @staticmethod
    def get_fun_by_id(fun_id):
        session = SessionLocal()
        try:
            return session.query(Fun).filter(Fun.fun_id == fun_id).first()
        finally:
            session.close()

    @staticmethod
    def update_fun(fun_id, update_data):
        session = SessionLocal()
        try:
            if fun := session.query(Fun).filter(Fun.fun_id == fun_id).first():
                for key, value in update_data.items():
                    setattr(fun, key, value)
                session.commit()
            else:
                print("功能不存在")
        except Exception as e:
            session.rollback()
            print(f"更新功能失败：{e}")
        finally:
            session.close()

    @staticmethod
    def delete_fun(fun_id):
        session = SessionLocal()
        try:
            if fun := session.query(Fun).filter(Fun.fun_id == fun_id).first():
                session.delete(fun)
                session.commit()
            else:
                print("功能不存在")
        except Exception as e:
            session.rollback()
            print(f"删除功能失败：{e}")
        finally:
            session.close()
    # 获取所有功能，并按trigger_type返回
    @staticmethod
    def get_all_fun():
        session = SessionLocal()
        try:
            funs = session.query(Fun).all()
            fun_dict = {}
            for fun in funs:
                if fun.trigger_type not in fun_dict:
                    fun_dict[fun.trigger_type] = []
                fun_dict[fun.trigger_type].append({
                    'fun_id': fun.fun_id,
                    'fun_name': fun.fun_name,
                    'status': fun.status,
                    'description': fun.description,
                    'trigger_keyword': fun.trigger_keyword,
                    'trigger_type': fun.trigger_type,
                    'code': fun.code  # 新增的 code 字段
                })
            return fun_dict
        finally:
            session.close()
    # 删除所有数据
    @staticmethod
    def delete_all_fun():
        session = SessionLocal()
        try:
            session.query(Fun).delete()
            session.commit()
        except Exception as e:
            session.rollback()
            print(f"删除所有功能失败：{e}")
        finally:
            session.close()
    # 返回所有功能
    @staticmethod
    def get_all_fun_id():
        session = SessionLocal()
        try:
            return session.query(Fun).all()
        finally:
            session.close()