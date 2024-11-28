# 文件路径: /d:/gr_project/wechat_robot_flet/wechat_robot/models/db_manager.py

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# 定义 data 目录的路径（确保与 fastapi_server.py 中的路径一致）
data_dir = os.path.join(os.path.abspath("."), "data")

# 如果 data 目录不存在，则创建
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

# 定义数据库文件的路径
db_file_path = os.path.join(data_dir, 'database.db')

# 创建数据库引擎
engine = create_engine(
    f'sqlite:///{db_file_path}',
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