"""
МФЦ:
* ЗАПОЛНИТЬ форму в зависимости от запроса
* Свидетельство о рождении
* смена рабочего места

* Создание данной формы
* редактированик
* подтягивание информации из других форм
"""


class BaseForm:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __str__(self):
        result = [f'{key} : {value}' for key, value in self.__dict__.items()]
        return ', '.join(result)


class BirthForm(BaseForm):
    attr_set = frozenset(['name', 'surname', 'mothers_name',
                          'fathers_name', 'age', 'birth_date'])

    def check_for_correctness(self):
        if BirthForm.attr_set.issubset(set(self.__dict__.keys())):
            return True
        else:
            return False


class WorkExchange(BaseForm):
    attr_set = frozenset(['birth_form', 'workplaces', 'new_workplaces'])

    def check_for_correctness(self):
        if WorkExchange.attr_set.issubset(set(self.__dict__.keys())):
            return True
        else:
            return False

    def __get_info_from_birthdate(self):
        pass

    def send_info_to_pfr(self, link):
        self.__get_info_from_birthdate()
        print(f'Data of {str(self)} where send to PFR {link}')


user_0 = WorkExchange(name='Basil', surname='Ivanov', mothers_name='Natalie',
                   fathers_name='Leo', age=27, birth_date=1994)

print(user_0.check_for_correctness())
print(user_0.send_info_to_pfr('pfr'))
