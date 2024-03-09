'''
Классы Weekday и NextDate
1. Реализуйте класс Weekday, описывающий перечисление с днями недели. Перечисление должно иметь семь элементов:

MONDAY — элемент со значением 0
TUESDAY — элемент со значением 1
WEDNESDAY — элемент со значением 2
THURSDAY — элемент со значением 3
FRIDAY — элемент со значением 4
SATURDAY — элемент со значением 5
SUNDAY — элемент со значением 6
2. Также реализуйте класс NextDate, позволяющий определять дату следующего дня недели, начиная с текущего дня. При создании экземпляра класс должен принимать три аргумента в следующем порядке:

today — дата текущего дня, представленная экземпляром класса date
weekday — день недели, представленный элементом перечисления Weekday
after_today — булево значение, по умолчанию равняется False
Параметр after_today должен определять, учитывается ли текущая дата при определении даты следующего дня недели. Если он имеет значение False, текущая дата не должна учитываться, если True — должна учитываться.

Класс NextDate должен иметь два метода экземпляра:

date() — метод, возвращающий дату следующего дня недели в виде экземпляра класса date
days_until() — метод, возвращающий количество дней до даты следующего дня недели
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованные классы используются только с корректными данными.

Примечание 2. Никаких ограничений касательно реализаций классов нет, они могут быть произвольными.
'''

from enum import Enum,IntEnum
from datetime import date, timedelta

Weekday = IntEnum('Weekday',['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY'],start = 0)


class NextDate:
    def __init__(self,today :date, weekday :Weekday, after_today =False):
        self.today = today
        self.weekday = weekday.value
        self.after_today = after_today
        self.day_until = (self.weekday-self.today.weekday())%7
    
    def date(self):
        if self.today.weekday() ==self.weekday and self.after_today:
            return self.today
        else:
            self.day_until = self.day_until if self.day_until!=0 else 7
        return self.today+timedelta(days = self.day_until)
        
    def days_until(self):            
        return self.day_until

# INPUT DATA:

# TEST_1:
from datetime import date

today = date(2023, 4, 17)                              # понедельник
next_friday = NextDate(today, Weekday.FRIDAY)          # следующая пятница

print(next_friday.date())
print(next_friday.days_until())

# TEST_2:
from datetime import date

today = date(2023, 4, 17)                              # понедельник
next_monday = NextDate(today, Weekday.MONDAY)          # следующий понедельник без учета текущего

print(next_monday.date())
print(next_monday.days_until())

# TEST_3:
from datetime import date

today = date(2023, 4, 17)                              # понедельник
next_monday = NextDate(today, Weekday.MONDAY, True)    # следующий понедельник с учетом текущего

print(next_monday.date())
# print (next_monday.day_until)
print(next_monday.days_until())

# TEST_4:
from datetime import date

for weekday in Weekday:
    today = date(2023, 4, 27)                              # четверг
    next_date = NextDate(today, weekday)

    print(next_date.date())
    print(next_date.days_until())

# TEST_5:
from datetime import date

for weekday in Weekday:
    today = date(2023, 4, 27)                              # четверг
    next_date = NextDate(today, weekday, True)

    print(next_date.date())
    print(next_date.days_until())

# TEST_6:
from datetime import date, timedelta

today = date(2023, 4, 23)

for _ in range(7):
    today += timedelta(days=1)
    for weekday in Weekday:
        next_date = NextDate(today, weekday)
        print(f'Today = {today} {Weekday(today.weekday()).name}, next {weekday.name} = {next_date.date()}')
        print(f'Days until = {next_date.days_until()}')

# TEST_7:
from datetime import date, timedelta

today = date(2023, 4, 23)

for _ in range(7):
    today += timedelta(days=1)
    for weekday in Weekday:
        next_date = NextDate(today, weekday, True)
        print(f'Today = {today} {Weekday(today.weekday()).name}, next {weekday.name} = {next_date.date()}')
        print(f'Days until = {next_date.days_until()}')