# schemas.py

from pydantic import BaseModel
from typing import Optional

class WeChatLoginRequest(BaseModel):
    code: str  # 微信登录凭证

class WeChatLoginResponse(BaseModel):
    openid: str
    session_key: str

class UserResponse(BaseModel):
    id: int
    openid: str
    nickname: str
    avatar_url: str

    class Config:
        orm_mode = True  # 允许Pydantic从ORM模型转换数据
