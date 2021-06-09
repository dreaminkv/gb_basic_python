# 2. *(вместо 1) Решить задачу генерации нечётных чисел от 1 до n
# (включительно), не используя ключевое слово yield.
def odd_nums(num):
    nums = (i for i in range(0, num + 1) if i % 2 != 0)
    return nums


odd_to_15 = odd_nums(15)
print(next(odd_to_15))
print(next(odd_to_15))
