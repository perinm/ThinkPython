def MDC(a,b):
  if b == 0:
    return a
  else:
    resto=a%b
  if resto == 0:
    return b
  else:
    return MDC(b,resto)

print(MDC(17,4))