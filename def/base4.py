# def outer():
#     outer_value = 'outer value'
#     def inner():
#         outer_value = 'inner value'
#         print('inner: outer_value = {}, id = {}'.format(outer_value, id(outer_value)))
#     inner()
#     print('outer: outer_value = {}, id = {}'.format(outer_value, id(outer_value)))

# outer()


def outer():
    outer_value = 'outer value'
    def inner():
        nonlocal outer_value
        outer_value = 'inner value'
        print('inner: outer_value = {}, id = {}'.format(outer_value, id(outer_value)))
    inner()
    print('outer: outer_value = {}, id = {}'.format(outer_value, id(outer_value)))

outer()