'''
Классы USADate и ItalianDate
1. Реализуйте класс USADate, описывающий дату в американском формате. При создании экземпляра класс должен принимать три аргумента в следующем порядке:

year — год
month — месяц
day — день
Класс USADate должен иметь два метода экземпляра:

format() — метод, который возвращает строку, представляющую собой дату в формате MM-DD-YYYY
iso_format() — метод, который возвращает строку, представляющую собой дату в формате YYYY-MM-DD
2. Также реализуйте класс ItalianDate, описывающий дату в итальянском формате, конструктор которого принимает три аргумента:

year — год
month — месяц
day — день
Класс ItalianDate должен иметь два метода экземпляра:

format() — который возвращает строку, представляющую собой дату в формате DD/MM/YYYY
iso_format() — который возвращает строку, представляющую собой дату в формате YYYY-MM-DD
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованные классы используются только с корректными данными.

Примечание 2. Никаких ограничений касательно реализаций классов нет, они могут быть произвольными.
'''
from abc import ABC
import datetime


class BaseDate (ABC):
    DATE_FORMAT = None
    
    def __init__(self, year, month, day):
        self.date = datetime.date(year, month, day)
        
    def format(self):
        return self.date.strftime(self.DATE_FORMAT)

    def iso_format(self):
        return self.date.isoformat()
        
        
class USADate(BaseDate):
    DATE_FORMAT = "%m-%d-%Y"

    
class ItalianDate(BaseDate):
    DATE_FORMAT = "%d/%m/%Y"


italiandate = ItalianDate(2023, 4, 6)

print(italiandate.format())
print(italiandate.iso_format())