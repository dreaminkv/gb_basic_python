# 5. Представлен список чисел. Определить элементы списка, не
# имеющие повторений. Сформировать из этих элементов список
# с сохранением порядка их следования в исходном списке, например:
# src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [23, 1, 3, 10, 4, 11]
#
#
# Подсказка: напишите сначала решение «в лоб». Потом подумайте об оптимизации.
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

unique_list = set()
tmp = set()
for el in src:
   if el not in tmp:
       unique_list.add(el)
   else:
       unique_list.discard(el)
   tmp.add(el)

unique_list_ord = [el for el in src if el in unique_list]
print(unique_list_ord)
