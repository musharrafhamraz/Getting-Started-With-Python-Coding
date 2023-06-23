def average(a, b):
    print('average is ', (a+b)/2)
average(1,2)



def average1(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    print('Average is: ', sum/len(numbers))
average1(1,2,3,4,5)