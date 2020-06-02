import turtle,math

def is_triangle(l1,l2,l3):
  return not(l1+l2<=l3 or l1+l3<=l2 or l2+l3<=l1)

def polyline(t, n, length, angle,l):
    """Draws n line segments.

    t: Turtle object
    n: number of line segments
    length: length of each segment
    angle: degrees between segments
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)
        x=t.xcor()
        y=t.ycor()
        l.append((round(x,0),round(y,0)))
    return l

def arc(t, r, angle,l):
    """Draws an arc with the given radius and angle.

    t: Turtle
    r: radius
    angle: angle subtended by the arc, in degrees
    """
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n

    # making a slight left turn before starting reduces
    # the error caused by the linear approximation of the arc
    t.lt(step_angle/2)
    l=polyline(t, n, step_length, step_angle,l)
    t.rt(step_angle/2)
    return l

def circulo(t,r,a,l):
  t.pu()
  t.seth(0)
  t.fd(r)
  t.seth(90)
  t.pd()
  l=arc(t,r,a,l)
  t.pu()
  return l

'''
def circulocentro(t,r,a):
  t.pu()
  t.seth(0)
  t.fd(r)
  t.seth(90)
  t.pd()
  t.circle(r,a)
  t.pu()

a=float(input("Digita a:\n"))
b=float(input("Digite b:\n"))
c=float(input("Digite c:\n"))


print(["No","Yes"][is_triangle(a,b,c)])

t=turtle.Turtle()
t.fd(a)
t.color("blue")
circulocentro(t,b,-270)
t.home()
circulocentro(t,c,90)
'''

a=b=120
c=150
print(["No","Yes"][is_triangle(a,b,c)])

t=turtle.Turtle()
t.tracer(1,0)
home=t.pos()
t.fd(a)
home2=t.pos()
t.color("blue")
l1=[]
l2=[]
ab=circulo(t,b,175,l1)
print(len(l1))
print(l1)
t.home()
ac=circulo(t,c,175,l2)
print(len(l2))
print(l2)
if(len(l1)>len(l2)):
  for i in range(len(l2)):
    if(l2[i] in l1):
      print(l2[i])