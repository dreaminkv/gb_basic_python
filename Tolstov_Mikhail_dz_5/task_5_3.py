# Есть два списка:
# tutors = [
#     'Иван', 'Анастасия', 'Петр', 'Сергей',
#     'Дмитрий', 'Борис', 'Елена'
# ]
# klasses = [
#     '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
# ]
#
#
# Необходимо реализовать генератор, возвращающий кортежи вида
# (<tutor>, <klass>), например:
# ('Иван', '9А')
# ('Анастасия', '7В')
# ...
#
# Количество генерируемых кортежей не должно быть больше длины списка tutors.
# Если в списке klasses меньше элементов, чем в списке tutors, необходимо
# вывести последние кортежи в виде: (<tutor>, None), например:
# ('Станислав', None)
#
# Доказать, что вы создали именно генератор. Проверить его работу вплоть до
# истощения. Подумать, в каких ситуациях генератор даст эффект.
from itertools import zip_longest

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей',
          'Дмитрий', 'Борис', 'Елена', 'Павл', 'Михаил']
klasses = ['9А', '7В', '9Б', '9В', '8Б',
           '10А', '10Б', '9А']

gen_tutors_classes = ((tutors, klasses) for tutors, klasses in zip_longest(tutors, klasses))
print(gen_tutors_classes)
print(*gen_tutors_classes)
print(*gen_tutors_classes)

# доказательство, что я создал генератор <generator object <genexpr> at 0x0000025707A03970>
# и второй принт не выводится, так как генератор исчерпал себя

# второй вариант создания генератора
# def tutors_klasses(tutors, klasses):
#     for el in zip_longest(tutors, klasses):
#         yield el
#
#
# print(tutors_klasses(tutors, klasses))
# доказательство, что я создал генератор <generator object tutor_klass at 0x0000024C472655F0>

# gen_tutors_klasses = tutors_klasses(tutors, klasses)
# добавим генератор в переменную, что бы было проще проверить в python console
