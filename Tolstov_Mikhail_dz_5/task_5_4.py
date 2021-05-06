# 4. Представлен список чисел. Необходимо вывести те его элементы,
# значения которых больше предыдущего, например:
# src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# result = [12, 44, 4, 10, 78, 123]
#
#
# Подсказка: использовать возможности python, изученные на уроке.
# Подумайте, как можно сделать оптимизацию кода по памяти, по скорости.
import timeit
import sys
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]


max_src = [src[i] for i in range(1, len(src)) if src[i] > src[i-1]]
print(max_src)


def max_src(list_num):
    result = []
    for i in range(1, len(list_num)):
        if list_num[i] > list_num[i - 1]:
            result.append(list_num[i])
    yield result


print(*max_src(src))

print('Затрачено пямяти с помощью List Comprehensions: ', sys.getsizeof(max_src))
print('Затрачено пямяти с помощью генератора', sys.getsizeof(max_src(src)))



code_to_test_1 = """
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
max_src = [src[i] for i in range(1, len(src)) if src[i] > src[i-1]]
"""

elapsed_time_1 = timeit.timeit(code_to_test_1, number=100)/100
print('Время выполнения List Comprehensions: ', elapsed_time_1)

code_to_test = """
def max_src(src):
    result = []
    for i in range(1, len(src)):
        if src[i] > src[i - 1]:
            result.append(i)
    yield result
"""

elapsed_time_2 = timeit.timeit(code_to_test, number=100)/100
print('Время выполнения генератора: ', elapsed_time_2)
