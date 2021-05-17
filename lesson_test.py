# import os
# folder = r'C:\Users\tolstov.my\AppData\Local\Programs\Python\Python39\Lib\site-packages\aiohttp'
#
# py_files = [os.path.join(folder, item)
#             for item in os.listdir(folder)
#             if item.lower().endswith('.py')]
# print(py_files)
# import os
#
# folder = r'C:\Users\tolstov.my\AppData\Local\Programs\Python\Python39\Lib\site-packages\django'
# # django_dirs = [item for item in os.listdir(folder)
# #                if os.path.isdir(os.path.join(folder, item))]
# # print(django_dirs)
#
# # import os
# # from time import perf_counter
# #
# # folder = 'some_data'
# # start = perf_counter()
# # size_threshold = 15 * 2 ** 10
# # small_files = [item
# #                  for item in os.listdir(folder)
# #                  if os.stat(os.path.join(folder, item)).st_size < size_threshold]
# # print(len(small_files), perf_counter() - start)
# #
# # start = perf_counter()
# # small_files_2 = [item.name
# #                  for item in os.scandir(folder)
# #                  if item.stat().st_size < size_threshold]
# # print(len(small_files_2), perf_counter() - start)
# # print(small_files == small_files_2)
# import os
# from time import perf_counter
#
# folder = 'some_data'
# start = perf_counter()
# all_files = [item
#               for item in os.listdir(folder)]
# print(len(all_files), perf_counter() - start)
# # 1000 0.056053622000000025
# start = perf_counter()
# all_files_2 = [item.name
#                 for item in os.scandir(folder)]
# print(len(all_files_2), perf_counter() - start)
# print(all_files == all_files_2)
# # 1000 0.04480954299999995
# # True

import os

import django

root_dir = django.__path__[0]
for root, dirs, files in os.walk(root_dir):
   print(root, len(dirs), len(files
import os

folder = r'C:\Users\inkve\Desktop\Tolstov_Mikhail_dz_6'
py_files = [item
            for item in os.listdir(folder)
            if item.lower().endswith('.py')]
print(py_files)
