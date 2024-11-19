from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Optional
import jwt
from datetime import datetime, timedelta
import requests

from config import JWT_SECRET, JWT_ALGORITHM, JWT_EXPIRATION_TIME, WECHAT_APPID, WECHAT_SECRET
from app import models, schemas
from app.database import SessionLocal

router = APIRouter()


# 获取数据库会话的依赖函数
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class WechatLoginRequest(BaseModel):
    js_code: str
    nickname: str
    avatar_url: Optional[str]
    gender: int
    registered_ip: str


class Token(BaseModel):
    token: str


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(seconds=JWT_EXPIRATION_TIME)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return encoded_jwt


@router.post("/wechat-login", response_model=Token)
async def wechat_login(request: WechatLoginRequest, db: Session = Depends(get_db)):
    try:
        print(f"收到的请求数据: {request.dict()}")
        data = request.dict()

        js_code = data["js_code"]
        nickname = data["nickname"]
        avatar_url = data["avatar_url"]
        gender = data["gender"]
        registered_ip = data["registered_ip"]

        # 发起请求获取微信openid
        wechat_api_url = f"https://api.weixin.qq.com/sns/jscode2session?appid={WECHAT_APPID}&secret={WECHAT_SECRET}&js_code={js_code}&grant_type=authorization_code"
        response = requests.get(wechat_api_url)

        if response.status_code == 200:
            wechat_data = response.json()
            if "openid" in wechat_data:
                wechat_openid = wechat_data["openid"]
                print(f"获取到的 wechat_openid: {wechat_openid}")
            else:
                error_msg = wechat_data.get("errmsg", "unknown error")
                raise HTTPException(status_code=400, detail=f"无法获取微信 openid, 错误信息: {error_msg}")
        else:
            raise HTTPException(status_code=response.status_code, detail="微信服务器异常")

        # 查询用户是否存在
        db_user = db.query(models.User).filter(models.User.wechat_openid == wechat_openid).first()
        if not db_user:
            # 如果用户不存在，创建新用户
            user_create = schemas.UserCreate(
                wechat_openid=wechat_openid,
                nickname=nickname,
                avatar_url=avatar_url,
                gender=gender,
                registered_ip=registered_ip
            )
            db_user = models.User(**user_create.model_dump())
            db.add(db_user)
            db.commit()
            db.refresh(db_user)

        # 生成 JWT token
        token_data = {"sub": db_user.wechat_openid}
        token = create_access_token(data=token_data)

        return Token(token=token)
    except Exception as e:
        db.rollback()  # 处理异常时回滚事务
        print(f"处理请求时遇到错误: {e}")
        raise HTTPException(status_code=422, detail=str(e))
    finally:
        db.close()  # 确保无论发生异常与否都关闭数据库连接