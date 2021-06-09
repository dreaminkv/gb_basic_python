# """
# 5.Реализовать функцию get_jokes(), возвращающую n шуток, сформированных
# из трех случайных слов, взятых из трёх списков (по одному из каждого):
#
#
#         	Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
#
#
# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий
# повторы слов в шутках (когда каждое слово можно использовать только в одной шутке)?
# Сможете ли вы сделать аргументы именованными?
# Задачи со * предназначены для продвинутых учеников, которым мало сделать обычное задание
# # import random
# """
import random


def get_jokes(number_of_jokes=0, nuko=False):
    """first argument number of jokes. If you want to avoid repeating
    common words in jokes, set the second argument to true"""
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    ready_made_jokes = []
    for i in range(0, number_of_jokes):
        collect_jokes = random.choice(nouns), random.choice(adverbs), random.choice(adjectives)
        if nuko:
            nouns.remove(collect_jokes[0])
            adverbs.remove(collect_jokes[1])
            adjectives.remove(collect_jokes[2])
        ready_made_jokes.append((' '.join(collect_jokes)))
    return ready_made_jokes


print(get_jokes(10))
