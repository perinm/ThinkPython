def nested_sum(lista):
	sum=0
	for i in lista:
		for i in i:
			sum+=i
	return sum

t = [[1,2],[3],[4,5,6]]
print(nested_sum(t))