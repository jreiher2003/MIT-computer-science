def merge(left,right):
	"""Assumes left and right are sorted lists.
	returns a new sorted list containing the same elements
	as (left + right) would contain"""
	result = []
	i, j = 0, 0
	while i < len(left) and j < len(right):
		if left[i] <= right[j]:
			result.append(left[i])
			i += 1
		else:
			result.append(right[j])
			j += 1
	while i < len(left):
		result.append(left[i])
		i += 1
	while j < len(right):
		result.append(right[j])
		j += 1
	return result



def mergesort(lst):
	"""Returns a new sort list containing the same
	elements as lst"""
	print lst
	if len(lst) < 2:
		return lst[:]
	else:
		middle = len(lst) /2
		left = mergesort(lst[:middle])
		right = mergesort(lst[middle:])
		together = merge(left, right)
		print 'merged ', together
		return together

import random
x = random.sample(range(100), 25)
# mergesort(x)

def create(smallest, largest):
	intSet = []
	for i in range(smallest, largest+1):
		intSet.append(None)
	return intSet

def insert(intSet,e):
	intSet[e] = 1

def member(intSet, e):
	return intSet[e] == 1

def hashChar(c):
	""" c is a char 
	function returns a different integer in the range of 0-255
	for each possible value of c """
	return ord(c)

def cSetCreate():
	cSet = []
	for i in range(0, 255):
		cSet.append(None)
	return cSet

def cSetInsert(cSet, e):
	cSet[hashChar(e)] = 1

def cSetMember(cSet, e):
	return cSet[hashChar(e)] == 1


###########################################
# exceptions

def readFloat(requestMsg, errorMsg):
	while True:
		val = raw_input(requestMsg)
		try:
			val = float(val)
			return val
		except:
			print errorMsg

#print readFloat('Enter a float: ', 'Not a float.')

def readVal(valType, requestMsg, errorMsg):
	while True:
		val = raw_input(requestMsg)
		try:
			val = valType(val)
			return val
		except:
			print errorMsg
#print readVal(int, 'Enter int: ', 'Not an int...')


def getGrades(fname):
	try:
		gradesFile = open(fname, 'r')
	except IOError:
		print 'could not open', fname
		raise 'GetGradesError'
	grades = []
	for line in gradesFile:
		grades.append(float(line))
	return grades