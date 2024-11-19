from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()


# 用户数据库模型
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True, comment="自增ID")
    wechat_openid = Column(String(191), unique=True, nullable=False, comment="微信openid")
    nickname = Column(String(255), nullable=False, comment="昵称")
    avatar_url = Column(String(255), nullable=False, comment="头像URL")
    phone_number = Column(String(20), nullable=True, comment="电话号码")
    level = Column(Integer, default=0, nullable=False, comment="等级")
    balance = Column(Float, default=0.00, nullable=False, comment="余额")
    deposit = Column(Float, default=0.00, nullable=False, comment="押金")
    points = Column(Integer, default=0, nullable=False, comment="积分")
    is_new_user = Column(Boolean, default=True, nullable=False, comment="是否新用户")
    created_at = Column(DateTime, server_default=func.now(), nullable=False, comment="创建时间")
    registered_ip = Column(String(45), nullable=True, comment="注册IP")