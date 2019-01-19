import time

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

def percorre_lista(t):
    for w1 in t:
        print(w1)
        start_time = time.time()
        for w2 in t:
            w=interliga(w1,w2)
            if in_bisect(t,w):
                print("As palavras",w1,"e",w2,"reorganizadas juntas dão:",w)
            w=interliga(w2,w1)
            if in_bisect(t,w):
                print("As palavras",w2,"e",w1,"reorganizadas juntas dão:",w)
        print("--- %s seconds ---" % (time.time() - start_time))

def interliga(w1,w2):
    w=""
    for i in range(len(w1+w2)):
        if i<len(w1):
            w+=w1[i]
        if i<len(w2):
            w+=w2[i]
    return w

t=append()
percorre_lista(t)