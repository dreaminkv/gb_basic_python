# 4 Написать скрипт, который выводит статистику для заданной
# папки в виде словаря, в котором ключи — верхняя граница размера файла
# (пусть будет кратна 10), а значения — общее количество файлов
# (в том числе и в подпапках), размер которых не превышает этой границы,
# но больше предыдущей (начинаем с 0), например:
#     {
#       100: 15,
#       1000: 3,
#       10000: 7,
#       100000: 2
#     }
# Тут 15 файлов размером не более 100 байт; 3 файла больше 100
# и не больше 1000 байт...
# Подсказка: размер файла можно получить из атрибута .st_size
# объекта os.stat.
import os
from os.path import join


def file_size_statistics(folder='.'):
    """
    :param folder: enter the path to the folder
    :return: dictionary with statistics
    """
    dict_stat = {100: 0, 1000: 0, 10000: 0, 100000: 0}
    for root, dirs, files in os.walk(folder):
        total_size = [os.stat(join(root, name)).st_size for name in files]
        for el in total_size:
            if el <= 1000:
                dict_stat[100] += 1
            elif 1000 < el <= 10000:
                dict_stat[1000] += 1
            elif 10000 < el <= 100000:
                dict_stat[10000] += 1
            elif el > 100000:
                dict_stat[100000] += 1
    return dict_stat


print(file_size_statistics())
