import math,copy

class Point:
	def __init__(self,x,y):
		self.x = x
		self.y = y
	
	def __str__(self):
		return "(%g, %g)" % (p.x, p.y)

class Circle:
	def __init__(self,x,y,r):
		self.center = Point(x,y)
		self.radius = r

class Rectangle:
	def __init__(self,w,h,x,y):
		self.width = w
		self.height = h
		self.corner = Point(x,y)

def point_in_circle(circulo,ponto):
	dx = ponto.x - circulo.center.x
	dy = ponto.y - circulo.center.y
	d = math.sqrt(dx**2+dy**2)
	if d>circulo.radius:
		return "O ponto está fora do círculo"
	elif d==circulo.radius:
		return "O ponto está contido na linha da circuferência do círculo"
	else:
		return "O ponto está dentro da circuferência do círculo"

def rect_in_circle(circulo,rect):
	p = copy.copy(rect.corner)
	print(p)
	if not point_in_circle(circulo,p):
		return False
	
	p.x += rect.width
	print(p)
	if not point_in_circle(circulo,p):
		return False
	
	p.y -= rect.height
	print(p)
	if not point_in_circle(circulo,p):
		return False
	
	p.x -= rect.width
	print(p)
	if not point_in_circle(circulo,p):
		return False
	
	return True

def rect_circle_overlap(circulo,rect):

	p = copy.copy(rect.corner)
	print(p)
	if point_in_circle(circulo,p):
		return True
	
	p.x += rect.width
	print(p)
	if point_in_circle(circulo,p):
		return True
	
	p.y -= rect.height
	print(p)
	if point_in_circle(circulo,p):
		return True
	
	p.x -= rect.width
	print(p)
	if point_in_circle(circulo,p):
		return True
	
	return False

c = Circle(0,0,75)
p = Point(50,50)
box = Rectangle(50,50,0,0)

print(point_in_circle(c,p),'\n')

print("Retângulo está por inteiro dentro do círculo?")
print(rect_in_circle(c,box),'\n')

print("Alguma quina do retângulo está dentro do círculo?")
print(rect_circle_overlap(c,box))