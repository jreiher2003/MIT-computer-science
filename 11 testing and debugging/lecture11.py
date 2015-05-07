#
#
# not a good program
# just had to make a copy of the list before alisising it

def silly():
	res = []
	done = False
	while not done:
		elem = raw_input('Enter element. Return when done. ')
		if elem == '':
			done = True
		else:
			res.append(elem)
	print 'res should be [1, a, 2] ', res
	tmp = res[:]
	print 'tmp', tmp, 'res', res
	tmp.reverse()
	isPal = (res == tmp)
	if isPal:
		print 'is a palindrone'
	else:
		print 'is Not a palindrone'


silly()