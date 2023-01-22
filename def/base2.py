def sample(arg1, arg2=100):
    print(arg1, arg2)

sample(200)


def spam(arg1, *arg2):
    print("arg1={}, arg2={}".format(arg1, arg2))
    print(type(arg2))

spam(1,2,3,4,5)


def spam_2(arg1, **arg2):
    print('arg1={}, arg2={}'.format(arg1, arg2))
    print(type(arg2))

spam_2(3, name='Taro', age=20)


def spam_3(arg1, *arg2, **arg3):
    print('arg1={}, arg2={}, arg3={}'.format(arg1, arg2, arg3))

spam_3(1,2,3,4,5,name='Issei', age=26)


def sample_2():
    return 1, 2
a, b = sample_2()
print(a, b)