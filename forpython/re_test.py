import re

# pattern=re.compile(r'\b\w+s\b')
# example='a new day not new start symbols ???'
# print(pattern.sub('good',example))

# matchobj=re.search('(.*) not (.*?) ',example)
# print(matchobj.group())
telNumber = '''Suppose my Phone No. is 0535-1234567,
yours is 010-12345678, his is 025-87654321.'''
pattern = re.compile(r'(\d{3,4})-(\d{7,8})')
index=0
flag=1
while True:
	match_result=pattern.search(telNumber,index)
	if not match_result:
		break
	print(f'''telNumber {flag} is :{match_result.group(1)}-{match_result.group(2)},and it starts from {match_result.start()},end with {match_result.end()}''')
	index=match_result.end()+1
	flag+=1