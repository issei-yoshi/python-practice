class ClassA:
    def __init__(self, a):
        self.a = a

    def __bool__(self):
        if self.a == 'a':
            return True
        return False

var = ClassA('b')


# bool_var =  True
print('bool: {}'.format(bool(var)))

if var:
    print('if is true')