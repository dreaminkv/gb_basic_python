# Реализовать проект «Операции с комплексными числами». Создать класс «Комплексное число».
# Реализовать перегрузку методов сложения и умножения комплексных чисел. Проверить работу проекта.
# Для этого создать экземпляры класса (комплексные числа), выполнить сложение и умножение созданных
# экземпляров. Проверить корректность полученного результата.


class Complex_nums:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return self.num + other.num

    def __mul__(self, other):
        return self.num * other.num


b = Complex_nums(22)
print(b)
c = Complex_nums(22)
print(b + c)
print(b * c)
