# name=["jSion","stenwaveS","steFAn","Waves"]
# result=list(map(lambda x:x.capitalize(),name))
# print(result)
from functools import reduce
Str="123.45645"
index=Str.find('.')
def demo(s):
	digits={'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
	return digits[s]
def fn(x,y):
	return x*10+y
def fn1(x,y):
	return 0.1*x+y
print(Str[index+1:][::-1])

print(reduce(fn,map(demo,Str[:index]))+reduce(fn1,map(demo,Str[index+1:][::-1]))*0.1)
print(float(Str))