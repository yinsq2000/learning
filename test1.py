import matplotlib.pyplot as plt
import numpy as np
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
plt.close('all')
