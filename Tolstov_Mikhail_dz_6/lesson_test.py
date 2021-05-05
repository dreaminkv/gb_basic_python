# raw_data = open('poem.txt', 'r', encoding='utf-8')
# content = raw_data.read()
# print(content)
# raw_data.close()

# with open('poem.txt', 'r', encoding='utf-8') as f:
#     # content = []
# #     print(f.tell())
# #     for i in range(5):
# #         print(f.tell())
# #         f.seek(22)
#     content = f.readline()
# #
# print(content, type(content))
with open('poem.txt', 'r', encoding='utf-8') as f:
    content = f.readlines()
    content_new = list(map(lambda x: f'{x[:-1]}6{x[-1]}', content))
print(content_new)

# with open('new_poem_0_2.txt', 'w+', encoding='utf-8') as f:
#     f.writelines(content_new)
#     f.seek(0)
#     old_data = f.readlines()
#
# print(old_data)
with open('new_poem_3.txt', 'a+', encoding='utf-8') as f:
    f.writelines(content_new)
    #
    # with open('log.txt', 'r', encoding='utf-8') as f:
    #     log_list = []
    #     line = f.readline()
    #     while line:
    #         line_parts = line.split(' ')
    #         el_list = (line_parts[0], line_parts[5], line_parts[6])
    #         log_list.append(el_list)
    #         line = f.readline()
    #     print(log_list)