from pprint import pprint

def sqrt(x):
	"""returns a squre root of number"""
	ans = 0
	if x > 0:
		while ans*ans < x:
			ans = ans + 1
		if ans* ans != x:
			print x, 'is not a perfect square'
			return None
		else:
			return ans
	else:
		print x, 'is a negative number'
		return None

print sqrt(18)

# pprint(locals())
# pprint(globals())
test = sqrt(34)
print test == None


def solve(numLegs, numHeads):
	for numChicks in range(0, numHeads + 1):
		numPigs = numHeads - numChicks
		totLegs = 4 * numPigs + 2 * numChicks
		if totLegs == numLegs:
			return numPigs, numChicks
	return None, None

def barnYard():
	heads = 20
	legs = 56
	pigs, chickens = solve(legs,heads)
	if pigs == None:
		print "This is no solution"
	else:
		print "Number of pigs: ", pigs
		print "Number of chickens: ", chickens

print barnYard()

print ""
### Recursion

def is_palindrone(x):
	if len(x) <= 1:
		return True
	elif x[0] == x[-1] and is_palindrone(x[1:-1]):
		return True
	else:
		return False

print is_palindrone('abba')
print is_palindrone('jeff')

print ""
def fibo(n):
	if n == 0 or n ==1:
		return 1
	else:
		return fibo(n-1) + fibo(n-2)

print fibo(36)