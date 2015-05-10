import locale, os
if os.name in ['mac', 'posix']:
	locale.setlocale(locale.LC_ALL, 'en_US_UTF-8') #max version
else:
	locale.setlocale(locale.LC_ALL, ) # PC-Version


def formatInt(i):
	return locale.format('%d', i, grouping=True)

from pylab import *
import random, math


def throwDarts(numDarts, shouldPlot):
	inCircle = 0
	estimates = []
	for darts in xrange(1, numDarts + 1, 1):
		x = random.random()
		y = random.random()
		if math.sqrt(x*x + y*y) <= 1.0:
			inCircle += 1
		if shouldPlot:
			piGuess = 2*(inCircle/float(darts))
			estimates.append(piGuess)
		if darts%1000000 == 0: # so its making progress
			piGuess = 2*(inCircle/float(darts))
			dartsStr = locale.format('%d', darts, True)
			print 'Estimate with', formatInt(darts), 'darts ', piGuess
	if shouldPlot:
		xAxis = xrange(1, len(estimates)+1)
		semilogx(xAxis, estimates)
		titleString = 'Estimations of pi, final estimate: ' + str(piGuess)
		title(titleString)
		xlabel('Number of darts thrown')
		ylabel('Estimate of pi')
		show()
	return 2*(inCircle/float(numDarts))

def findPi(numDarts, shouldPlot=False):
	piGuess = throwDarts(numDarts, shouldPlot)
	print 'Estimated value of pi with',formatInt(numDarts), 'darts: ', piGuess


findPi(10000,True)