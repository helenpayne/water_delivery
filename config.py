# config.py

import os

# 微信小程序配置
WECHAT_APPID = os.getenv("WECHAT_APPID", "wx42e5ff9a1f0757ed")
WECHAT_SECRET = os.getenv("WECHAT_SECRET", "d43e92107d6ea6c6ae8c2560c8abee31")


JWT_SECRET = "kB7fQ8sV9p&xW!E2$0tL3D#oJH4y*5zK6P$7mN8@0vT9yU1R!"  # 替换为一个复杂的密钥
JWT_ALGORITHM = "HS256"  # HMAC SHA256 算法
JWT_EXPIRATION_TIME = 3600  # 令牌有效期（秒）
