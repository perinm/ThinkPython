import turtle

def draw(t,length,n):
  if(n==0):
    return
  angle=50
  t.fd(length*n)
  t.lt(angle)
  draw(t,length,n-1)
  t.color("blue")
  t.rt(2*angle)
  draw(t,length,n-1)
  t.color("red")
  t.lt(angle)
  t.bk(length*n)


screen.setup (width=200, height=200, startx=0, starty=0)
t=turtle.Turtle()
t.speed(0)
t.tracer(1,0)
draw(t,5,9)