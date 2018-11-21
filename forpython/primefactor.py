import math
import random
from functools import reduce

def isprimes(number):
	for i in range(2,int(math.sqrt(number))+1):
		if number%i==0:
			return False
	return True
def primes(number):
	return [i for i in range(2,number+1) if 0 not in [i%j for j in range(2,int(math.sqrt(i))+1)]]
def primesfactor(number):
	global result
	if not isinstance(number,int) or number==1:
		return
	for i in primes(number):
		if number!=1 and number%i==0:
			result.append(i)
			number=number//i
			break
	primesfactor(number)
	return result
def factor_func(number):
	global result_factor
	global factor_one
	# if not isinstance(number,int) or isprimes(number):
	# 	return
	temp=[]
	for i in range(2,int(math.sqrt(number))+1):
		if number%i==0 :
			number=number//i
			factor_one.append(i)
			factor_one.append(number)
			temp=[i for i in factor_one]
			# print(factor_one)
			# print(temp)
			del factor_one[-1]
			result_factor.append(temp)
			factor_func(number)
			if isprimes(number):
				return
# data=[random.randint(100,1000) for i in range(50)]
# for i in data:
# 	result=[]
# 	r=primesfactor(i)
# 	r_test=reduce(lambda x,y:x*y,r)
# 	print(i,"=",r,i==r_test)
result_factor=[]
factor_one=[]
The_integer=24
factor_func(The_integer)
result_factor.append([1,The_integer])
print(result_factor)







