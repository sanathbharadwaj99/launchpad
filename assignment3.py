num=[1, 2, 3, 2, 0, 65, 21, 4, 2, 10]
x=2
y=[]
for i in range(0,len(num)):
	if num[i]==x:
		y.append(i)
print(y)