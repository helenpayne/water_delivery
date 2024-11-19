from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class Token(BaseModel):
    token: str



# 用户基础模型
class UserBase(BaseModel):
    nickname: str  # 昵称
    avatar_url: str  # 头像URL
    phone_number: Optional[str] = None  # 电话号码（可选）
    level: int = 0  # 等级，默认值为0
    balance: float = 0.00  # 余额，默认值为0
    deposit: float = 0.00  # 押金，默认值为0
    points: int = 0  # 用户积分，默认值为0
    is_new_user: bool = True  # 是否新用户，默认值为True
    registered_ip: Optional[str] = None  # 注册IP（可选）

# 用户创建模型
class UserCreate(UserBase):
    wechat_openid: str  # 微信openid（唯一且不能为空）

# 用户响应模型
class UserResponse(UserBase):
    id: int  # 用户ID
    created_at: datetime  # 创建时间

    class Config:
        from_attributes = True  # 启用ORM模式以支持SQLAlchemy

# 更新用户信息模型
class UserUpdate(BaseModel):
    nickname: Optional[str] = None
    avatar_url: Optional[str] = None
    phone_number: Optional[str] = None
    level: Optional[int] = None
    balance: Optional[float] = None
    deposit: Optional[float] = None
    points: Optional[int] = None
    is_new_user: Optional[bool] = None
    registered_ip: Optional[str] = None

# 用于数据库查询和验证的基础用户模型
class UserInDB(UserBase):
    id: int  # 用户ID
    created_at: datetime  # 创建时间

    class Config:
        from_attributes = True
