import time,random,os
from multiprocessing import Pool

def long_time_task(name):
	print('task %s(%s) is running' %(name,os.getpid()))
	start=time.time()
	time.sleep(random.random()*4)
	end=time.time()
	print('task %s(%s) has tasted %2.5f' % (name,os.getpid(),(end-start)))

if __name__=='__main__':
	print('parent process %s' % os.getpid())
	p=Pool()
	for i in range(5):
		p.apply_async(long_time_task,args=(i,))
	p.apply_async(long_time_task,args=(2,))
	print('waiting for all subprocess done...')
	p.close()
	p.join()
	print('all subprocess done...')

