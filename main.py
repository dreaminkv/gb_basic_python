<<<<<<< HEAD
<<<<<<< HEAD
class Auto:
    def __init__(self):
        print("Автомобиль заведен")
        self.auto_name = "Mazda"
        self._auto_year = 2019
        self.__auto_model = "CX9"

a = Auto()
print(a.auto_name)
print(a.__auto_model)
=======
# class Auto:
#     # атрибуты класса
#     auto_count = 0
#
#     # методы класса
#     def on_auto_start(self, auto_name, auto_model, auto_year):
#         print("Автомобиль заведен")
#         self.auto_name = auto_name
#         self.auto_model = auto_model
#         self.auto_year = auto_year
#         self.auto_count += 1
#
# a = Auto()
# a.on_auto_start('Mazda', 'Rx8', 2020)
# print(a.auto_name)
# print(a.auto_count)
#
# a3 = Auto()
# a3.on_auto_start('Mazda', 'Rx8', 2020)
# print(a3.auto_name)
# print(a3.auto_count)
#
# a = Auto()
# a.on_auto_start('Mazda', 'Rx8', 2020)
# print(a.auto_name)
# print(a.auto_count)
class Player:
    def player_method(self):
        print("Родительский метод класса Player")
=======
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

>>>>>>> lesson_8

@dec_math
def hard_math(num):
    print(100 ** num)

<<<<<<< HEAD
class Navigator:
    def navigator_method(self):
        print("Родительский метод класса Navigator")


class MobilePhone(Player, Navigator):
    def mobile_phone_method(self):
        print("Дочерний метод класса MobilePhone")


m_p = MobilePhone()
m_p.player_method()
m_p.navigator_method()
>>>>>>> lesson-9
=======

hard_math(6)
>>>>>>> lesson_8
