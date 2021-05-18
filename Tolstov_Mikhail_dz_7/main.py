import os
import shutil
import datetime

ODD_PATH = 'data/odd_num'
EVEN_PATH = 'data/even_num'

txt_files = [file for file in os.listdir() if file.endswith('.txt')]
# print(txt_files)
#
# for file in txt_files:
#     nums = file.split("_")[1][:-4]
#     if int(nums) % 2 ==0:
#         os.replace(file, os.path.join(EVEN_PATH, file))
#     else:
#         os.replace(file, os.path.join(ODD_PATH, file))
# file_tuple = [el for el in os.walk('data')]
# files = [el[2] for el in file_tuple if el != []]
# txt_files = []
# for el in files:
#     txt_files.extend(el)
# for file in txt_files:
#     nums = file.split("_")[1][:-4]
#     if int(nums) % 2 ==0:
#         os.replace(file, os.path.join(EVEN_PATH, file))
#         # os.rename(os.path.join(EVEN_PATH, file), file)
#     else:
#         os.replace(file, os.path.join(ODD_PATH, file))
#         # os.rename(os.path.join(ODD_PATH, file), file)
# # shutil.move('copy_data', 'data')
#
# # print(os.stat('data'))

# print(oct(os.stat('data/even_num/text_44.txt').st_mode)[-3:])
# print(datetime.datetime.fromtimestamp(os.stat('data/even_num/text_44.txt').st_atime))
print(os.stat('data/even_num/text_92.txt').st_size)

shutil.copy2('main.py', 'data/copy_data/')
print(oct(os.stat('main.py').st_mode)[-3:])
print(oct(os.stat('data/copy_data/main.py').st_mode)[-3:])

print(datetime.datetime.fromtimestamp(os.stat('main.py').st_atime))
print(datetime.datetime.fromtimestamp(os.stat('main.py').st_mtime))

print(datetime.datetime.fromtimestamp(os.stat('data/copy_data/main.py').st_atime))
print(datetime.datetime.fromtimestamp(os.stat('data/copy_data/main.py').st_mtime))