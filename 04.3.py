import turtle,math

def isosceles(t,n,lint):
  a=360.0/n
  a2=(180-a)/2.0
  length=math.sin(math.radians(a/2))*lint
  if(round(t.heading(),0)==0 or round(t.heading(),0)==180):
    t.color('red')
  if(round(t.heading(),0)==90 or round(t.heading(),0)==270):
    t.color('blue')
  if(round(t.heading(),0)==45 or round(t.heading(),0)==225 or round(t.heading(),0)==135 or round(t.heading(),0)==315):
    t.color('purple')
  t.fd(lint)
  t.color('black')
  t.rt(180-a2)
  t.fd(length*2)
  t.rt(180-a2)
  if(round(t.heading(),0)==0 or round(t.heading(),0)==180):
    t.color('red')
  if(round(t.heading(),0)==90 or round(t.heading(),0)==270):
    t.color('blue')
  if(round(t.heading(),0)==45 or round(t.heading(),0)==225 or round(t.heading(),0)==135 or round(t.heading(),0)==315):
    t.color('purple')
  t.fd(lint)
  t.color('black')
  t.lt(180)

t=turtle.Turtle()
t.speed(0)
r=200
n=4
l=125
angle=360/n
a2=(180-angle)/2
li=float(l/2)/math.sin(math.radians(angle/2))
t.pu()
t.setpos(-1000+li,1000-li*1.5)
t.pd()
for i in range (r):
  for _ in range (n):
    isosceles(t,n,li)
  n=n+4
  t.seth(0)
  t.pu()
  t.fd(li*2)
  if(t.xcor()>=1000-li*0.99):
    t.setpos(-1000+li,t.ycor()-li*2)
  t.pd()