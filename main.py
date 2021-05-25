# def p_wrapper(func):
#     print(func)
#
#     def tag_wrapper(*args, **kwargs):
#         print('args', args)
#         print('kwargs', kwargs)
#         markup = func(*args, **kwargs)
#         print(markup)
#         return markup
#
#     return tag_wrapper
#
#
# @p_wrapper
# def render_input(field):
#     return f'<input id="id_{field}" type="text" name="{field}">'
#
#
# username_f = render_input('username')
# print(render_input)
def dec_math(func):
    def wrapper(*args, **kwargs):
        print('Hard math')
        func(*args, **kwargs)
        print('Hard math is over')
    return wrapper


@dec_math
def hard_math(num):
    print(100 ** num)


hard_math(6)