class Student(object):
	"""docstring for Student"""
	count=0
	def __init__(self, name):
		self.name = name
		self.__class__.count+=1

if Student.count!=0:
	print("test failed")
elif Student("lee") and Student.count!=1:
	print("test failed")
elif Student("nani") and Student.count!=2:
	print("test failed")
else:
	print('the number of student is %s' %Student.count)
	print("test success")

	


		