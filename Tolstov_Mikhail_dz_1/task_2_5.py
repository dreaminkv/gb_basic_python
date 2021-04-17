# Создать вручную список, содержащий цены на товары (10–20 товаров), например:
# [57.8, 46.51, 97, ...]
#
# Вывести на экран эти цены через запятую в одну строку, цена должна
# отображаться в виде <r> руб <kk> коп (например «5 руб 04 коп»). Подумать,
# как из цены получить рубли и копейки, как добавить нули, если, например,
# получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).
# Вывести цены, отсортированные по возрастанию, новый список не создавать
# (доказать, что объект списка после сортировки остался тот же).
# Создать новый список, содержащий те же цены, но отсортированные по убыванию.
# Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров
# по возрастанию, написав минимум кода?

import random

price_list = []
price_list_correct = []
for i in range(0, 10):
    i = random.random() * 100
    i = f'{i:.2f}'
    price_list.append(i)

for elem in range(len(price_list)):
        prices = price_list.pop(elem - elem)
        penny = prices[-2:] + ' коп'
        rubles = prices[0:-3] + ' руб '
        prices = rubles + penny
        price_list.append(prices)


print('id до сортировки: ', id(price_list))
print(', '.join(price_list))

price_list.sort()
print('id после сортировки: ', id(price_list))
print('Цены по возрастанию: ', (', '.join(price_list)))

price_list_up = sorted(price_list, reverse=True)
print('Цены по убыванию: ', (', '.join(price_list_up)))

top5_price = [top5 for top5 in price_list_up[:5]]
print('5 самых дорогих товаров: ', (', '.join(top5_price)))
