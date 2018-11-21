import os,re

def search_str(dir):
	Str='test'
	pattern=re.compile(Str)
	for i in os.listdir(dir):
		abs_path=os.path.abspath(os.path.join(dir,i))
		if not os.path.isdir(abs_path):
			if pattern.search(i):
				print(abs_path)
		else:
			search_str(abs_path)
if __name__=='__main__':
	dir='/home/stenwaves/'
	search_str(dir)
