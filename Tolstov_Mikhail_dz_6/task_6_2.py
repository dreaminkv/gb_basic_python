# 2. *(вместо 1) Найти IP адрес спамера и количество отправленных
# им запросов по данным файла логов из предыдущего задания.
# Примечание: спамер — это клиент, отправивший больше всех запросов;
# код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
import time
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    log_list = []
    for line in f:
        line_clean = line.replace('"', '')
        line_parts = line_clean.split(' ')
        el_line_parts = (line_parts[0])
        log_list.append(el_line_parts)


def who_spammer(log_ip):
    """
    :param log_ip: list of ip addresses from the log file
    :return: ip addresses of the spammer and the number of hits
    """
    uniq_ip_list = set(log_ip)
    uniq_ip_count = [log_ip.count(el) for el in uniq_ip_list]
    uniq_ip_count_list = list(zip(uniq_ip_list, uniq_ip_count))
    spammer = (sorted(uniq_ip_count_list, key=lambda x: x[1], reverse=True))[0]
    return spammer


start = time.perf_counter()
print(who_spammer(log_list))
end = time.perf_counter()
print(f'Write time: {end - start}')