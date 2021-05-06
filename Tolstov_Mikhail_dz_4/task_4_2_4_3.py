# 2. Написать функцию currency_rates(), принимающую в качестве аргумента код валюты
# (например, USD, EUR, GBP, ...) и возвращающую курс этой валюты по отношению к
# рублю. Использовать библиотеку requests. В качестве API можно использовать
# http://www.cbr.ru/scripts/XML_daily.asp. Рекомендация:
# выполнить предварительно запрос к API в обычном браузере, посмотреть содержимое ответа.
# Можно ли, используя только методы класса str, решить поставленную задачу?
# Функция должна возвращать результат числового типа, например float. Подумайте:
# есть ли смысл для работы с денежными величинами использовать вместо float
# тип Decimal? Сильно ли усложняется код функции при этом? Если в качестве
# аргумента передали код валюты, которого нет в ответе, вернуть None.
# Можно ли сделать работу функции не зависящей от того, в каком регистре был передан аргумент?
# В качестве примера выведите курсы доллара и евро.
# 3. Доработать функцию currency_rates(): теперь она должна возвращать кроме курса дату, которая
# передаётся в ответе сервера. Дата должна быть в виде объекта date. Подумайте, как извлечь
# дату из ответа, какой тип данных лучше использовать в ответе функции?
import requests
from decimal import *
from datetime import date


def currency_rates(valute_name):
    """
    Enter the name of the currency in the format 'USD'
    as an argument to find out the current exchange rate in rubles
    """
    valute_name = str(valute_name)
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response = requests.get(url)
    json = response.json()
    if valute_name in json['Valute']:
        result_of_exchange = Decimal(json['Valute'][valute_name]['Value'])
        result_of_exchange = result_of_exchange.quantize(Decimal("1.00"))
        date1 = json['Date']
        date1 = date1[0:10]
        year = int(date1[0:4])
        month = int(date1[5:7])
        day = int(date1[8:])
        print(result_of_exchange, date(year, month, day))


if __name__ == '__main__':
    currency_rates('USD')
    currency_rates('EUR')
