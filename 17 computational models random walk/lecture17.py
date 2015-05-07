# random walk problem
# drunk college kid in field
# how far does he walk?
import math, random, pylab
from pprint import pprint

class Location(object):
	def __init__(self, x, y):
		self.x = float(x)
		self.y = float(y)

	def move(self, xc, yc):
		return Location(self.x + float(xc), self.y + float(yc))

	def getCoords(self):
		return self.x, self.y

	def getDist(self, other):
		ox, oy = other.getCoords()
		xDist = self.x - ox
		yDist = self.y - oy
		return math.sqrt(xDist**2 + yDist**2)

# pprint(dir(pylab))

class CompassPt(object):
	possibles = ("N", "S", "E", "W")
	def __init__(self, pt):
		if pt in self.possibles: 
			self.pt = pt
		else:
			raise ValueError('in CompassPt.__init__')

	def move(self, dist): 
		""" dist = distance on cartesian plane """
		if self.pt == 'N': return (0, dist)
		elif self.pt == 'S': return (0, -dist)
		elif self.pt == 'E': return (dist, 0)
		elif self.pt == 'W': return (-dist, 0)
		else: raise ValueError('in CompassPt.move')

class Field(object):
	def __init__(self, drunk, loc):
		self.drunk = drunk
		self.loc = loc

	def move(self, cp, dist):
		oldLoc = self.loc
		xc, yc = cp.move(dist) # x change and y change
		self.loc = oldLoc.move(xc, yc)

	def getLoc(self):
		return self.loc

	def getDrunk(self):
		return self.drunk

class Drunk(object):
	def __init__(self, name):
		self.name = name

	def move(self, field, time = 1):
		if field.getDrunk() != self:
			raise ValueError('Drunk.move called with drunk no')
		for i in range(time):
			pt = CompassPt(random.choice(CompassPt.possibles))
			field.move(pt, 1)

def performTrial(time, f):
	start = f.getLoc()
	distances = [0.0]
	for t in range(1, time + 1):
		f.getDrunk().move(f)
		newLoc = f.getLoc()
		distance = newLoc.getDist(start)
		distances.append(distance)
	return distances

# assert False

drunk = Drunk('Homer Simpson')
for i in range(3):
	f = Field(drunk, Location(0,0))
	distances = performTrial(500, f)
	pylab.plot(distances)

pylab.title("Homer's random walk")
pylab.xlabel("Time")
pylab.ylabel("Distance from Origin")

pylab.show()
# assert False

def performSim(time, sumTrials):
	distLists = []
	for trial in range(sumTrials):
		d = Drunk('Drunk ' + str(trial))
		f = Field(d, Location(0,0))
		distances = performTrial(time, f)
		distLists.append(distances)
	return distLists

def ansQuest(maxTime, numTrials):
	means = []
	distLists = performSim(maxTime, sumTrials)
	for t in range(maxTime + 1):
		tot = 0.0
	for distL in distLists:
		tot += distL[t]
	means.append(tot/len(distL))
	pylab.figure()
	pylab.plot(means)
	pylab.ylabel('distance')
	pylab.xlabel('time')
	pylab.title('Average Distance vs. Time (' + str(len(distLists)))

ansQuest(500, 100)
pylab.show()