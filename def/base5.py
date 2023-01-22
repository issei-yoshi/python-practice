def generator(max):
    print('create generator')
    for n in range(max):
        yield n
        print('yield実行')

gen = generator(10)

for x in gen:
    print('x = {}'.format(x))
