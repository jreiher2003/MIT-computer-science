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
print throws
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