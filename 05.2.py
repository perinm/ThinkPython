def check_fermat(a,b,c,n):
  if(a**n+b**n==c**n):
    print("Holy smokes, Fermat was wrong!")
  else:
    print("No, that doesn't work")
    
a=int(input("Digita a:\n"))
b=int(input("Digite b:\n"))
c=int(input("Digite c:\n"))
n=int(input("Digite n:\n"))

check_fermat(a,b,c,n)