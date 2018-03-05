# 自动计算数据

import matplotlib.pyplot as plt 

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

# 删除数据点的轮廓
# 可在调用scatter()时传递实参edgecolor = 'none'

# 自定义颜色 调用c = 'red'/ c = (1, 0, 0)
# plt.scatter(x_values, y_values, c = (1, 0, 0), edgecolor = 'none', s = 40)

# 使用颜色折射
# 颜色折射(colormap)
plt.scatter(x_values, y_values, c = y_values, cmap = plt.cm.Blues, edgecolor = 'none', s = 40)

# 备注：将参数c设置成了一个y值列表，并使用参数cmap告诉pyplot使用哪个颜色映射。
# 这些代码就会将y值较小的点显示为浅蓝色，并将y值叫到的点显示为深蓝色。           

# 设置图表标题并给坐标轴加上标签
plt.title("Square Number", fontsize = 16)
plt.xlabel("Value", fontsize = 12)
plt.ylabel("Square of Value", fontsize = 12)

# 设置刻度标记的大小
plt.tick_params(axis = 'both', which = 'major', labelsize = 12)

# 设置每个坐标的取值范围
plt.axis([0, 1100, 0, 1100000])

plt.show()

#自动保存图表
# plt.savefig('Square_plot.png', bbox_inches = 'tight')




















