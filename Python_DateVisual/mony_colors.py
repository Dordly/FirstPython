# 立方
import matplotlib.pyplot as plt 

x_value = list(range(1, 5001))
y_value = [x**3 for x in x_value]
# 颜色折射(colormap)
plt.scatter(x_value, y_value, edgecolor = 'none', s = 20)

# 备注：将参数c设置成了一个y值列表，并使用参数cmap告诉pyplot使用哪个颜色映射。
# 这些代码就会将y值较小的点显示为浅蓝色，并将y值叫到的点显示为深蓝色。           

# 设置图表标题并给坐标轴加上标签
plt.title("Square Number", fontsize = 16)
plt.xlabel("Value", fontsize = 12)
plt.ylabel("Square of Value", fontsize = 12)

# 设置刻度标记的大小
plt.tick_params(axis = 'both', which = 'major', labelsize = 12)

plt.show()