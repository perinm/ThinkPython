def cumsum(lista):
	l=[]
	for i in range(len(lista)):
		total=0
		for i in range(i+1):
			total+=lista[i]
		l.append(total)
	return l

t = [1,2,3]
print(cumsum(t))