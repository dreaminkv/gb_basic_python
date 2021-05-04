from random import randint


def gen_random_char(word_lenght, sentence_length):
    for _ in range(sentence_length):
        word = []
        for i in range(word_lenght):
            word.append(chr(randint(92, 121)))
        yield ('').join(word)


gen_chars = gen_random_char(8, 5)
print(gen_chars)
for el in gen_chars:
    print(el)

print('#####################')