def cartalk(s):
	c=0
	i=0
	while i < len(s)-1:
		if s[i]==s[i+1]:
			c+=1
			i+=2
			if c==3:
				return True
		else:
			c=0
			i+=1
	return False

fin = open('words.txt')
l=[]
n=5
for line in fin:
	word=line.strip()
	if len(word)>n:
		if cartalk(word):
			l.append(word)
			print(word)