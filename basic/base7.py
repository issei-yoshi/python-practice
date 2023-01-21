fruit = 'apple'
print(fruit)
print(type(fruit))

print(fruit * 10)
fruit_10 = fruit * 10
print(fruit_10)

new_fruit = fruit + ' banana'
print(new_fruit)

fruits = """apple
banana
grape
"""

print(fruits)

fruit = 'banana'
print(fruit[2])


byte_fruit = fruit.encode('utf-8')
print(byte_fruit)
print(type(byte_fruit))

str_fruit = byte_fruit.decode('utf-8')
print(str_fruit)
print(type(str_fruit))


msg = 'ABCDEABC'
print(msg.count('ABC'))

print(msg.startswith('ABDE'))
print(msg.endswith('C'))


msg = ' ABC '
print(msg)
print(msg.strip())

msg = 'ABCDEFABC'
print(msg.strip('CBA'))
print(msg.lstrip('CBA'))
print(msg.rstrip('CBA'))


msg = 'abcABC'
msg_u = msg.upper()
msg_l = msg.lower()
msg_s = msg.swapcase()
print(msg_u, msg_l, msg_s)


msg = 'ABCDEABC'
msg_r = msg.replace('ABC', 'FFF', 1)
print(msg_r)

msg = 'hello world'
print(msg.capitalize())


msg = 'hello, my name is Issei'
print(msg[1:10:3])
print('hello {}'.format('Taro'))
name = 'Jiro'
print(f'hello {name}')


msg = 'apple'
print(msg.islower())
print(msg.isupper())


msg = 'ABCDEABC'
print(msg.find('ABC'))
print(msg.rfind('ABC'))

print(msg.index('ABC'))
print(msg.rindex('ABC'))

print(msg.rfind('ABCE'))
# print(msg.index('ABCE')) #Error occurred