import unidecode

while True:
	s = unidecode.unidecode(input("Digite string que quer rotacionar: "))
	while True:
		print("\nDigite número inteiro negativo ou\npositivo que gostaria de rotacionar, até 25): ")
		try:
			decimal = int(input())
		except ValueError:
			print("Please enter a number.")
			continue
		binary = bin(decimal)[2:]
	if i >= 0:
		i = i%25
	elif(i < 0):
		i = -1*(abs(i)%25)
	l=[]
	for c in s:
		if c.islower():
			if((ord(c)+i)>122):
				c = chr(96+i-(122-ord(c)))
			elif(ord(c)+i<97):
				c = chr(123+i-(ord(c) - 97))
			else:
				c = chr(ord(c)+i)
		elif c.isupper():
			if((ord(c)+i)>90):
				c = chr(64+i-(90-ord(c)))
			elif((ord(c)+i)<65):
				c = chr(91+i-(ord(c) - 65))
			else:
				c = chr(ord(c)+i)
		l.append(c)

		print("Sua string rotacionada é:\n\n[",end=(""))
		for i in l:
			if(i=='\x89'):
				print(' ',end=(''))
			else:
				print(i,end=(''))
	print("]\n\n")