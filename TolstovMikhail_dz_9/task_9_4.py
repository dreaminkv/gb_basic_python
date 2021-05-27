# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed,
# color, name, is_police(булево). А также методы:
# go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar
# , WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который
# должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод
# show_speed. При значении скорости свыше 60 (TownCar)
# и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения
# атрибутов. Выполните доступ к атрибутам, выведите
# результат. Вызовите методы и покажите результат.
class Car:
    def __init__(self, speed, color, name, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'the {self.name} started'

    def stop(self):
        return f'the {self.name} stop'

    def turn(self, direction):
        self.direction = direction
        if direction == 'right':
            return f'the {self.name} turned to the right'
        elif direction == 'left':
            return f'the {self.name} turned to the left'

    def show_speed(self):
        return f'Current {self.name} speed: {self.speed} km / h'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'{self.name} have exceeded the speed limit 60 km / h'
        else:
            return f'Current {self.name} speed: {self.speed} km/ch'


class SportCar(Car):
    pass


class PoliceCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'{self.name} have exceeded the speed limit 40 km / h'
        else:
            return f'Current {self.name} speed: {self.speed} km/ch'


a = WorkCar(60, 'green', 'Lexus', False)
print(a.turn('left'))
print(a.show_speed())

b = SportCar(200, 'red', 'Ferrari', False)
print(b.turn('right'))
print(b.show_speed())
print(b.stop())

c = TownCar(50, 'blue', 'Toyota', False)
print(c.turn('right'))
print(c.go())
print(c.stop())
