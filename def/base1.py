def print_hello():
    print('hello world')

print_hello()


def num_max(a: int, b: int):
    print("a: {}, b: {}".format(a, b))
    if a > b:
        return a
    else:
        return b

print(num_max(a=100, b=3))
print(num_max('20', 'a'))