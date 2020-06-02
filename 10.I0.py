def append():
	t=[]
	fin = open('words.txt')
	for line in fin:
		word = line.strip()
		t.append(word)
	return t

def in_bisect(t,palavra):
	esquerda=0
	direita=len(t)
	for i in range(17):
		meio = esquerda+((direita-esquerda)//2)
		if t[meio]>palavra:
			direita=meio-1
		elif t[meio]<palavra:
			esquerda=meio+1
		else:
			return meio+1
	return "\nEm nenhuma linha, palavra não encontrada!"

palavra = "bookkeepers"

print("A palavra",palavra,"está contida na linha:",in_bisect(append(),palavra))