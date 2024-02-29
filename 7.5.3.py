'''
Классы Validator, Number и String
1. Реализуйте абстрактный класс Validator, описывающий дескриптор, который проверяет, что устанавливаемое или изменяемое значение является корректным. При создании экземпляра класс не должен принимать никаких аргументов.

Дескриптор должен закрепляться за атрибутом, имеющим то же имя, что и переменная, которой присваивается дескриптор.

При обращении к атрибуту дескриптор должен возвращать значение этого атрибута, если оно установлено. Если значение атрибута не установлено, должно быть возбуждено исключение AttributeError с текстом:

Атрибут не найден
При установке или изменении значения атрибута дескриптор должен сперва проверять его на корректность с помощью метода validate().

Класс Validator должен иметь один абстрактный метод экземпляра:

validate() — пустой метод
2. Также реализуйте класс Number, наследника класса Validator, описывающий дескриптор, который проверяет, что устанавливаемое или изменяемое значение является числом из определенного диапазона. Дескриптор должен закрепляться за атрибутом, имеющим то же имя, что и переменная, которой присваивается дескриптор. При создании экземпляра класс должен принимать два аргумента в следующем порядке:

minvalue — левая граница диапазона, по умолчанию имеет значение None и не ограничивает число слева
maxvalue — правая граница диапазона, по умолчанию имеет значение None и не ограничивает число справа
Класс Number должен иметь один метод экземпляра:

validate() — метод, принимающий в качестве аргумента произвольный объект и возбуждающий исключение, если он не удовлетворяет каким-либо условиям. Если указанный объект не принадлежит типу int или float, должно быть возбуждено исключение TypeError с текстом:
Устанавливаемое значение должно быть числом
Если указанный объект является числом меньше minvalue, должно быть возбуждено исключение ValueError с текстом:
Устанавливаемое число должно быть больше или равно <minvalue>
Если указанный объект является числом больше maxvalue, должно быть возбуждено исключение ValueError с текстом:
Устанавливаемое число должно быть меньше или равно <maxvalue>
3. Наконец, реализуйте класс String, наследника класса Validator, описывающий дескриптор, который проверяет, что устанавливаемое или изменяемое значение является строкой определенной длины. Дескриптор должен закрепляться за атрибутом, имеющим то же имя, что и переменная, которой присваивается дескриптор. При создании экземпляра класс должен принимать три аргумента в следующем порядке:

minsize — минимальная длина слова, по умолчанию имеет значение None и не ограничивает минимальную длину
maxsize — максимальная длина слова, по умолчанию имеет значение None и не ограничивает максимальную длину
predicate — функция-предикат для дополнительной валидации, по умолчанию имеет значение None и не используется
Класс String должен иметь один метод экземпляра:

validate() — метод, принимающий в качестве аргумента произвольный объект и возбуждающий исключение, если он не удовлетворяет каким-либо условиям. Если указанный объект не принадлежит типу str, метод должен возбуждать исключение TypeError с сообщением:
Устанавливаемое значение должно быть строкой
Если указанный объект является строкой с длиной меньше minsize, должно быть возбуждено исключение ValueError с текстом:
Длина устанавливаемой строки должна быть больше или равна <minsize>
Если указанный объект является строкой с длиной больше maxsize, должно быть возбуждено исключение ValueError с текстом:
Длина устанавливаемой строки должна быть меньше или равна <maxsize>
Если указанный объект при передаче в функцию predicate() возвращает False, должно быть возбуждено исключение ValueError с текстом:
Устанавливаемая строка не удовлетворяет дополнительным условиям
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованные классы используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации классов нет, она может быть произвольной.
'''



from abc import ABC, abstractmethod

class Validator(ABC):
    def __set_name__(self, cls, attr):
        self._attr = attr 

    def __get__(self, obj, cls):
        if obj is None:
            return self
        if self._attr in obj.__dict__:
            return obj.__dict__[self._attr]
        else:
            raise AttributeError('Атрибут не найден')

    def __set__(self, obj, value):
        if self.validator(value):
            obj.__dict__[self._attr] = value
        else:
            raise ValueError('Некорректное значение')
            
    @abstractmethod
    def validator(value): pass


class Number (Validator):
    
    def __init__(self, minvalue=None, maxvalue=None):
        self.minvalue  = minvalue 
        self.maxvalue  = maxvalue 
        
    def validator(self,value):
        if not isinstance(value,(int,float)):
            raise TypeError ('Устанавливаемое значение должно быть числом')
        if not self.minvalue is None:    
            if value<self.minvalue:
                raise ValueError (f'Устанавливаемое число должно быть больше или равно {self.minvalue}')
        if self.maxvalue:        
            if value>self.maxvalue:
                raise ValueError (f'Устанавливаемое число должно быть меньше или равно {self.maxvalue}')
        return True
        
        
class String(Validator):
    
    def __init__(self,minsize=None,maxsize=None,predicate = None):
        self.minsize  = minsize 
        self.maxsize  = maxsize 
        self.predicate  = predicate 
        
        
    def validator(self,value):
        if not isinstance(value,str):
            raise TypeError ('Устанавливаемое значение должно быть строкой')
        if self.minsize:    
            if len(value)<self.minsize:
                raise ValueError (f'Длина устанавливаемой строки должна быть больше или равна {self.minsize}')
        if self.maxsize:        
            if len(value)>self.maxsize:
                raise ValueError (f'Длина устанавливаемой строки должна быть меньше или равна {self.maxsize}')
        if not self.predicate is None:    
            if not self.predicate(value):
                raise ValueError ('Устанавливаемая строка не удовлетворяет дополнительным условиям')
        return True        
            
            
# INPUT DATA:

# TEST_1:
class Student:
    age = Number(18, 99)


student = Student()
student.age = 19
print(student.age)

# TEST_2:
class Student:
    age = Number(18, 99)

try:
    student = Student()
    student.age = '19'
except TypeError as error:
    print(error)

# TEST_3:
class Student:
    age = Number(18, 99)

try:
    student = Student()
    student.age = 16
except ValueError as error:
    print(error)

# TEST_4:
class Student:
    age = Number(18, 99)

try:
    student = Student()
    student.age = 101
except ValueError as error:
    print(error)

# TEST_5:
class Student:
    age = Number(18)


student = Student()
student.age = 101
print(student.age)

try:
    student.age = 15
except ValueError as error:
    print(error)

# TEST_6:
class Student:
    age = Number(maxvalue=100)


student = Student()
student.age = 11
print(student.age)

try:
    student.age = 101
except ValueError as error:
    print(error)

# TEST_7:
class Student:
    age = Number(18, 99)


student = Student()
student.age = 18
print(student.age)

student.age = 99
print(student.age)

# TEST_8:
class Student:
    age = Number()


student = Student()
student.age = -1000
print(student.age)

student.age = 99999
print(student.age)

# TEST_9:
class Person:
    name = String(6, 10)


person = Person()
person.name = 'Андрей'
print(person.name)

person.name = 'Абдурахман'
print(person.name)

# TEST_10:
class Person:
    name = String(6, 10)


person = Person()

try:
    person.name = 'Ян'
except ValueError as e:
    print(e)


try:
    person.name = 'Аполлинария'
except ValueError as e:
    print(e)

try:
    person.name = 1
except TypeError as e:
    print(e)

# TEST_11:
class Person:
    name = String(6, 10, predicate=lambda x: x.startswith('А'))


person = Person()

try:
    person.name = 'Василий'
except ValueError as e:
    print(e)

# TEST_12:
class Person:
    name = String(6)


person = Person()
person.name = 'Пабло Диего Хосе Франциско де Паула Хуан Непомукено Криспин Криспиано де ла Сантисима Тринидад Руиз Пикассо'
print(person.name)

try:
    person.name = 'Ира'
except ValueError as e:
    print(e)

# TEST_13:
class Person:
    name = String(maxsize=10)


person = Person()
person.name = 'Ярик'
print(person.name)

try:
    person.name = 'Пабло Диего Хосе Франциско де Паула Хуан Непомукено Криспин Криспиано де ла Сантисима Тринидад Руиз Пикассо'
except ValueError as e:
    print(e)

# TEST_14:
class Person:
    name = String()


person = Person()
person.name = 'О'
print(person.name)

person.name = 'Выквырагтыргыргын Валерий'
print(person.name)

# TEST_15:
class PositiveNumber:
    num = Number(0)


positivenumber = PositiveNumber()
positivenumber.num = 0
print(positivenumber.num)

try:
    positivenumber.num = -1
except ValueError as e:
    print(e)

# TEST_16:
class Student:
    age = Number(18, 99)


student = Student()
try:
    print(student.age)
except AttributeError as e:
    print(e)

# TEST_17:
class Student:
    age = Number(18, 99)

print(Student.age.__class__)