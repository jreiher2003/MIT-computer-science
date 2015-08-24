import random, pylab

fair = [1,2,3,4,5,6]

def throwPair(vals1, vals2):
	d1 = random.choice(vals1)
	d2 = random.choice(vals2)
	return d1, d2

print throwPair(fair, fair)