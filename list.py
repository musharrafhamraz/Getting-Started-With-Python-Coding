l = [1,3,5,7]
print(type(l))


list = [1,3,5,7, 'Hamraz', True]

for i in list:
    print(i)

print(list[-3]) # Negative index
print(list[len(list)-3]) # Coverting negative index to Positive Index

print(list[2]) # Positive Index

# Checking if any element is present in the list or not
if 7 in list:
    print('yes')
else:
    print('no')

# Same thing applies for the string

if 'Ham' in "Hamraz":
    print('yes')
else:
    print('no')

# List Comprehension

lst = [i*i for i in range(4)]
print(lst)


lst = [i*i for i in range(4) if i%2==0]
print(lst)


# List Methods

l = [1, 2, 3, 5]

l.append(7)
print(l)

l.sort()
l.reverse()
l.index(1)
l.count()
 # so on