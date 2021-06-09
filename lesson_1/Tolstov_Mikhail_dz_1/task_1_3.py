# 3. Реализовать склонение слова «процент» для чисел до 20. Например, задаем число 5 — получаем «5 процентов»,
# задаем число 2 — получаем «2 процента». Вывести все склонения для проверки.

percent_value = ['процент', 'процента', 'процентов']
percent_key = int(input('Введите количество процентов от 1 - 20: '))

if percent_key == 1:
    print(percent_key, percent_value[0])
elif percent_key == 2 or percent_key == 3 or percent_key == 4:
    print(percent_key, percent_value[1])
else:
    print(percent_key, percent_value[2])