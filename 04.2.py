import math,turtle

def polygon(t,n,length):
  angle=360/n
  for i in range(n):
    t.fd(length)
    t.lt(angle)

def circle(t,r):
  circumference=2*math.pi*r
  n = 50
  length = circumference/n
  polygon(t,n,length)

def polyline(t, n, length, angle):
    """Draws n line segments.

    t: Turtle object
    n: number of line segments
    length: length of each segment
    angle: degrees between segments
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def arc(t, r, angle):
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
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)

bob=turtle.Turtle()
bob.speed(10)
a=bob.pos()
n=15
for _ in range (n*2):
  bob.pu()
  bob.setpos(a)
  bob.pd()
  arc(bob,200,20*[1,-1][_%2==0])
  if(_%2==0):
    bob.lt(360/n)