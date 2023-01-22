class Human:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age


    @property
    def name(self): #getter
        print('getter nameが呼ばれた')
        return self.__name

    @property
    def age(self):
        print('getter ageが呼ばれた')
        return self.__age

    @name.setter
    def name(self, name):
        print('setter nameが呼ばれた')
        self.__name = name

    @age.setter
    def age(self, age):
        print('setter ageが呼ばれた')
        if age < 0:
            print('0以上の値を設定してね')
            return
        self.__age = age

human = Human('Issei', 13)
human.name = 'IsseiYoshi'
print(human.name)

human.age = 33
print(human.age)