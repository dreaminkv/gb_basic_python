from sys import argv


def show_sales(from_num=None, to_num=None):
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        read_data = [line for line in f]
        if not from_num and not to_num:
            print(*(i for i in read_data))
        elif from_num and not to_num:
            print(*read_data[int(from_num) - 1:])
        else:
            print(*read_data[int(from_num) - 1: int(to_num)])


if len(argv) == 1:
    show_sales()
if len(argv) == 2:
    show_sales(argv[1])
elif len(argv) == 3:
    show_sales(argv[1], argv[2])
