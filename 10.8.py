import random

def has_duplicates(t):
	t1=t[:]
	t2=[]
	i=0
	while t1:
		t2.append(t1.pop(0))
		if t2[-1] in t1:
			return True
	return False

casos=100000
casospositivos=0
for i in range(casos):
	turma=[]
	for i in range(23):
		turma.append(random.randint(1,365))
	if has_duplicates(turma):
		casospositivos+=1

chance=(casospositivos/casos)*100

print("A chance para umas amostra de",casos,"casos é de",str(chance)+"%.")
print("Foram simulados",casos,"casos com 23 estudantes.")
print("Com",casospositivos,"casos onde houve pelo menos uma correspondência.")