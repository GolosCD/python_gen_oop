'''
Классы Lecture и Conference🌶️🌶️
1. Реализуйте класс Lecture, описывающий некоторое выступление. При создании экземпляра класс должен принимать три аргумента в следующем порядке:

topic — тема выступления
start_time — время начала выступления в виде строки в формате HH:MM
duration — длительность выступления в виде строки в формате HH:MM
2. Также реализуйте класс Conference, описывающий конференцию, протяженностью в один день. Конференция представляет собой набор последовательных выступлений. При создании экземпляра класс не должен принимать никаких аргументов.

Класс Conference должен иметь четыре метода экземпляра:

add() — метод, принимающий в качестве аргумента выступление и добавляющий его в конференцию. Если выступление пересекается по времени с другими выступлениями, должно быть возбуждено исключение ValueError с текстом:
Провести выступление в это время невозможно
total() — метод, возвращающий суммарную длительность всех выступлений в конференции в виде строки в формате HH:MM
longest_lecture() — метод, возвращающий длительность самого долгого выступления в конференции в виде строки в формате HH:MM
longest_break() — метод, возвращающий длительность самого долгого перерыва между выступлениями в конференции в виде строки в формате HH:MM
Примечание 1. Перерыв между выступлениями может быть нулевым. Другими словами, одно выступление может заканчиваться, например, в 12:00, а другое начинаться в 12:00.

Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованные классы используются только с корректными данными.

Примечание 3. Никаких ограничений касательно реализаций классов нет, они могут быть произвольными.
'''

class Lecture:
    def __init__(self, topic, start_time, duration):
        self.topic = topic
        self.start_time = self.convert_min(start_time)
        self.duration = self.convert_min(duration)
        self.end_time = self.start_time+self.duration
        
    @staticmethod    
    def convert_min(time):
        hours,minute = map(int,time.split(':'))
        return hours*60+minute
        
    def __str__(self):
        return f'{self.topic},({self.start_time//60:02}:{self.start_time%60:02}), ({self.end_time//60:02}:{self.end_time%60:02})'
            
class Conference:
    def __init__(self):
        self.conf = []
        
    def add(self,event :Lecture):
        if self.conf:
            for existing_lecture in self.conf:
                if event.start_time < existing_lecture.start_time + existing_lecture.duration and existing_lecture.start_time < event.start_time + event.duration:
                    raise ValueError ('Провести выступление в это время невозможно')
        self.conf.append(event)
        self.conf.sort(key = lambda x: x.start_time)
   
            
    def longest_lecture(self):
        max_lec = max(self.conf,key = lambda x: x.duration)
        return f'{max_lec.duration//60:02}:{max_lec.duration%60:02}'
        
    def longest_break(self):
        res = []
        for index,event in enumerate(self.conf[:-1]):
            next = self.conf[index +1]
            res+=[next.start_time-event.end_time]
        br = max(res)
        return f'{br//60:02}:{br%60:02}'
        
    def total(self):
        total = sum([event.duration for event in self.conf])
        return f'{total//60:02}:{total%60:02}'
        
    def __iter__(self):
        return iter(self.conf)

        

# INPUT DATA:

# TEST_1:
conference = Conference()

conference.add(Lecture('Простые числа', '08:00', '01:30'))
conference.add(Lecture('Жизнь после ChatGPT', '10:00', '02:00'))
conference.add(Lecture('Муравьиный алгоритм', '13:30', '01:50'))
print(conference.total())
print(conference.longest_lecture())
print(conference.longest_break())

# TEST_2:
conference = Conference()
conference.add(Lecture('Простые числа', '08:00', '01:30'))

try:
    conference.add(Lecture('Жизнь после ChatGPT', '09:00', '02:00'))
except ValueError as error:
    print(error)

# TEST_3:
conference = Conference()
conference.add(Lecture('Простые числа', '08:00', '01:00'))
conference.add(Lecture('Жизнь после ChatGPT', '11:00', '02:00'))

try:
    conference.add(Lecture('Муравьиный алгоритм', '10:00', '04:00'))
except ValueError as error:
    print(error)

# TEST_4:
conference = Conference()
conference.add(Lecture('Муравьиный алгоритм', '09:30', '02:00'))
conference.add(Lecture('Жизнь после ChatGPT', '11:45', '04:00'))
conference.add(Lecture('Простые числа', '08:00', '01:30'))

print(conference.longest_lecture())
print(conference.longest_break())

# TEST_5:
conference = Conference()
conference.add(Lecture('Введение в ООП', '09:30', '00:30'))
conference.add(Lecture('Атрибуты объектов и классов', '08:00', '01:30'))
conference.add(Lecture('Методы экземляра класса', '10:30', '02:00'))

print(conference.longest_lecture())
print(conference.longest_break())

# TEST_6:
conference = Conference()
conference.add(Lecture('Декоратор @property', '09:30', '00:30'))
conference.add(Lecture('Свойства', '09:00', '00:30'))
conference.add(Lecture('Модификаторы доступа и аксессоры', '08:30', '00:30'))

print(conference.longest_lecture())
print(conference.longest_break())

# TEST_7:
conference = Conference()
conference.add(Lecture('Декораторы @classmethod и @staticmethod', '09:30', '00:30'))

try:
    conference.add(Lecture('Декоратор @singledispatchmethod', '09:30', '00:30'))
except ValueError as e:
    print(e)

# TEST_8:
conference = Conference()
conference.add(Lecture('Декораторы @classmethod и @staticmethod', '09:30', '00:30'))

try:
    conference.add(Lecture('Декоратор @singledispatchmethod', '09:45', '00:30'))
except ValueError as e:
    print(e)

# TEST_9:
conference = Conference()
conference.add(Lecture('Декораторы @classmethod и @staticmethod', '09:30', '00:30'))

try:
    conference.add(Lecture('Декоратор @singledispatchmethod', '09:59', '00:30'))
except ValueError as e:
    print(e)

# TEST_10:
conference = Conference()
conference.add(Lecture('Декораторы @classmethod и @staticmethod', '09:30', '00:30'))

try:
    conference.add(Lecture('Декоратор @singledispatchmethod', '09:00', '00:35'))
except ValueError as e:
    print(e)

# TEST_11:
conference = Conference()
conference.add(Lecture('Декораторы @classmethod и @staticmethod', '09:30', '00:30'))
conference.add(Lecture('Декоратор @singledispatchmethod', '09:00', '00:30'))
conference.add(Lecture('Создание, инициализация и очищение объектов', '11:00', '00:30'))

start_times = ['09:30', '09:45', '09:59', '09:00', '09:00', '09:15', '09:29', '08:30', '11:00', '11:15', '11:25', '10:45']
durations = ['00:30', '00:30', '00:30', '00:35', '00:15', '00:15', '00:30', '00:35', '00:20', '00:10', '00:35', '00:16']

for start_time, duration in zip(start_times, durations):
    try:
        conference.add(Lecture('Строковое представление объектов', start_time, duration))
    except ValueError as e:
        print(e)

# TEST_12:
conference = Conference()
conference.add(Lecture('Декораторы @classmethod и @staticmethod', '09:30', '00:30'))
conference.add(Lecture('Декоратор @singledispatchmethod', '09:00', '00:30'))
conference.add(Lecture('Создание, инициализация и очищение объектов', '11:00', '00:30'))
conference.add(Lecture('Унарные операторы и функции', '10:45', '00:15'))
conference.add(Lecture('Арифметические операции', '10:00', '00:30'))
conference.add(Lecture('Вызываемые объекты', '08:00', '01:00'))

print(conference.total())
print(conference.longest_lecture())
print(conference.longest_break())

