def eval_loop(s):
  return eval(s)

while True:
  a=(input())
  if(a.lower()=='done'):
    break
  s=eval_loop(a)
  print(str(s))

print(str(s))