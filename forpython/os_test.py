import os
from stat import *
# dir=os.path.join(os.path.abspath('.'),'testdir')
# try:
# 	os.mkdir(dir)
# except FileExistsError as e:
# 	print(e)
# finally:
# 	os.rename(os.path.split(dir)[1],'testDir')
# 	os.rmdir('testDir')
# 	# print('delete %s' %os.path.split(dir)[1])
# List=[x for x in os.listdir('.') if os.path.isdir(x)]
# print(List)
# List_file=[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
# print(List_file)	
dir=os.path.join(os.path.abspath('.'))
print(dir)
print(os.stat(dir))
print(S_IMODE(os.stat(dir).st_mode))