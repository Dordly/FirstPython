# ------- 多线程 -------

#  使用threading模块来创建多线程

#   1. 将一个函数传入并创建Thread实例，并调用start来执行

# import random 
# import time, threading
# # 新线程要执行的代码
# def thread_run(urls):
# 	print ('Current %s is running ...' % threading.current_thread().name)
# 	for url in urls:
# 		print('%s ----->>> %s' % (threading.current_thread().name, url))
# 		time.sleep(random.random())
# 	print ('%s ended.' % threading.current_thread().name)

# print ('%s is running ....' % threading.current_thread().name)
# t1 = threading.Thread(target = thread_run, name = 'Thread_1', args = (['url_1', 'url_2', 'url_3'], ))
# t2 = threading.Thread(target = thread_run, name = 'Thread_2', args = (['url_4', 'url_5', 'url_6'], ))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print ( '%s ended.' % threading.current_thread().name)



#  2.从threading.Thread继承创建线程类，下面将方法一的程序进行重写

import random 
import threading
import time
class myThread(threading.Thread):
	"""pip线程通信机制"""
	def __init__(self, name, urls):
		threading.Thread.__init__(self, name = name)
		self.urls = urls

	def run(self):
		print ('Current %s is running...' % threading.current_thread().name)
		for url in self.urls:
			print ('%s ---->>> %s' % (threading.current_thread().name,url))
			time.sleep(random.random())

		print('%s ended.' % threading.current_thread().name)
print ('%s is running...' % threading.current_thread().name)

t1 = myThread(name = 'Thread_1', urls = ['url_1', 'url_2', 'url_3'])
t2 = myThread(name = 'Thread_2', urls = ['url_4', 'url_5', 'url_6'])
t1.start()
t1.join()
t2.start()
t2.join()

		






























