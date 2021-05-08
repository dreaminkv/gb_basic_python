from sys import argv


def add_sale(float_num):
    with open('bakery.csv', 'a', encoding='utf-8') as f:
        f.writelines(float_num + '\n')


add_sale(argv[1])
