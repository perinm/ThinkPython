import unidecode

def uses_only(s,l):
	for letter in s:
		if not letter in l:
			return False
	return True

fin = open('words.txt')
line = fin.readline()
stringc = ""
while True:
	a = unidecode.unicode(input("Caracter(s) proibido ou '0' para parar de adicionar: "))
	if a == '0':
		break
	stringc+=a

lista = []

for line in fin:
	word=line.strip()
	if uses_only(word,list(stringc)):
		lista.append(word)

c=0
for element in lista:
	print(element,end=(5*" "))
	if c%7==0:
		print('\n'+('-'*70)+'\n',end=(""))
	c+=1
print('\n')
