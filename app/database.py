from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 替换为你的 MySQL 数据库连接字符串
DATABASE_URL = "mysql+pymysql://root:123456@localhost/water_delivery"

# 创建数据库引擎
engine = create_engine(DATABASE_URL, echo=True)

# 创建会话工厂
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 声明基础类
Base = declarative_base()