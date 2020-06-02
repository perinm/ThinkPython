import math

def mysqrt(a,x):
  while 1:
    y=(x+a/x)/2
    if y == x:
      return y
    x=y

def test_square(a,x):
  y=str(mysqrt(a,x))
  z=str(math.sqrt(a))
  print(str(float(a))+"  "+y+" "*(19-len(y))+z+" "*(19-len(z))+str(abs(float(y)-float(z))))

myy="mysrt(a)"
mat="math.sqrt(a)"
dif="diff"
print("a    "+myy+" "*(19-len(myy))+mat+" "*(19-len(mat))+dif)
print("-    "+"-"*len(myy)+" "*(19-len(myy))+"-"*len(mat)+" "*(19-len(mat))+"-"*len(dif))
for i in range (1,150):
  test_square(i,i)