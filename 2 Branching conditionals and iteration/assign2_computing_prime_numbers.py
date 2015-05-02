# problem set 1
# name : Jeff Reiher
# Time: 20 min
n = 1000

pnums = []
for num in range(1,7910):
	if all(num % i != 0 for i in range(2, num)):
		pnums.append(num)
print len(pnums)
print pnums[-1:]

# 2 computes the sum of the logarithms of all the primes from 2 to some
# number n
from math import *

logsum = 0
# n = raw_input('This is a logarithm ratio tester. Which Number do you want oto test?')
n = 7
for x in range(2, n):
	for divisor in range(2, 1 + int(sqrt(x+1))):
		if x % divisor == 0:
			break
		else:
			logsum += log(x)

print n, logsum, n/logsum

