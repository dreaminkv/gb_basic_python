# 3. Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий
# элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника
# (get_full_name) и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса
# Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.
class Worker:
    name = 'Mikhail'
    surname = 'Bestworkerov'
    position = 'System administrator'
    _income = {"wage": 50000, "bonus": 100000}


class Position(Worker):
    def get_full_name(self):
        return Worker.name, Worker.surname, Worker.position

    def get_total_income(self):
        result = 0
        for val in Worker._income.values():
            result += val
        return result


a = Position()

print(a.get_full_name())
print(a.get_total_income())
