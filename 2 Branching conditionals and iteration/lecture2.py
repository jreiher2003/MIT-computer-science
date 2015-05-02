print 'a' < 3
print 4 < '3'
print ord('3')
print ord(str(4))
sample code for use Lecture 2

x = 3 # create variable x and assign value 3 to it
x = x * x # bind x to value 9
n = raw_input('Enter a Number: ')
print n
print int(n)/int(n)
for x in range(100):
	if (x%2==0):
		print 'even'
	else:
		print 'odd'

x = 16
if (x/2) * 2 == x:
	print 'Even'
else:
	print 'Odd'

x = 111
y = 51
z = 11
print x,y,z
if x > z and y > z:
	print z, "z is the smallest"
elif x > y and z > y:
	print y, "y is the smallest"
else:
	print x, "x is the smallest"	

# squares x
y = 0 
x = -4
itersLeft = x
while itersLeft > 0:
	y = y + x
	itersLeft = itersLeft - 1
print y