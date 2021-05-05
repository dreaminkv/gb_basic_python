#1. Не используя библиотеки для парсинга, распарсить (получить определённые данные)
# файл логов web-сервера nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
# — получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:
# [
#     ...
#     ('141.138.90.60', 'GET', '/downloads/product_2'),
#     ('141.138.90.60', 'GET', '/downloads/product_2'),
#     ('173.255.199.22', 'GET', '/downloads/product_2'),
#     ...
# ]

with open('log.txt', 'r', encoding='utf-8') as f:
    log_list = []
    for line in f:
        line_clean = line.replace('"', '')
        line_parts = line_clean.split(' ')
        el_line_parts = (line_parts[0], line_parts[5], line_parts[6])
        log_list.append(el_line_parts)
    print(log_list)

