import os
import sys
from fastapi import FastAPI

# 确保将项目根目录添加到 Python 搜索路径
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from app.models import Base
from app.database import engine
from app.routers import user, auth

# 创建数据库表
Base.metadata.create_all(bind=engine)

app = FastAPI()

# 注册路由
app.include_router(user.router)
app.include_router(auth.router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)