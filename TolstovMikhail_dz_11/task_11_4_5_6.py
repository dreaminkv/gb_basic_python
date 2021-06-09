# 4, 5, 6 Начать работу над проектом «Склад оргтехники».
# Создать класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведённых типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
# Продолжить работу над предыдущим заданием. Разработать методы, которые
# отвечают за приём оргтехники на склад и передачу в определённое подразделение
# компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру (например, словарь).
# Продолжить работу над предыдущим заданием. Реализовать механизм валидации вводимых
# пользователем данных. Например, для указания количества принтеров, отправленных
# на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум
# возможностей, изученных на уроках по ООП.


class NoStrError(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return 'Ошибка, тип данных названия оборудования должен быть str'.format(self.text)


class NoIntError(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return 'Ошибка, тип данных года выпуска оборудования должен быть int'.format(self.text)


class Warehouse:
    equipment_warehouse = []

    @staticmethod
    def number_equipment_warehouse():
        return f'Количство техники на складе: {len(Warehouse.equipment_warehouse)} шт, ' \
               f'состав техники на складе: {Warehouse.equipment_warehouse}'

    @staticmethod
    def in_some_office(num_possition):
        Some_office.equipment_some_office.append(Warehouse.equipment_warehouse[num_possition])
        del Warehouse.equipment_warehouse[num_possition]
        print(f'Перенесли технику: {Warehouse.equipment_warehouse[num_possition]} в некоторое подразделение')


class Office_equipment(Warehouse):
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year


class Some_office(Warehouse):
    equipment_some_office = []

    @staticmethod
    def number_equipment_somoff():
        return f'Количство техники в некотором подразделении: {len(Some_office.equipment_some_office)} шт,' \
               f' состав техники в некотором подразделении: {Some_office.equipment_some_office}'

    @staticmethod
    def in_warehouse(num_possition):
        Warehouse.equipment_warehouse.append(Some_office.equipment_some_office[num_possition])
        del Some_office.equipment_some_office[num_possition]
        print(f'Перенесли технику: {Some_office.equipment_some_office[num_possition]} на склад')


class Printer(Office_equipment, Warehouse):
    def __init__(self, name, model, year, size_paper):
        super().__init__(name, model, year)
        self.size_paper = size_paper
        if not isinstance(name, str):
            raise NoStrError(name)
        elif not isinstance(year, int):
            raise NoIntError(year)

    def in_warehouse(self):
        Warehouse.equipment_warehouse.append({'name': self.name, 'model': self.model,
                                              'year': self.year, 'size_paper': self.size_paper})


class Scaner(Office_equipment):
    def __init__(self, name, model, year, scan_quality_dpi):
        super().__init__(name, model, year)
        self.scan_quality_dpi = scan_quality_dpi
        if not isinstance(name, str):
            raise NoStrError(name)
        elif not isinstance(year, int):
            raise NoIntError(year)

    def in_warehouse(self):
        Warehouse.equipment_warehouse.append({'name': self.name, 'model': self.model,
                                              'year': self.year, 'size_paper': self.scan_quality_dpi})


class Xerox(Office_equipment):
    def __init__(self, name, model, year, copies_minute):
        super().__init__(name, model, year)
        self.copies_minute = copies_minute
        if not isinstance(name, str):
            raise NoStrError(name)
        elif not isinstance(year, int):
            raise NoIntError(year)

    def in_warehouse(self):
        Warehouse.equipment_warehouse.append({'name': self.name, 'model': self.model,
                                              'year': self.year, 'copies_minute': self.copies_minute})


a = Printer('Printer HP', 'x456', 2008, 'a4')
f = Printer('Printer Kyocera', 'm323', 2010, 'a3')
l = Printer('Printer Brother', 'al12', 2020, 'a1')
y = Xerox(123, 'c3720l', '2021', '40 pcs')  # Здесь допущена ошибка типа данных в названии оборудования
# и года выпуска, можно исправить по очереди для проверки выполнения исключения
b = Warehouse()
y.in_warehouse() # Отправим копир с магазина на склад
a.in_warehouse()  # Отправим принтер с магазина на склад
f.in_warehouse()  # Отправим принтер с магазина на склад
l.in_warehouse()  # Отправим принтер с магазина на склад
print(b.number_equipment_warehouse())  # Остаток техники на складе
a.in_some_office(-1)  # Отправим принтер со склада в некоторое подразделение
a.in_some_office(-1)  # Отправим принтер со склада в некоторое подразделение
z = Some_office()
print(z.number_equipment_somoff())  # Остаток техники в некотором подразделении
print(b.number_equipment_warehouse())  # Остаток техники на складе
z.in_warehouse(-1) # Отправим принтер со склада в некоторое подразделение
print(b.number_equipment_warehouse())
