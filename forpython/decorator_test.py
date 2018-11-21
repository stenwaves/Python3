import time
import random
import functools
def log(text):
	def decorator_test(func_test):
		@functools.wraps(func_test)
		def log_print():
			print("%s:%s() "% (text,func_test.__name__))
			start=time.time()
			print(f'the result of executing {func_test.__name__} is {func_test()}')
			print("%s() has executed"% func_test.__name__)
			return f'executing {func_test.__name__} tastes {time.time()-start}',func_test()
		return log_print
	return decorator_test
@log("execute")
def demo():
	List=[i for i in range(2000)]
	return functools.reduce(lambda x,y:x+y,List)

print(demo())