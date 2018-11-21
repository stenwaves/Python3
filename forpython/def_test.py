# def scope_test():
# 	def local_test():
# 		variable="one day and one night"
# 	def nonlocal_test():
# 		nonlocal variable
# 		variable="not just today"
# 	def global_test():
# 		global variable
# 		variable="a better day"
# 	variable="holy shit"
# 	# global a
# 	# a="stand by"
# 	local_test()
# 	print(variable)
# 	nonlocal_test()
# 	print(variable)
# 	global_test()
# 	print(variable)
# scope_test()
# print(variable)
# def demo(*p):
# 	average=sum(p)/len(p)
# 	x=tuple([i for i in p if i>average])
# 	return (average,)+x
# print(demo(2,4,5,5,7))
# import random
# def demo(k,seq):
# 	x=list(reversed(seq[:k]))+list(reversed(seq[k:]))
# 	z=list(reversed(x))
# 	print(z)
# list_test=[random.randint(0,100) for i in range(20)]
# k=random.randint(-19,20)
# print(k)
# print(list_test)
# demo(k,list_test)
import random

def Quciksort(List,First,Last):
	global k
	if First>Last:
		return
	key=List[First]
	i=First
	j=Last
	while i<j:
		while i<j and List[j]>=key:
			j-=1
		List[i]=List[j]
		while i<j and List[i]<=key:
			i+=1
		List[j]=List[i]
	if i==j:
		k=k+1
	List[j]=key
	Quciksort(List,First,i-1)
	Quciksort(List,i+1,Last)
k=0
List=random.sample(range(1,50),20)
random.shuffle(List)
Quciksort(List,0,(len(List)-1))
print(k)
print(List)

