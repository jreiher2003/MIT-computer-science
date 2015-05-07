from pprint import pprint
from lecture15 import cPoint
import math
# print cPoint
class cartesianPoint:
	pass

cp1 = cartesianPoint()  # instance of class
cp2 = cartesianPoint()  # instance of class
cp1.x = 1.0				# attributes
cp1.y = 2.0				# attributes
cp2.x = 1.0				# attributes
cp2.y = 3.0				# attributes
# new instance
p1 = cartesianPoint()
p1.x = 3
p1.y = 4
p2 = cartesianPoint()
p2.x = 3
p2.y = 4

# print p1 is p2
# print samePoint(p1,p2)

class polarPoint:
	pass

pp1 = polarPoint()
pp2 = polarPoint()
pp1.radius = 1.0
pp1.angle = 0
pp2.radius = 2.0
pp2.angle = math.pi / 4.0

def samePoint(p1, p2):
	return (p1.x == p2.x) and (p1.y == p2.y)

def printPoint(p):
	print '(' + str(p.x) + ',' + str(p.y) + ')'

