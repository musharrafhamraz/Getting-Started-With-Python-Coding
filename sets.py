myset = {'musharraf', 'hamraz', 'hahahaha'}
myset2 = {'musharraf', 'hamraz', 'nononnm', 23, 56, True}

print(myset)

for i in myset:
    print(i)


myset.add(12)
intersectionset = myset.intersection(myset2)

print(intersectionset)


myset.discard('hamraz')

print(myset)