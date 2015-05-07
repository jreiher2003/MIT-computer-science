# intro to lists

techs = ['MIT', 'Yale', 'Brown']
Ivys = ['Harvard', 'Yale', 'Brown']

university = []
university.append(Ivys)
print university
university.append(techs)
print university
# for u in university: 
# 	print u
# 	for i in u:
# 		print i

u = [u for u in university]
print u
print [i for i in u]
print [t for t in techs]

unis = techs + Ivys
print id(unis)
Ivys.remove('Harvard')
print unis
print id(Ivys)

lettercounts = {}
for l in 'Mississippi':
	lettercounts[l] = lettercounts.get(l, 0) + 1
print lettercounts

litems = lettercounts.items()
print litems
litems.sort()
print litems