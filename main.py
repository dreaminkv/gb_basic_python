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


class Navigator:
    def navigator_method(self):
        print("Родительский метод класса Navigator")


class MobilePhone(Player, Navigator):
    def mobile_phone_method(self):
        print("Дочерний метод класса MobilePhone")


m_p = MobilePhone()
m_p.player_method()
m_p.navigator_method()