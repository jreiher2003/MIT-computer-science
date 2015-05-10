import pylab

def rsquared(measured, estimated):
	diffs = (estimated-measured)**2
	mMean = measured.sum()/float(len(measured))
	var = (mMean-measured)**2
	return 1-diffs.sum()/var.sum()
	
# get data from file
def getData(fname):
	f = open(fname, 'r')
	x = []
	y = []
	for line in f:
		if line[0] == '#': continue
		line = line[:-1]
		elems = line.rsplit(':')
		x.append(float(elems[0]))
		y.append(float(elems[1]))
	return pylab.array(x), pylab.array(y)

distances, forces = getData('txt.txt')
pylab.scatter(distances, forces)
pylab.xlabel('Dsitance (Meters)')
pylab.ylabel('Force (Newtons)')
a,b = pylab.polyfit(distances,forces),1)
yVals = a*distances+b
pylab.plot(distances,yVals,c='1', linewidth=2)
pylab.title('Force vs. Distance for spring')


a,b,c = pylab.polyfit(distances,forces,2)
yVals = a*(distances**2) + b* distances + c
pylab.plot(times, yVals, c = 'y', linewidth=4)
pylab.show()