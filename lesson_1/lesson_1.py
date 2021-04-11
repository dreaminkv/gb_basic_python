# '''
# Первое занятие
# '''
# '''
# str_for_print = 'Hello'
# print(str_for_print, type(str_for_print))
# str_for_print = 10
# print(str_for_print, type(str_for_print))
# # комментарий
# '''
# '''
# str_for_print = int(input('Введите возраст: '))
# print(str_for_print, type(str_for_print))
# '''
# '''
# 1. Определить является ли цифрой input
# 2. Определить являются ли все символы цифрой
# '''
# str_for_print = input('Input symbol: ')
# if str_for_print.isdigit() == True:
#     print('Digit')
#     int_for_print = int(str_for_print)
#     if int_for_print < 5:
#         print('Less')
#     else:
#         print('More')
# else:
#     print('Char')
#
# # print(str_for_print, type(str_for_print))
# str_for_print = input('Input symbol: ')
# while not str_for_print.isdigit():
#     str_for_print = input('Input symbol: ')
# print("Tha's all")

list_of_digit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# print(len(list_of_digit))
# print(list_of_digit[1])
# for i in list_of_digit:
#     print('Hello', i)

for i in range(len(list_of_digit)):
    list_of_digit[i] *= 10
print(list_of_digit)
