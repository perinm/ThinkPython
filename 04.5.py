import turtle,math

def polyline(t,n,length,angle):
  for i in range(n):
    t.fd(length)
    t.lt(angle)

def arc(t,r,angle):
  arc_length=2*math.pi*r*angle/360
  n = int(arc_length/3)+1
  step_length=arc_length/n
  step_angle=float(angle)/n
  polyline(t,n,step_length,step_angle)
  
bob=turtle.Turtle()
bob.speed(0)
r=500
ri=4
for i in range(1,r):
  arc(bob,(ri**((i/math.pi)*(math.log10(1.618))*(1.618))),(90))