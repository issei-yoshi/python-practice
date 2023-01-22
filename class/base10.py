class  Human:

    __class_val = 'Human'

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def print_msg(self):
        print('name = {}, age = {}'.format(self.__name, self.__age))


human = Human('Issei', 11)
# print()
human.print_msg()