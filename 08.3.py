def is_palyndrome(string):
    if string == string[::-1]:
        return "É um palíndromo"
    else:
        return "Não é um palíndromo"
print(is_palyndrome("reviver"))