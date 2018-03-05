# 使用 scatter()绘制散点图并设置其样式

import matplotlib.pyplot as plt 

# 使用scatter()绘制一系列点
x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

# 设置输出的样式并添加标题，给轴添加标签
plt.scatter(x_values, y_values, s = 100)

# 设置图表标题并给坐标轴加上标签
plt.title("Square Number", fontsize = 16)
plt.xlabel("Value", fontsize = 12)
plt.ylabel("Square of Value", fontsize = 12)

# 设置刻度标记的大小
plt.tick_params(axis = 'both', which = 'major', labelsize = 12)
plt.show()