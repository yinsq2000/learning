import pandas as pd
import numpy as np
'''
s = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'],dtype='float')
print(s)


data = {
    '姓名': ['张三', '李四', '王五'],
    '年龄': [25, 30, 28],
    '城市': ['北京', '上海', '广州']
}
df = pd.DataFrame(data)
print(df)


# 创建一个 3x4 的 NumPy 数组
arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]])

# 用数组定义 DataFrame
df1 = pd.DataFrame(arr)
print(df1)

df = pd.DataFrame(arr,
                  columns=['A', 'B', 'C', 'D'],
                  index=['row1', 'row2', 'row3'])
print(df)
arr1=arr[1,:]
print(arr1)
arr1[1] = 100
print(arr1)

print(df1)


df = pd.read_csv("C:\\Users\\admin\\Desktop\\FINTECH\\数据分析\\广告投放数据表.csv")


print(df.head()) # 前5行
print(df.tail(3)) # 后3行
print(df.info()) # 数据类型、缺失值
print(df.describe()) # 统计：均值、最大最小、标准差
print(df.columns) # 列名
print(df.shape) # 行数、列数


filtered = df[(df['douyin'] > 10) & (df['sales'] < 50 )]
print(filtered)

filtered1 = df.query("douyin > 10 and sales > 50" )
print(filtered1)

filtered1['add_column'] = 0
filtered1['add_column'] = filtered1['douyin']+filtered1['kuaishou']+filtered1['wechat']
#print(filtered1)

col_range = df[['douyin', 'wechat']].apply(lambda col: col.max() - col.min())
#printprint(col_range)

df3 = df[['douyin', 'wechat']].apply(lambda row: row['douyin'] + row['wechat'], axis=1)
print(df3)


df_concat = pd.concat([filtered, filtered1], axis=0)
print(df_concat)
'''
'''


import pandas as pd
from sqlalchemy import create_engine

# 1. 数据库连接配置
# 格式：mysql+pymysql://用户名:密码@主机:端口/数据库名
engine = create_engine("mysql+pymysql://root:root@0507@.121:3306/marketing")


from sqlalchemy import create_engine
#import matplotlib.pyplot as plt 

# 数据库连接配置
DB_CONFIG = {
    'host': '192.168.110',
    'port': 3306,
    'user': 'root',
    'password': 'root@0507',
    'database': 'marketing'
}
# 创建 SQLAlchemy 引擎
# 格式：mysql+pymysql://用户名:密码@主机:端口/数据库名?charset=utf8
connection_url = f"mysql+pymysql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}?charset=utf8mb4"

engine = create_engine(connection_url)

# 方法1：使用 LIMIT 子句读取前 10000 条
query = "SELECT * FROM userbehavior_tiny LIMIT 5000"
df = pd.read_sql(query, engine)

# 方法2：分块读取（适合超大表）
# chunks = pd.read_sql("SELECT * FROM your_table", engine, chunksize=10000)
# df = next(chunks)  # 只取第一块

print(f"读取完成，共 {len(df)} 条记录")
print(df.head())
print(df.info())

'''

import pandas as pd
import pymysql

# 连接数据库
conn = pymysql.connect(
    host="192.168.110.121",
    user="root",
    password="root@0507",
    database="marketing",
    charset="utf8"
)

# 读取前10000条
sql = "SELECT * FROM userbehavior_tiny LIMIT 10000;"
df = pd.read_sql(sql, conn)

print(df.head())
print(df)
