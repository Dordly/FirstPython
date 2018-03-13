import random, time, Queue
from multiprocessing.managers import BaseManager

# 1. 创建task_queue和result_queue,存放任务和结果
task_queue = Queue.Queue()
result_queue = Queue.Queue()

class Queuemanager(BaseManager):
	pass
	# 2. 将创建的两个队列注册到网络上，并利用register方法来讲callable参数关联到Queue对象上
	# 并将Queue对象暴露在网络上
	Queuemanager.register('get_task_queue', callable = lambda:task_queue)
	Queuemanager.register('get_result_queue', callable = lambda:result_queue)

	# 3. 绑定端口8001,设置验证口令，‘qiye’相当于对对象的初始化
	manager = Queuemanager(address = ('', 8001), authkey = 'qiye')

	# 4. 启动关联，监听信息通道
	manager.start()

	# 5. 通过管理实例的方法来获得通过网络访问的Queue对象
	task = manager.get_task_queue()
	result = manager.get_result_queue()

	# 6. 添加任务
	for url in ["ImageUrl_" + i for i in range(10)]:
		print ('put task %s ...' %url)

	# 7. 获取返回结果
	print ('try get result ...')
	for i in range(10):
		print ('result is %s ' %result.get(timeout = 10))

	# 8. 关闭管理
	manager.shutdown()
