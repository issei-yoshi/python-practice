class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        print('hello {}'.format(self.name))

    def say_age(self):
        print('{} years old'.format(self.age))


class Employee(Person):
    def __init__(self, name, age, number):
        super().__init__(name, age)
        self.number = number

    def say_number(self):
        print('my number is = {}'.format(self.number))

    def greeting(self):
        super().greeting()
        print('I am employee, phone_number is {}'.format(self.number))

man = Employee('Issei', 30, '11111111')
man.greeting()
man.say_age()
man.say_number()