# 3. Создать структуру файлов и папок, как написано в задании 2
# (при помощи скрипта или «руками» в проводнике). Написать скрипт,
# который собирает все шаблоны в одну папку templates,
# Примечание: исходные файлы необходимо оставить; обратите внимание,
# что html-файлы расположены в родительских папках (они играют роль пространств имён)
# предусмотреть возможные исключительные ситуации; это реальная задача, которая решена,
# например, во фреймворке django.
from shutil import copytree


def copy_in_templates():
    file_src_1 = 'my_project/authapp/templates'
    file_src_2 = 'my_project/mainapp/templates'
    try:
        copytree(file_src_1, 'my_project/templates')
        copytree(file_src_2, 'my_project/templates', dirs_exist_ok=True)
    except FileExistsError:
        print('Папка templates уже создана и копирование в нее шаблонов завершено')


copy_in_templates()
