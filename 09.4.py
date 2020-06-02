import unidecode

def uses_only(s,l):
	for letter in s:
		if letter not in l:
			return False
	return True

word = unicode.unicode(input("Digite palavra: "))
lista = []
while True:
	a = unicode.unicode(input("Caracter proibido ou '0' para parar de adicionar: "))
	if a == '0':
		break
	lista.append(a)

print(uses_only(word,lista))