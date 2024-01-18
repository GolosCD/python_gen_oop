'''
Класс BirthInfo 🌶️
Реализуйте класс BirthInfo, описывающий данные о дате рождения. При создании экземпляра класс должен принимать один аргумент:

birth_date — дата рождения, представленная в одном из следующих вариантов:
экземпляр класса date
строка с датой в ISO формате
список или кортеж из трех целых чисел: года, месяца и дня
Если дата рождения является некорректной или представлена в каком-либо другом формате, должно быть возбуждено исключение TypeError с текстом:

Аргумент переданного типа не поддерживается
Экземпляр класса BirthInfo должен иметь один атрибут:

birth_date — дата рождения в виде экземпляра класса date
Класс BirthInfo должен иметь одно свойство:

age — свойство, доступное только для чтения, возвращающее текущий возраст в годах, то есть количество полных лет, прошедших с даты рождения на сегодняшний день
Примечание 1. Возраст в годах должен вычисляться так же, как и обычный возраст человека, то есть в день рождения его возраст увеличивается на один год.

Приведенный ниже код:

birthinfo = BirthInfo(date(2023, 2, 26))

print(birthinfo.age)
в 2024-02-25 должен выводить:

0
в 2024-02-26 должен выводить:

1
в 2025-02-25 должен выводить:

1
 в 2025-02-26 должен выводить:

2
Примечание 2. Для проверки того, что свойство age возвращает верный возраст, мы используем собственную функцию current_age(), которая вычисляет возраст в годах на основе даты рождения и текущей даты.

Примечание 3. Никаких ограничений касательно реализации класса BirthInfo нет, она может быть произвольной.
'''

from functools import singledispatchmethod
from datetime import date,timedelta,datetime
import re

def current_age(birthday, today):
    age = today.year - birthday.year - 1
    age += (today.month, today.day) >= (birthday.month, birthday.day)
    return age


class BirthInfo:
    @singledispatchmethod
    def __init__(self,d):
        raise TypeError ('Аргумент переданного типа не поддерживается')
      
    @__init__.register(date)
    def _from_init(self,d):
        self.birth_date = d

        
    @__init__.register(str)
    def _from_init(self,d):
        try:
            txt = re.fullmatch(r'\b\d{4}-\d{2}-\d{2}\b',d)
            b = map(int,txt.group().split('-'))
            self.birth_date = date(*b)
        except:
            raise TypeError ('Аргумент переданного типа не поддерживается')
            
    @__init__.register(list)    
    @__init__.register(tuple)
    def _from_init(self,d):
        self.birth_date = date(*d)
        
    @property
    def birth_date(self):
        return self._birth_date
    
    @birth_date.setter
    def birth_date(self,day):
        self._birth_date = day
        
    @property
    def age(self):
        today = date.today()
        age = today.year - self._birth_date.year-1 
        age += (today.month, today.day) >= (birthday.month, birthday.day)
        return  age

        
'''  
# INPUT DATA:

# TEST_1:
birthinfo1 = BirthInfo('2020-09-18')
birthinfo2 = BirthInfo(date(2010, 10, 10))
birthinfo3 = BirthInfo([2016, 1, 1])

print(birthinfo1.birth_date)
print(birthinfo2.birth_date)
print(birthinfo3.birth_date)

# TEST_2:
birthday = date(2020, 9, 18)
today = date.today()
birthinfo = BirthInfo(birthday)
true_age = current_age(birthday, today)

print(birthinfo.age == true_age)

# TEST_3:
birthinfo1 = BirthInfo('2020-09-18')
birthinfo2 = BirthInfo(date(2010, 10, 10))
birthinfo3 = BirthInfo([2016, 1, 1])

print(type(birthinfo1.birth_date))
print(type(birthinfo2.birth_date))
print(type(birthinfo3.birth_date))

# TEST_4:
birthday = date(2023, 3, 6)
today = date.today()
birthinfo = BirthInfo(birthday)
true_age = current_age(birthday, today)

print(birthinfo.age == true_age)

# TEST_5:
errors = [20200918, True, {1: 'one'}, {1, 2, 3}, 100.9]

for obj in errors:
    try:
        BirthInfo(obj)
    except TypeError as e:
        print(e)
'''
# TEST_6:
today = date.today()
for day in range(10):
    birthday = (today + timedelta(days=day)).replace(year=2000)
    birthinfo = BirthInfo(birthday)
    true_age = current_age(birthday, today)
    print('true_age: ', true_age, 'birthinfo.age :',birthinfo.age,'birthday :',birthday)
    print(birthinfo.age == true_age)

# TEST_7:
birth_dates = ['20200918', '2020-0918', '202009-18', ' 2020-09-18 ', '2020-9-18']

for birth_date in birth_dates:
    try:
        birthinfo1 = BirthInfo(birth_date)
    except TypeError as e:
        print(e)