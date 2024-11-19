from app.models import Base
from fastapi import FastAPI
from app.routers import user  # 引入用户路由
from app.database import engine  # 引入数据库引擎

# 创建数据库表
Base.metadata.create_all(bind=engine)

app = FastAPI()

# 包含用户认证路由
app.include_router(user.router)
