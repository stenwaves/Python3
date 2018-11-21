from queue import *
import json

def queue2list(q):
	reslut={}
	temp=[]
	while not q.empty():
		temp.append(q.get())
	reslut["0"]=temp
	return reslut
def list2queue(dict):
	q=Queue()
	for i in dict['value']:
		q.put(i)
	return q



q=Queue()
for i in range(8):
	q.put(i)


# print(q)
json_str=json.dumps(q,default=queue2list)
print(type(json_str),json_str)
# reslut_q=json.loads(json_str,object_hook=list2queue)
# print(reslut_q)
# if not reslut_q.empty():
# 	print(reslut_q.get())
# x=list2queue({'value': [0, 1, 2, 3, 4, 5, 6, 7]})
# if not x.empty():
# 	print(x.get())


