from functools import reduce

def Fibonacci_seq(n):
	'''n:the number of Fibonacci sequence'''
	a,b=1,1
	result=[]
	while n:
		result.append(a)
		a,b=b,a+b
		n-=1
	return result
# print(reduce(lambda x,y:x*y,range(1,6)))
# seq=["d145","41ee",",skij"]
# print(list(filter(lambda x:x.isalnum(),seq)))




