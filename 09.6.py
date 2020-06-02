def is_abcederian(s):
	for x,y in zip(s[::],s[1::]):
		if ord(x)>ord(y):
			return False
	return True

fin = open('words.txt')
lista=[]

n=4
c=0
count=0
l=[]
for line in fin:
	word=line.strip()
	if len(word)>n:
		if is_abcederian(word):
			l.append(word)
			print(word)
			c+=1
			count+=1
			if c==5:
				lista.append(l)
				
				l=[]
				c=0

print('\n',count,lista[-1])
print("Palavras com mais de",str(n),"letras.")
if not lista:
	print("Não há palavras com mais de",str(n),"letras.")

c=0
print('')
for element in lista:
	if c%3==0:
		print(element)
		print(('_'*70)+'\n',end=(""))
	else:
		print(element,end=('\t\t|\t'))
	c+=1
print('\n'+('_'*70))