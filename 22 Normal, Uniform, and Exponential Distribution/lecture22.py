# from pylab import *
import random, pylab
# pylab.use('Agg')

fair = [1,2,3,4,5,6]

def throwPair(vals1, vals2):
	d1 = random.choice(vals1)
	d2 = random.choice(vals2)
	return d1, d2

# print throwPair(fair, fair)

def conductTrials(numThrows, die1, die2):
	throws = []
	for i in range(numThrows):
		d1, d2 = throwPair(die1, die2)
		throws.append(d1+d2)
	return throws

numThrows = 100000
throws = conductTrials(numThrows, fair, fair)
# print throws
# pylab.hist(throws)
# pylab.xticks(range(2,13), ['2','3','4','5','6','7','8','9','10','11','12','13'])
# pylab.title('Distribution of Values')
# pylab.xlabel('Sum of two dice')
# pylab.ylabel('Number of Throws')

# # get probabilities for fair dice
# pylab.figure()
# sums = pylab.array([0]* 14)
# for val in range(2, 13):
# 	sums[vals] = throws.count(val)
# probs = sums[2:13]/float(numThrows)
# xVals = pylab.arange(2,13)
# pylab.plot(xVals, probs, label='Fair Dice')
# pylab.xticks(range(2,13), ['2','3','4','5','6','7','8','9','10','11','12','13'])
# pylab.title('Probability of Values')
# pylab.xlabel('Sum of two dice')
# pylab.ylabel('Probability')

# pylab.show()

def craps(die1, die2):
	""" Return True if shooter wins at craps by betting pass line """
	d1, d2 = throwPair(die1,die2)
	tot = d1 + d2
	if tot in [7,11]: return True
	if tot in [2,3,12]: return False
	point = tot
	while True:
		d1, d2 = throwPair(fair, fair)
		tot = d1 + d2
		if tot == point: return True
		if tot == 7: return False

def simCraps(numBets, die1, die2):
	wins, losses = 0,0
	for i in range(numBets):
		if craps(die1, die2): wins += 1
		else: losses +=1
	print wins, losses
	houseWin = float(losses)/float(numBets)
	print houseWin
	print "House Winning percentage: " + str(100*houseWin) + '%'
	print "House profits per %d bets: $%d" % (numBets, losses-wins)


print simCraps(100000, fair, fair)
weighted1 = [1,1,2,3,4,5,6]
weighted2 = [2,1,2,3,4,5,6]
weighted3 = [3,1,2,3,4,5,6]
weighted4 = [4,1,2,3,4,5,6]
weighted5 = [5,1,2,3,4,5,6]
weighted6 = [6,1,2,3,4,5,6]
# throws = conductTrials(numThrows, fair, weighted)
# print throws
print 'weighted1'
print simCraps(100000, weighted1, weighted1)
print '<br>'
print 'weighted2'
print simCraps(100000, weighted2, weighted2)
print 'weighted3'
print simCraps(100000, weighted3, weighted3)
print 'weighted4'
print simCraps(100000, weighted4, weighted4)
print 'weighted5'
print simCraps(100000, weighted5, weighted5)
print 'weighted6'
print simCraps(100000, weighted6, weighted6)

print "all one fair one weighted"
print 'weighted1'
print simCraps(100000, weighted1, fair)
print 'weighted2'
print simCraps(100000, weighted2, fair)
print 'weighted3'
print simCraps(100000, weighted3, fair)
print 'weighted4'
print simCraps(100000, weighted4, fair)
print 'weighted5'
print simCraps(100000, weighted5, fair)
print 'weighted6'
print simCraps(100000, weighted6, fair)

