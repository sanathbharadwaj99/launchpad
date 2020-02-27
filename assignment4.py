num=[1, 1, 2, 3, 4, 64, 35, 93, 35, 87, 4, 3]
x=[]
for i in num:
	if i not in x:
		x.append(i)
print(x)