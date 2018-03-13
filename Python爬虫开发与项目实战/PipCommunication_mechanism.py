# pip通信机制
import multiprocessing
import random
import time,os

# pip发送机制
def proc_send(pipe, urls):
	for url in urls:
		print ('Process(%s) send: %s' %(os.getpid(), url))
		pipe.send(url)
		time.sleep(random.random())

# 注：输出语句格式 print(''),不能使用print " ",----语法错误

# pip接收机制
def proc_recv(pipe):
	while True:
		print ('Process(%s) rev: %s' %(os.getpid(), pipe.recv()))
		time.sleep(random.random())

if __name__ == "__main__":
	pipe = multiprocessing.Pipe()
	p1 = multiprocessing.Process(target = proc_send, args = (pipe[0], ['url_'+str(i) 
		for i in range(10)
			]))
	p2 = multiprocessing.Process(target = proc_recv, args = (pipe[1],))
	p1.start()
	p2.start()
	p1.join()
	p2.join()



















































