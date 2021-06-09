# """
# 2. *(вместо задачи 1) Доработать предыдущую функцию в num_translate_adv():
# реализовать корректную работу с числительными, начинающимися с
# заглавной буквы — результат тоже должен быть с заглавной. Например:
# >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"
# """


def num_translate(number):
    numbers = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре',
               'five': 'пять', 'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять',
               'ten': 'десять', 'Zero': 'Ноль', 'One': 'Один', 'Two': 'Два', 'Three': 'Три',
               'Four': 'Четыре', 'Five': 'Пять', 'Six': 'Шесть', 'Seven': 'Семь', 'Eight': 'Восемь',
               'Nine': 'Девять', 'Ten': 'Десять'}
    if number in numbers:
        return numbers[number]



print(num_translate('Ten'))
