class MyException(Exception):
    pass

def devide(a, b):
    if b == 0:
        raise MyException('cant divide with 0')
    else:
        return a / b

try:
    c = devide(10, 0)
except Exception as e:
    print(e, type(e))