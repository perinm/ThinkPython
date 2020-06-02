import unidecode

def uses_all(s,l):
	lista1=[]
	for letter in l:
		if letter in s:
			lista1.append(letter)
	return lista1 == l

fin = open('words.txt')
stringc = ""
while True:
	a = unidecode.unidecode(input("Caracter(s) proibido ou '0' para parar de adicionar: "))
	if a == '0':
		break
	stringc+=a

lista = []

for line in fin:
	word=line.strip()
	if uses_all(word,list(stringc)):
		lista.append(word)

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
print(2*'\n'+str(c)+' palavras achadas com a string:',stringc,'\n')