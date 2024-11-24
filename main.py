from fastapi import FastAPI

# 确保将项目根目录添加到 Python 搜索路径
import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from app.models import Base
from app.database import engine
from app.routers import user, auth

# 创建/更新数据库表
Base.metadata.create_all(bind=engine)

app = FastAPI()

# 注册路由
app.include_router(user.router)  # 包含用户相关的路由
app.include_router(auth.router)  # 包含认证相关的路由

@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI application!"}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)