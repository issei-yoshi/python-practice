fruit = ('applie', 'banana', 'lemon')

print(fruit)
print(type(fruit))
print(fruit[0])

fruit = fruit + ('grape',)
print(fruit)

list_fruit = ['apple', 'banana']
fruit = tuple(list_fruit)
print(fruit)

print(fruit.count('apple'))
print(fruit.index('banana'))

pos = (135, 35)
countries = {pos : 'Japan'}

print(countries.get((135, 35)))