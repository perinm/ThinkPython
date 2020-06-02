def has_duplicates(t):
	t1=t[:]
	t2=[]
	while t1:
		t2.append(t1.pop(0))
		print(t1,t2)
		if t2[-1] in t1:
			return True
	return False

t=[2,3,4,5,1,6,7,8,1]
print(has_duplicates(t))