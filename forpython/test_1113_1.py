import os,time,random,sys
from multiprocessing import Queue


def write(q):
	print('write process %s' %os.getpid())
	for i in range(3):
		print('put %s to queue' %i)
		q.put(i)
		time.sleep(random.random())
def read(q):
	print('read process %s' %os.getpid())
	while True:
		value=q.get()
		print('get %s from queue' %value)
if __name__=='__main__':
	print('parent process is %s' %os.getpid())
	q=Queue()
	pid=os.fork()
	if pid==0:
		write(q)
		print('exit writeprocess %s' %os.getpid())
		os._exit(0)
	else:
		pid_1=os.fork()
		if pid_1==0:
			read(q)