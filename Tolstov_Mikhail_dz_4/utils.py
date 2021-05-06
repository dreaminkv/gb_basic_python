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
