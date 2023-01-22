class Human:
    class_name = 'Human'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_name_age(self):
        print('インスタンスメソッド実行')
        print('name = {}, age= {}'.format(self.name, self.age))

    @classmethod
    def print_class_name(cls, msg):
        print('クラスメソッド実行')
        print(cls.class_name)
        print(msg)

    @staticmethod
    def print_msg(msg):
        print('スタティックメソッド実行')
        print(msg)

# インスタンスメソッド
man = Human('Issei', 19)
man.print_name_age()
# print(man.name)
# print(man.age)

# クラスメソッド
Human.print_class_name('こんにちは')

# スタティックメソッド
man.print_msg('hello static')
Human.print_msg('hello_static')