import sys

list_a = [i for i in range(100000)]
def num(max):
    i = 0
    while i < max:
        yield i
        i += 1


gen = num(100000)

print(sys.getsizeof(list_a))
print(sys.getsizeof(gen))