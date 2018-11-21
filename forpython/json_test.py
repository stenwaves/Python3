import json
class human(object):
	"""docstring for human"""
	def __init__(self, run):
		self.run = run
		
class Student(human):
	"""docstring for Student"""
	def __init__(self, name, age, sex):
		super().__init__(run=3)
		self.name = name
		self.age = age
		self.sex = sex
	def get_name(self):
		return self.name
def student2dict(std):
	return{
	'name':std.name,
	'age':std.age,
	'sex':std.sex
	}
def dict2student(json_str):
	return Student(**json_str)
s=Student('lee',20,'girl')
if __name__=='__main__':
	json_str=json.dumps(s,default=student2dict)
	with open('./test_1112.txt','w') as fp:
		fp.write(json_str)
	print(json_str)
	std=json.loads(json_str,object_hook=dict2student)
	print(std.run)
	print(std)



		