# class Student(object):
# 	"""docstring for Student"""
# 	def __init__(self, arg):
# 		self.arg = arg
# 	def __call__(self,*args,**kwargs):
# 		print(args,kwargs)
# obj=Student('lee')
# obj(1,2,3,k=2)
from enum import Enum
week=Enum('week',('jjjj','hello'))
for name,member in week.__members__.items():
	print(name,"=>",member,',',member.value)
