class Human:

    def __init__(self, name, age, phone_number):
        self.name = name
        self.age = age
        self.phone_number = phone_number

    def __str__(self):
        return self.name + ',' + str(self.age) + ',' + self.phone_number

    def __eq__(self, other):
        return (self.name == other.name) and (self.phone_number == other.phone_number)

man = Human('Issei', 19, '00000000000')
man2 = Human('Issei', 21, '00000000000')
man_str = str(man)
print(man_str)

print(man == man2)