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
    for _ in range(17):
        if esquerda == direita:
            return False
        meio = esquerda+((direita-esquerda)//2)
        if t[meio]>palavra:
            direita=meio-1
        elif t[meio]<palavra:
            esquerda=meio+1
        elif t[meio]==palavra:
            return True
    return False

def percorre_lista():
    t=append()
    for i in t:
        if in_bisect(t,i[::-1]):
            print(i,i[::-1])

percorre_lista()