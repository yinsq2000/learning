
import matplotlib.pyplot as plt
import numpy as np


import pandas as pd
from sqlalchemy import create_engine
'''
# 1. 数据库连接配置
# 格式：mysql+pymysql://用户名:密码@主机:端口/数据库名
engine = create_engine(
    "mysql+pymysql://root:12345678@192.168.110.121:3306/marketing",
    echo = False,  # True 会打印执行的SQL，调试用
    pool_recycle = 3600  # 自动重连，防止超时
)
'''
# 数据库连接配置
DB_CONFIG = {
    'host': '192.168.110.121',
    'port': 3306,
    'user': 'root',
    'password': '12345678',
    'database': 'marketing'
}
# 创建 SQLAlchemy 引擎
# 格式：mysql+pymysql://用户名:密码@主机:端口/数据库名?charset=utf8
connection_url = f"mysql+pymysql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}?charset=utf8"

engine = create_engine(connection_url)

# 方法1：使用 LIMIT 子句读取前 10000 条
query = "SELECT * FROM userbehavior_tiny LIMIT 5000"
df = pd.read_sql(query, engine)

# 方法2：分块读取（适合超大表）
# chunks = pd.read_sql("SELECT * FROM userbehavior_tiny LIMIT", engine, chunksize=10000)
# df = next(chunks)  # 只取第一块

print(f"读取完成，共 {len(df)} 条记录")
print(df.head())
print(df.info())

