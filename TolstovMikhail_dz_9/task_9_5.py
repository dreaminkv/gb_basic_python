# 5. Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса
# метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для
# каждого экземпляра.
class Stationery:
    def __init__(self, title='Black Sea'):
        self.title = title

    def draw(self):
        return f'we paint a picture called: {self.title}'


class Pen(Stationery):
    def draw(self):
        return f'we draw a picture with a pen called: {self.title}'


class Pencil(Stationery):
    def draw(self):
        return f'we draw a picture with a pencil called: {self.title}'


class Handle(Stationery):
    def draw(self):
        return f'we draw a picture with a handle called: {self.title}'


a = Stationery('New moon')
b = Pen('Good day')
c = Pencil()
d = Handle()

print(a.draw())
print(b.draw())
print(c.draw())
print(d.draw())