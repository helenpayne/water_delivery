from fastapi import APIRouter, HTTPException, Depends, Request
from sqlalchemy.orm import Session
import jwt
from app.models import User
from app.database import SessionLocal
from app import schemas
from config import JWT_SECRET, JWT_ALGORITHM

router = APIRouter()


# 获取数据库会话的依赖函数
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 用于从请求头中解析 JWT token 的工具函数
def get_token_from_header(request: Request):
    auth_header = request.headers.get('Authorization')
    if not auth_header or not auth_header.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid authorization header")
    return auth_header.split(" ")[1]


# 用于解析 JWT token 并获取当前用户的工具函数
def get_current_user(token: str = Depends(get_token_from_header), db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        openid = payload.get("sub")
        if openid is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        user = db.query(User).filter(User.wechat_openid == openid).first()
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")


# 新增的获取用户信息的路由
@router.get("/user-info", response_model=schemas.UserResponse)
def get_user_info(current_user: User = Depends(get_current_user)):
    return current_user