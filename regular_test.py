import re

random_name = ['words', 'василий', 'Кирил', 'Ва', 'Кири']
# pattern = re.compile(r'^[А-ЯЁ][а-яё]+$')
pattern = re.compile(r'Кир')
# for word in random_name:
#     print(pattern.search(word))

forum_message = 'Василий Иванов под ником p@nisher96 писал оскорбления' \
                'на почту sunny_girl@yandex.ru 21/08/2020 и hello_kitty2000@gmail.com 23.08.2020'

spps = re.compile(r'\w+@\w+\.\w+')
padd = re.compile(r'\w+@\w+')
data_find = re.compile(r'(?:\d{2}[./|]){2}\d{4}')
print(data_find.findall(forum_message))
# print(padd.split((forum_message)))
# print(spps.findall(forum_message))