d={}
keys=[]
vals=[]
for i in range(0,3):
	vals.append(input("enter name: "))
	keys.append(input("enter usn: "))
for i in keys:
	for j in vals:
		d[i]=j
		vals.remove(j)
		break
print(d)