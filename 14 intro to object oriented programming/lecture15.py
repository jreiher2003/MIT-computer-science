import math
class cPoint:
	def __init__(self,x,y):
		self.x = x
		self.y = y
		self.radius = math.sqrt(self.x*self.x + self.y * self.y)
		self.angle = math.atan2(self.y, self.x)

	def cartesian(self):
		return (self.x, self.y)

	def polar(self):
		return (self.radius, self.angle)

	def __str__(self):
		return '(' + str(self.x) + ', ' + str(self.y) + ')'

	def __cmp__(self,other):
		return (self.x > other.x) and (self.y > other.y)

class pPoint:
	def __init__(self,r,a):
		self.radius = r
		self.angle = a
		self.x = r * math.cos(a)
		self.y = r * math.sin(a)

	def cartesian(self):
		return (self.x, self.y)

	def polar(self):
		return (self.radius)

	def __str__(self):
		return '(' + str(self.x) + ', ' + str(self.y) + ')'

	def __cmp__(self):
		return (self.x > other.x) and (self.y > other.y)

class Segment:
	def __init__(self, start, end):
		self.start = start
		self.end = end
	def length(self):
		return math.sqrt( ( (self.start.x - self.end.x) * (self.start.x - self.end.x) ) 
						+ ( (self.start.y - self.end.y) * (self.start.y - self.end.y) ) )

# instances
# p = cPoint(1.0, 2.0)
# print dir(p)
# print p.x
# print p.radius
# print p.cartesian()
# print p.polar()
# print p.__str__()
# print p.__cmp__()

# p.x = 'foobar' # don't do this
# print p.x
# q = pPoint(3.0,4.0)
# print p > q

p1 = cPoint(3.0, 4.0)
p2 = cPoint(5.0, 7.0)
s1 = Segment(p1,p2)
print s1.length()