for i in range(1, 100):
    if i % 15 == 0:
        print('{}: Fizz Buzz'.format(i))
    elif i % 3 == 0:
        print('{}: Fizz'.format(i))
    elif i % 5 == 0:
        print('{}: Buzz'.format(i))
    else:
        print(i)