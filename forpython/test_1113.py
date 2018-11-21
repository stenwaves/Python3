from multiprocessing import Process,Queue
import os,time,random

def write(q):
	print('write process %s' %os.getpid())
	for i in range(3):
		print('put %s to queue' %i)
		q.put(i)
		time.sleep(random.random())
def read(q):
	print('read process %s' %os.getpid())
	while True:
		value=q.get(True)
		print('get %s from queue' %value)
		
if __name__=='__main__':
	q=Queue()
	pw=Process(target=write,args=(q,))
	pr=Process(target=read,args=(q,))
	pw.start()
	pr.start()
	pw.join()
	pr.terminate()