def avoids(s,l):
	for letter in s:
		if letter in l:
			return False
	return True

fin = open('words.txt')
line = fin.readline()
l = ''
while True:
	a=input("Digite letra proibida ou '0' para parar de adicionar elementos: ")
	if(a=='0'):
		break
	l+=a
for line in fin:
	word = line.strip()
	if avoids(word,l):
		print(word)