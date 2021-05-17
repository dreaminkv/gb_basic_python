# for i in range(100):
#     with open(f'text_{i}.txt', 'w', encoding='utf-8') as f:
#         f.(str(i**10))
import os
# print(os.listdir())
# os.makedirs('data', exist_ok=True)
# # os.mkdir('data/odd_num')
# # os.mkdir('data/even_num')
# # print(sorted(os.listdir('data')))
# import os
# import shutil
#
# ODD_PATH = 'data/odd_num'
# EVEN_PATH = 'data/even_num'
# # txt_files = [[file for file in file_tuple if file.endswith('.txt')]
# #              for file_tuple in os.walk('data')]
# file_tuple = [el for el in os.walk('data')]
# files = [el[2] for el in file_tuple if file_tuple if el != []]
# txt_files = []
# for el in files:
#     txt_files.extend(el)
# # print(txt_files)
# for file in txt_files:
#     nums = file.split("_")[1][:-4]
#     if int(nums) % 2 == 0:
#         # os.replace(file, os.path.join(EVEN_PATH, file))
#         os.rename(os.path.join(EVEN_PATH, file), file)
#     else:
#         os.rename(os.path.join(ODD_PATH, file), file)
#
# shutil.move('copy_data', 'data')