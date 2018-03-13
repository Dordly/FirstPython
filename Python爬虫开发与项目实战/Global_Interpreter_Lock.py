#  全局解释器锁 ---- GIL(Global Interpreter Lock)
#  协程 - 微线程、纤程 ，是一种用户级的轻量级线程，有自个儿的寄存器上下文和栈

#  gevent是一个基于协程的Python网络函数库

from gevent import monkey
monkey.patch_all()
import gevent
import urllib2

def run_task(url):
	print ('Visit ---> %s' % url)
	try:
		response = urllib2.urlopen(url)
		data = response.read()
		print ('%d bytes received from %s.' % (len(data), url))
	except Exception as e:
		print (e) 
if __name__ == '__main__':
	urls = ['https://github.com/', 'https://www.python.org/', 'http://www.cnblogs.com/']
	greenlets = [gevent.spawn(run_task, url) for url in urls  ]
	gevent.joinall(greenlets)










































