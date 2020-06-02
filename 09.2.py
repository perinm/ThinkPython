def has_no_e(s):
    for letter in s:
        if letter == 'e':
            return False
    return True

fin = open('words.txt')
line = fin.readline()
Ce=0
Se=0
for line in fin:
    word = line.strip()
    if has_no_e(word):
        Se+=1
    else:
        print(word)
        Ce+=1

print("Porcentagem de palavras que não contêm é: "+str(round(100*(Se/(Se+Ce)),2))+"%")
print("Porcentagem de palavras que contêm é: "+str(round(100*(Ce/(Se+Ce)),2))+"%")
