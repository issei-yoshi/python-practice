for i in range(10):
    print(i)

    # for _ in range(100):
    #     print('A')

for i in range(2, 20, 3):
    print(i)

sample = ['John', 'Paul', 'George', 'Ringo']
for member in sample:
    print(member)

human = {
    'Name': 'Taro',
    'Age': 20,
    'gender': 'man'
}

for h in human:
    print(h, human.get(h))