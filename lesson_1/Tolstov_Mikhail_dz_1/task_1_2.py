# 2. Создать список, состоящий из кубов нечётных чисел от 0 до 1000:
# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело
# на 7. Например, число «19 ^ 3 = 6859» будем включать в сумму,
# так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7. Внимание:
# использовать только арифметические операции!
# К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из
# этого списка, сумма цифр которых делится нацело на 7. Внимание:
# новый список не создавать!!!

numbers = []

for i in range(1001):
    if i % 2 != 0:
        i = i ** 3
        numbers.append(i)
print('Список из кубов нечётных чисел от 0 до 1000: ', numbers)

sum_divisible_seven = 0
sum_number = 0

for number in numbers:
    while number > 0:
        sum_number = sum_number + (number % 10)
        number = number // 10
    if sum_number % 7 == 0:
        sum_divisible_seven += sum_number
        sum_number = 0
    else:
        sum_number = 0

print('Cумма тех чисел из этого списка, сумма цифр которых делится нацело на 7: ', sum_divisible_seven)

for i in range(len(numbers)):
    numbers[i] += 17

print('К каждому элементу нашего списка добавим 17 ', numbers)

sum_divisible_seven = 0
sum_number = 0

for number in numbers:
    while number > 0:
        sum_number = sum_number + (number % 10)
        number = number // 10
    if sum_number % 7 == 0:
        sum_divisible_seven += sum_number
        sum_number = 0
    else:
        sum_number = 0

print('Cумма тех чисел из этого списка, сумма цифр которых делится нацело на 7: ', sum_divisible_seven)