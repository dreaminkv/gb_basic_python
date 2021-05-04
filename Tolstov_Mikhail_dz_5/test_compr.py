import sys

def num_digit(num):
    sum_of_digit = 0
    for char in str(num):
        sum_of_digit += int(char)
    return sum_of_digit


list_odd_num = [str(i * 5) + '!' for i in range(0, 50, 2) if sum(map(int, str(i * 5).strip())) % 2 == 0]
print(list_odd_num)


user_info = ['Basil', 'Ivanov', 27]

user_info_nums = [el for el in user_info if isinstance(el, int)]
print(user_info_nums)

