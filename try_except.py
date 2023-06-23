a=20
b = 10

try:
    if a>b:
        print(a)
    else:
        raise Exception('sorry b is greater than a')
except NameError:
    print('No variable found!!!')
finally:
    print('I will always execute whatever happens.')