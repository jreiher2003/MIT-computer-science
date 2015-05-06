x = 16
ans = 0
while ans* ans < x:
	ans+=1
print ans

x = 996
i = 1
while i < x:
	if x % i == 0:
		print 'divisor ' ,i
	i += 1

x = 100
for i in range(1, x):
	if x % i == 0:
		print 'divisor ', i

print  [i for i in range(1,x) if x % i == 0]

# test = (1,2,3,4,5)
# print dir(test)
# print type(test)
# print len(test)
# print test[1:4]
# print test[-1:]
# print test[1:]
# print ""


x = 100
divisors = ()
for i in range(1,x):
	if x % i == 0:
		divisors = divisors + (i,)
print divisors

s1 = 'abcdefg'
s2 = 'hijklmn'

print s1+s2
print s1[0]
print s1[-1]

print s1.find('bcde')
print '\n'


sum_digits = 0
for c in str(1952):
	print c, str(1952)
	sum_digits += int(c)
print sum_digits