class Human:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age



    def get_name(self):
        print('getter nameを呼び出し')
        return self.__name

    def get_age(self):
        print('getter ageを呼び出し')
        return self.__age

    def set_name(self, name):
        print('setter nameを呼び出し')
        self.__name == name

    def set_age(self, age):
        print('setter ageを呼び出し')
        self.__age == age

    name = property(get_name, set_name)
    age = property(get_age, set_age)

    def print_msg(self):
        print(self.name, self.age)

human = Human('Taro', 12)
human.name = 'Issei'
human.age = 26

print(human.name)
print(human.age)

human.print_msg()