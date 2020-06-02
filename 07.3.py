import math

def fat(a):
  if(a==1 or a==0):
    return 1
  else:
    return a*fat(a-1)

def estimate_pi():
  total = 0
  k = 0
  factor = 2*math.sqrt(2)/9801
  while True:
    num = fat(4*k)*(1103+26390*k)
    den = fat(k)**4 * 396**(4*k)
    term = factor * num / den
    total += term

    if abs(term) < 1e-15:
      break
    
    k += 1
  
  return 1/total

print(estimate_pi())