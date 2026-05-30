
import matplotlib.pyplot as plt
import numpy as np
'''
# ===================== 3. 设置matplotlib中文显示 =====================
plt.rcParams["font.sans-serif"] = ["SimHei"]    # 黑体显示中文
plt.rcParams["axes.unicode_minus"] = False      # 解决负号显示问题
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y, label='sin(x)')
plt.title("正弦曲线")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()
'''
import pandas as pd
import pymysql

# 连接数据库
conn = pymysql.connect(
    host="192.168.110.121",
    user="root",
    password="12345678",
    database="marketing",
    charset="utf8"
)

# 读取前10000条
sql = "SELECT * FROM userbehavior_tiny LIMIT 5000;"
df = pd.read_sql(sql, conn)

print(df.head())
#print(df)

numpy_array = df.to_numpy()
print(numpy_array)


# ===================== 2. 按beahavior统计数量 =====================
behavior_count = df["beahavior"].value_counts()
print("行为分类统计：")
print(behavior_count)

# ===================== 3. 设置matplotlib中文显示 =====================
plt.rcParams["font.sans-serif"] = ["SimHei"]    # 黑体显示中文
plt.rcParams["axes.unicode_minus"] = False      # 解决负号显示问题
# ===================== 4. 绘制 柱状图 + 饼图 =====================
# 创建画布，1行2个子图
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# 柱状图
ax1.bar(behavior_count.index, behavior_count.values, color=["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"])
ax1.set_title("用户行为分类数量统计", fontsize=14)
ax1.set_xlabel("行为类型", fontsize=12)
ax1.set_ylabel("数量", fontsize=12)
# 在柱子上方显示数值
for i, v in enumerate(behavior_count.values):
    ax1.text(i, v + 50, str(v), ha="center")

# 饼图
ax2.pie(behavior_count.values, labels=behavior_count.index, autopct="%1.1f%%", startangle=90)
ax2.set_title("用户行为分类占比", fontsize=14)

plt.tight_layout()
plt.show()
