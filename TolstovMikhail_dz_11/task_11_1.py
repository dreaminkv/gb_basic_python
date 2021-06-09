# 1. Реализовать класс «Дата», функция-конструктор которого должна
# принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый — с декоратором @classmethod.
# Он должен извлекать число, месяц, год и преобразовывать их тип
# к типу «Число». Второй — с декоратором @staticmethod, должен проводить
# валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.


class Data:
    result = []
    day = 0
    month = 0
    year = 0

    def __init__(self, data):
        self.data = data
        [Data.result.append(el) for el in data.split('-')]

    @classmethod
    def split_data(cls):
        cls.day = int(cls.result[0])
        cls.month = int(cls.result[1])
        cls.year = int(cls.result[2])
        return f'day: {type(cls.day)} month: {type(cls.month)}' \
               f' year: {type(cls.year)}'

    @staticmethod
    def valid_data():
        if Data.day <= 31 and Data.month <= 12 and Data.year <= 2021:
            return f'Data is valid: {Data.day}-{Data.month}-{Data.year}'
        else:
            return f'No valid data'


Data('31-12-2010')
print(Data.split_data())
print(Data.valid_data())
