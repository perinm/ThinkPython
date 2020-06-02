#funcao que verifica palindromo
def palin(i,comeco,tam):
	s=str(i)[comeco:comeco+tam]
	return s==s[::-1]

#funcao que compara 4 casos
def check(i):
	return (palin(i,2,4) and
					palin(i+1,1,5) and
					palin(i+2,1,4) and
					palin(i+3,0,6))

#testando todos os numeros
for i in range(100000,999996):
	if(check(i)):
		print(i)