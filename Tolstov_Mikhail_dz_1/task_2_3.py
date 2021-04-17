# 3 *(вместо задачи 2) Решить задачу 2 не создавая новый список
# (как говорят, in place). Эта задача намного серьёзнее, чем может сначала показаться.

some_list1 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for i in range(len(some_list1)):
    el = some_list1.pop(i - i)
    if el[-1].isdigit() and int(el) < 10:
        el = '"' + el[:-1] + '0' + el[-1] + '"'
        some_list1.append(el)
    else:
        some_list1.append(el)

print(' '.join(some_list1))
