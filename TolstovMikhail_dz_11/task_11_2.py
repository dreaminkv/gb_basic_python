# 2 Создать собственный класс-исключение, обрабатывающий ситуацию деления на
# ноль. Проверить его работу на данных, вводимых пользователем. При вводе
# нуля в качестве делителя программа должна корректно обработать эту ситуацию
# и не завершиться с ошибкой.


class Zero_div_error(Exception):
    def __init__(self):
        pass

    @staticmethod
    def divide_by_null(divider, denominator):
        try:
            return divider / denominator
        except ZeroDivisionError:
            return f'Делить на 0 нельзя'


print(Zero_div_error.divide_by_null(10, 0))
