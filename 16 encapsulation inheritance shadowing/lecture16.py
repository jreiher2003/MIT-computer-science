class Person(object):
	def __init__(self, family_name, first_name):
		self.family_name = family_name
		self.first_name = first_name

	def familyName(self):
		return self.family_name

	def firstName(self):
		return self.first_name

	def __cmp__(self, other):
		""" compare function """
		return cmp((self.family_name, self.first_name),
					other.family_name, other.first_name)

	def __str__(self):
		return "<Person: %s %s>" % (self.first_name, self.family_name)

	def say(self, toWhom, something):
		return self.first_name + ' ' + self.family_name +\
			 ' says to ' + toWhom.first_name + ' ' +\
			  toWhom.family_name + ' ' + something

	def sing(self, toWhom, something):
		return self.say(toWhom, somthing + 'la la la ')

# instance of Person
per = Person('Reiher', 'Jeff')
print per.familyName()
print per.say(per, 'Why are you not in class')

class MITPerson(Person):
	nextIdNum = 0
	def __init__(self, familyName, firstName):
		Person.__init__(self,familyName, firstName)
		self.idNum = MITPerson.nextIdNum
		MITPerson.nextIdNum += 1

	def getIdNum(self):
		return self.idNum

	def __str__(self, other):
		return 'MIT Person: %s %s' % (self.first_name, self.familyName)

	def __cmp__(self, other):
		return cmp(self.idNum, other.idNum)

p1 = MITPerson( 'Smith', 'Fred')
p2 = MITPerson('Foobar', 'Jan')

print p1.getIdNum()
print p2.getIdNum()
print p2.say(p1, 'What up son')

class UG(MITPerson):
	def __init__(self, familyName, firstName):
		MITPerson.__init__(self, familyName, firstName)
		self.year = None

	def setYear(self, year):
		if year > 5: return OverflowError('Too many years')
		self.year = year

	def getYear(self):
		return self.year

	def say(self, toWhom, something):
		return MITPerson.say(self, toWhom, 'Excuse me, but ' + something)

me = Person('Reiher', 'Jeffrey')
ug = UG('Doe', 'Jane')

print ug.say(me, 'go fuck yourself')
print ug.getIdNum()

# print ug > per
# print per > ug

class Professor(MITPerson):
	def __init__(self, familyName, firstName, rank):
		MITPerson.__init__(self, familyName, firstName)
		self.rank = rank
		self.teaching = {}

	def addTeaching(self, term, subj):
		try:
			self.teaching[term].append(subj)
		except KeyError:
			self.teaching[term] = [subj]

	def getTeaching(self, term):
		try:
			return self.teaching[term]
		except KeyError:
			return None

	def lecture(self, toWhom, something):
		return MITPerson.say(toWhom, something + ' as it is obvious')

	def say(self, toWhom, something):
		if type(toWhom) == UG:
			return MITPerson.say(self, toWhom, 'I do not understand why you say ' + something)
		elif type(toWhom) == Professor:
			return MITPerson.say(self, toWhom, 'I really liked your paper on ' + something)


class Faculty(object):
	def __init__(self):
		self.names = []
		self.IDs = []
		self.members = []
		self.place = None

	def add(self, who):
		if type(who) != Professor: raise TypeError('not a Professor')
		if who.getIdNum() in self.IDs: raise ValueError('duplicate')
		self.names.append(who.familyName())
		self.IDs.append(who.getIdNum())
		self.members.append(who)

	def __iter__(self):
		self.place = 0
		return self	

	def next(self):
		if self.place >= len(self.names):
			raise StopIteration
		self.place += 1
		return self.members[self.place-1]