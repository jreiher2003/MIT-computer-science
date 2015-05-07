# code file for lecture 8,

def expl(a,b):
	ans = 1
	while b > 0:
		ans *= a
		b -= 1
	return ans, b, a

print expl(2,5)

def exp2(a,b):
	if b == 1:
		return a
	else:
		return a*exp2(a,b-1)

print exp2(2,100)

def exp3(a,b):
	if b == 1:
		return a
	elif (b % 2) * 2 == b:
		return exp3(a*a, b/2)
	else:
		return a * exp3(a, b-1)

print exp3(2,4)

def g(n,m):
	x = 0
	for i in range(n):
		for j in range(m):
			x += 1
	return x, i, j

print g(5,10)

def Towers(size, fromStack, toStack, spareStack):
	if size == 1:
		print 'Move direction ', fromStack, 'to ',toStack
	else:
		Towers(size-1, fromStack, spareStack, toStack)
		Towers(1, fromStack, toStack, spareStack)
		Towers(size-1, spareStack, toStack, fromStack)

# print Towers(8,'f','t','s')

def search(s, e):
	answer = None
	i = 0
	numCompares = 0
	while i < len(s) and answer == None:
		numCompares += 1
		if e == s[i]:
			answer = True
		elif e < s[i]:
			answer = False
		i += 1
	print answer, numCompares

search(1)