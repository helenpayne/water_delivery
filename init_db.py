import sys
import os

# 打印 sys.path，检查是否包含项目根目录
print(sys.path)

# 确保项目根目录在 sys.path 中
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
print(sys.path)  # 再次打印检查
