# 1.绘制随机漫步图
import matplotlib.pyplot as plt 

from random_walk import RandomWalk

# # 创建一个RandomWalk实例，来将其包含的点都绘制出来
# rw = RandomWalk()
# rw.fill_walk()
# plt.scatter(rw.x_values, rw.y_values, s = 15)
# plt.show()

# 2.模拟多次随机漫步
# 只要程序处于活动状态，将不断地模拟随机漫步

# 2.1 设置随机漫步图的样式
while True:
	# 创建一个RandomWalk实例，来将其包含的点都绘制出来

	# rw = RandomWalk()
	# 2.4 增加点数
	# rw = RandomWalk(50000)

	# 2.5 调整尺寸以适合屏幕
	# rw = RandomWalk()

	# 2.6 分子运动
	rw = RandomWalk(5000)

	rw.fill_walk()


	# 2.5 设置绘制窗口的尺寸
	plt.figure(figsize = (10, 6))

# 备注:若知道屏幕尺寸，则: plt.figure(dpi = 128, figsize = (10, 6))

	# 2.2 给点着色 - (使用颜色映射Blues着色的随机漫步图)
	point_numbers = list(range(rw.num_points))

	# 2.3 突出起点和终点
	# plt.scatter(0, 0, c = 'green', edgecolor = 'none', s = 100)
	
	# plt.scatter(rw.x_values[-1], rw.y_values[-1], c = 'red', edgecolor = 'none', s = 100)
	# plt.scatter(rw.x_values, rw.y_values, c = point_numbers, cmap = plt.cm.Blues, edgecolor = 'none', s = 15)

	# 2.4 增加点数
	# plt.scatter(rw.x_values, rw.y_values, c = point_numbers, cmap = plt.cm.Blues, edgecolor = 'none', s = 1)
	
	# 2.6 模拟花粉在水滴表面的运动路径
	plt.plot(rw.x_values, rw.y_values, linewidth = 3)

	# 隐藏坐标轴
	plt.axes().get_xaxis().set_visible(False)
	plt.axes().get_yaxis().set_visible(False)
	plt.show()

	keep_running = input("Make another walk? (y/n): ")
	if keep_running == 'n':
		break