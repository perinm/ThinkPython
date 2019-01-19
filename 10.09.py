import time

def append():
	t=[]
	fin = open('words.txt')
	for line in fin:
		word = line.strip()
		t.append(word)
	return t

def concatena():
	t=[]
	fin = open('words.txt')
	for line in fin:
		word = line.strip()
		t+=[word]
	return t

def extend():
	t=[]
	fin = open('words.txt')
	for line in fin:
		word = line.strip()
		t.extend([word])
	return t

fin = open('words.txt')

start_time = time.time()
t=append()

print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
t=concatena()

print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
t=extend()

print("--- %s seconds ---" % (time.time() - start_time))