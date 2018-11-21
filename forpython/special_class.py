# class Student(object):
# 	"""docstring for Student"""
# 	def __init__(self, name):
# 		self.name = name
# 	def __str__(self):
# 		return'just a test %s'% self.name
# obj=Student('sweke')
# print(str(obj))
# print(Student('stefen'))
class fib(object):
	"""docstring for fib"""
	# def __init__(self, arg):
	# 	super(fib, self).__init__()
	# 	self.arg = arg
	# def __getitem__(self,n):

	# 	pass
	def __init__(self):
		self.a,self.b=0,1
	
	def __iter__(self):
		return self

	def __next__(self):
		self.a,self.b=self.b,self.a+self.b
		return self.a
	def __getitem__(self,n):
		if isinstance(n,int):
			if n>10000:
				raise ValueError('range of fib must be less than 10000')
			a,b=1,1
			while n:
				a,b=b,a+b
				n-=1
			return a
		if isinstance(n,slice):
			start=n.start
			stop=n.stop
			step=n.step
			if step==None:
				step=1
			if stop>10000:
				raise ValueError('the range of slice must be less than 10000')
			if start==None:
				start=0
			if stop==None:
				stop=10000
			if step>(stop-start):
				raise ValueError('step must be less than range of slice')
			List=[]
			a,b=1,1
			for i in range(start,stop):
				if step==1:
					List.append(a)
				elif(i-start)%step==0:
					List.append(a)
				a,b=b,a+b
			return List

f=fib()
print(f[:15])
print(f[:15:2])