import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 设置美观样式
sns.set_theme(style="whitegrid")
plt.rcParams["font.sans-serif"] = ["SimHei"]    # 黑体显示中文
plt.rcParams["axes.unicode_minus"] = False

# 加载数据
tips = sns.load_dataset("tips")
print(tips.head())
# 散点图
'''
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="sex")
plt.title("小费金额 vs 总账单（按性别分组）")
plt.show()
#箱线图
sns.boxplot(data=tips, x="time", y="tip", hue="smoker")
plt.title("不同时段的小费分布（是否吸烟）")
plt.show()
#直方图
g = sns.FacetGrid(tips, col="day", height=4)
g.map(sns.histplot, "total_bill", kde=True, bins=15)
g.set_axis_labels("总账单 ($)", "频数")
plt.show()

#热力图 – 相关性矩阵（使用 iris 数据集）
iris = sns.load_dataset("iris")
corr = iris.select_dtypes(include=[float, int]).corr()
sns.heatmap(corr, annot=True, cmap="coolwarm", center=0)
plt.title("鸢尾花特征相关性矩阵")
plt.show()
'''
#分类图 – 小提琴图 + 箱线图组合（penguins 数据集）
penguins = sns.load_dataset("penguins").dropna()
# 你的代码
sns.violinplot(data=penguins, x="island", y="body_mass_g", hue="sex", split=True)
plt.title("不同岛屿企鹅体重分布（性别对比）")
plt.show()
# 练习 6：线性回归图 – 探索 mpg 数据集中 horsepower 与 mpg 的关系
mpg = sns.load_dataset("mpg").dropna()
# 你的代码
sns.lmplot(data=mpg, x="horsepower", y="mpg", hue="origin", ci=None, height=5, aspect=1.5)
plt.title("马力 vs 油耗（按产地分组）")
plt.show()


import seaborn as sns
print(sns.get_data_home())



