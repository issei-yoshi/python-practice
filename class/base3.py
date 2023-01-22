class SampleClass:
    def __init__(self, msg, name=None):
        print('called constructor')
        self.msg = msg
        self.name = name

    def __del__(self):
        print('destructor is called')
        print('name = {}'.format(self.name))

    def print_msg(self):
        print(self.msg)

    def print_name(self):
        print(self.name)

var_1 = SampleClass('hello', 'Issei')
var_1.print_msg()
var_1.print_name()
del var_1