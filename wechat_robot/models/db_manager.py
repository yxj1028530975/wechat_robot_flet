# 文件路径: /d:/gr_project/wechat_robot_flet/wechat_robot/models/db_manager.py

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker  # 更新导入路径

# 创建数据库引擎
engine = create_engine(
    'sqlite:///database.db',
    echo=False,
    connect_args={'check_same_thread': False}  # 允许多线程访问
)

# 创建基类
Base = declarative_base()

# 创建会话工厂
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)