# 4 *(вместо 3) Решить задачу 3 для ситуации, когда объём данных в файлах превышает объём ОЗУ
# (разумеется, не нужно реально создавать такие большие файлы, это просто задел на будущее проекта).
# Только теперь не нужно создавать словарь с данными. Вместо этого нужно сохранить объединенные
# данные в новый файл (users_hobby.txt). Хобби пишем через двоеточие и пробел после ФИО:
# Иванов,Иван,Иванович: скалолазание,охота
# Петров,Петр,Петрович: горные лыжи

with open('users.csv', 'r', encoding='utf-8') as f:
    users_list = [line.replace('\n', '') for line in f]

with open('hobby.csv', 'r', encoding='utf-8') as f:
    users_hobby_list = [line.replace('\n', '')for line in f]


def show_users_hobbies(users, users_hobby):
    """
    :param users: users list
    :param users_hobby: users hobby list
    :return: users hobby dict
    """
    users_hobby_dict = dict.fromkeys(users)
    for i in range(len(users_hobby)):
        users_hobby_dict.update({users[i]: users_hobby[i]})
    with open('users_hobby.txt', 'w', encoding='utf-8') as w:
        for key in users_hobby_dict:
            users_hobby_write = (key + ': ', str(users_hobby_dict[key]) + '\n')
            w.writelines(users_hobby_write)


show_users_hobbies(users_list, users_hobby_list)
