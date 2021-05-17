# 1 Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
# |--my_project
#    |--settings
#    |--mainapp
#    |--adminapp
#    |--authapp
#
#
# Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске
# (как быть?); как лучше хранить конфигурацию этого стартера, чтобы в будущем
# можно было менять имена папок под конкретный проект; можно ли будет при этом
# расширять конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?
import os


def star_my_project(project_name, *args):
    """
    :param add project_name:
    :param args: add folder names inside the project
    :return: adds project folders
    """
    for folder in args:
        dir_path = os.path.join(project_name, folder)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)


star_my_project('my_project', 'settings', 'mainapp', 'adminapp', 'authapp')
