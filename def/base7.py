def sub_sub_generator():
    yield "sub sub yield"
    return "sub sub return"

def sub_generator():
    yield "sub yield"
    res = yield from sub_sub_generator()
    print("sub res = {}".format(res))
    return "sub return"

def generator():
    yield "genarator yield"
    res = yield from sub_generator()
    print("gen res = {}".format(res))
    return 'gen return'

gen = generator()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))