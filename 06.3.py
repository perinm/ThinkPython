def first(word):
  return word[0]

def last(word):
  return word[-1]

def middle(word):
  return word[1:-1]

def is_palyndrome(word):
  print(word)
  if(first(word)==last(word)):
    a=len(word)-1
    s=""
    for _ in range(a-1):
      a=a-1
      s+=word[a]
    print("Meio é igual a",middle(word),"e meio inverso é igual a",s)
    if(s==middle(word)):
      return True
  else:
    return False

print(is_palyndrome("reviver"))