# lecture 8 MIT
# s == list, e == to the element we are searching for, first of list, last of list, #calls need to find e
def binary_search(lst, e, first, last, calls):
	print first, last, calls
	if (last - first) < 2:
		return lst[first] == e or lst[last] == e
	mid = first + (last - first)/2
	if lst[mid] == e:
		return True
	if lst[mid] > e: 
		return binary_search(lst, e, first, mid -1, calls + 1)
	else:
		return binary_search(lst, e, mid + 1, last, calls + 1)

def search (lst, e):
	print binary_search(lst, e, 0, len(lst)-1, 1)

# lst = range(10000000)
# print search(lst, 50000)
s = [1,8,3,6,4]
def basic_sort(lst):
	for i in range(len(lst)-1):
		minIndx = i
		minVal = lst[i]
		j = i + 1
		while j < len(lst):
			if minVal > lst[j]:
				minIndx = j
				minVal = lst[j]
			j = j + 1
		temp = lst[i]
		lst[i] = lst[minIndx]
		lst[minIndx] = temp
	return lst

# print basic_sort(s)

# import random

# t = random.sample(range(0,1000),1000)
# print t
# print basic_sort(t)

def bubble_sort(lst):
	for j in range(len(lst)):
		for i in range(len(lst) -1):
			if lst[i] > lst[i+1]:
				temp = lst[i]
				lst[i] = lst[i+1]
				lst[i+1] = temp
		print lst

print bubble_sort(s)