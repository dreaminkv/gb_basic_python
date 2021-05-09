# 5 **(вместо 4) Решить задачу 4 и реализовать интерфейс командной строки, чтобы
# можно было задать имя обоих исходных файлов и имя выходного файла. Проверить работу скрипта.
from sys import argv


def show_users_hobbies(users_file, hobbys_file, users_hobbys_write_file):
    """
    :param users_file: add users file name
    :param hobbys_file: add hobbys file name
    :param users_hobbys_write_file: add users_hobbys write file name
    :return:
    """
    with open(users_file, 'r', encoding='utf-8') as f:
        users_list = [line.replace('\n', '') for line in f]

    with open(hobbys_file, 'r', encoding='utf-8') as f:
        users_hobby_list = [line.replace('\n', '') for line in f]

    users_hobby_dict = dict.fromkeys(users_list)

    for i in range(len(users_hobby_list)):
        users_hobby_dict.update({users_list[i]: users_hobby_list[i]})

    with open(users_hobbys_write_file, 'w', encoding='utf-8') as w:
        for key in users_hobby_dict:
            users_hobby_write = (key + ': ', str(users_hobby_dict[key]) + '\n')
            w.writelines(users_hobby_write)


show_users_hobbies(argv[1], argv[2], argv[3])
