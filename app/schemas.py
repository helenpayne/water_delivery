from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class Token(BaseModel):
    token: str


class UserBase(BaseModel):
    nickname: str
    avatar_url: Optional[str] = None
    phone_number: Optional[str] = None
    level: int = 0
    balance: float = 0.00
    deposit: float = 0.00
    points: int = 0
    is_new_user: bool = True
    registered_ip: Optional[str] = None


class UserCreate(UserBase):
    wechat_openid: str


class UserResponse(UserBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True