
# 1.绘制简单的折线图
import matplotlib.pyplot as plt

# 3.校正图形
input_values = [0, 2, 3, 4, 5]

squares = [1, 4, 9, 16, 25]

# 2.修改标签文字和线条粗细
plt.plot(input_values, squares, linewidth = 5)

# 2.1 设置图表标题，并给坐标轴添加标签
plt.title("Squart Numbers ", fontsize = 24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Square of Value ", fontsize = 14)

# 设置刻度标记的大小
plt.tick_params(axis = 'both', labelsize = 12)
plt.show()


































