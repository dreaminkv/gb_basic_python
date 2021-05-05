file_1 = open('hello.txt', 'r', encoding='utf-8')
# content = file_1.read()
# print(content)
# file_1.close()

# clean_content = content.replace('\n', ' ').replace('\r', ' ')
# print(clean_content)
# paragraphs = file_1.readlines()
# print(dir(file_1))
# file_1.close()

# print(file_1.readline())
# print(file_1.readline())
# file_1.close()

#
# # for line in file_1:
# #     print(line)
# # file_1.close()
# # txt = '''Пробуем записать в файл текст.
# # Используем метод .write().'''
#
# txt = """sssss
# sssss
# """
# with open('tset_text.txt', 'a', encoding='utf-8') as f:
#     f.write(txt)
#
# with open(' hello_2.txt', 'r', encoding='utf-8') as f:
#     # print(f.tell())
#     # line = f.readline()
#     # while line:
#     #     print(line.strip(), f.tell(), sep='\n')
#     #     line = f.readline()
#     f.seek(39)
#     print(f.readline().strip())
#     f.seek(142)
#     print(f.readline().strip())
#
#
import json
import random

nums = [random.randint(0, 100) for _ in range(10)]

with open('nums_again.json', 'w', encoding='utf-8') as f:
   json.dump(nums, f)

with open('nums_again.json', 'r', encoding='utf-8') as f:
   nums = json.load(f)