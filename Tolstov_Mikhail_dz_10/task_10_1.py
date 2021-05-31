# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
# (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.


class Matrix:

    def __init__(self, *args: list):
        self.param = [*args]

    def __str__(self):
        return f'Матрица: {self.param}'

    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise ArithmeticError('Правый операнд должен быть типом MAtrix')
        elif len(self.param) != len(other.param):
            raise  ArithmeticError('Длина складываемых матриц не совпадает')
        for i in range(len(self.param)):
            yield [x+y for x,y in zip(self.param[i], other.param[i])]


if __name__ == '__main__':
    y = Matrix([-31, 22], [37, 43], [51, 86], [87, 54])
    x = Matrix([11, 23], [54, 76], [13, -67], [23, 53])

    print(y)
    b = x + y
    print(*b)
