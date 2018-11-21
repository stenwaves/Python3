class Student(object):
	"""docstring for Student"""
	def __init__(self,name,score):
		# if not isinstance(str,name):
		# 	raise ValueError
		# if score>100 or score<0:
		# 	raise ValueError
		self.__score = score
		self.__name = name
	# def get_name(self):
	# 	if not isinstance(str,name):

	# 	print("The student's name is %s" %self.__name)
	def get_grade(self):
		if not isinstance(self.__score,int):
			raise ValueError
		if self.__score>100 or self.__score<0 :
			raise ValueError
		if self.__score >= 80:
			return 'A'
		elif self.__score >= 60:
			return 'B'
		return 'C'
	# def set_sex(self,sex):
	# 	if not isinstance(sex,str):
	# 		print("error! not a string")
	# 		return
	# 	self.__sex=sex
	def get_name(self):
		if not isinstance(self.__name,str):
			raise ValueError
		return self.__name

		 