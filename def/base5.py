def generator(max):
    print('create generator')
    for n in range(max):
        try:
          x = yield n
          print('x = {}'.format(x))
          print('yield実行')
        except ValueError as e:
           print('throw実行')

gen = generator(10)
next(gen)
gen.send(100)
# gen.throw(ValueError('Invalid Value'))
gen.close()
# next(gen)

# for x in gen:
#     print('x = {}'.format(x))
