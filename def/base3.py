# def printAnimal():
#     animal = 'cat'
#     print('関数内animal={}, id={}'.format(animal, id(animal)))

# animal = 'dog'
# printAnimal()
# print('関数外animal={}, id={}'.format(animal, id(animal)))

def printAnimal():
    global animal
    animal = 'cat'
    print('関数内animal={}, id={}'.format(animal, id(animal)))

animal = 'dog'
printAnimal()
print('関数外animal={}, id={}'.format(animal, id(animal)))