# 3. Есть два файла: в одном хранятся ФИО пользователей сайта,
# а в другом — данные об их хобби. Известно, что при хранении данных используется принцип:
# одна строка — один пользователь, разделитель между значениями — запятая. Написать код, загружающий
# данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения — данные о хобби. Сохранить словарь
# в файл. Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО
# задаём в словаре значение None. Если наоборот — выходим из скрипта с кодом «1». При решении задачи считать, что
# объём данных в файлах во много раз меньше объема ОЗУ.
# Фрагмент файла с данными о пользователях (users.csv):
# Иванов,Иван,Иванович
# Петров,Петр,Петрович
# Фрагмент файла с данными о хобби (hobby.csv):
# скалолазание,охота
# горные лыжи

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
    return users_hobby_dict


print(show_users_hobbies(users_list, users_hobby_list))
