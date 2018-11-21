def Yh_triangles():
	line=[1]
	while True:
		temp=[]
		yield line
		for i in range(len(line)-1):
			temp.append(line[i]+line[i+1])
		line=[1]+temp+[1]
result=Yh_triangles()
for i in range(10):
	print(next(result))