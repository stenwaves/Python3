from multiprocessing import Process
import threading
import os


print('Process %s is running'%os.getpid())
print('thread %s is running'%threading.current_thread().name)