'''
 Класс User
Реализуйте класс User, описывающий интернет-пользователя. 
При создании экземпляра класс должен принимать два аргумента в следующем порядке:

name — имя пользователя. Если name не является непустой строкой, 
состоящей только из букв, должно быть возбуждено исключение ValueError с текстом:
Некорректное имя
age — возраст пользователя. Если age не является целым числом, принадлежащим 
отрезку [0; 110], должно быть возбуждено исключение ValueError с текстом:
Некорректный возраст
Экземпляр класса User должен иметь два атрибута:

_name — имя пользователя
_age — возраст пользователя
Класс User должен иметь четыре метода экземпляра:

get_name() — метод, возвращающий имя пользователя
set_name() — метод, принимающий в качестве аргумента значение new_name и 
изменяющий имя пользователя на new_name. Если new_name не является непустой 
строкой, состоящей только из букв, должно быть возбуждено исключение 
ValueError с текстом:
Некорректное имя
get_age() — метод, возвращающий возраст пользователя
set_age() — метод, принимающий в качестве аргумента значение new_age и 
изменяющий возраст пользователя на new_age. Если new_age не является целым 
числом, принадлежащим отрезку [0; 110], должно быть возбуждено исключение 
ValueError с текстом:
Некорректный возраст
Примечание 1. Если при создании экземпляра класса User имя и возраст 
одновременно являются некорректными, должно быть возбуждено исключение, 
связанное с именем.
'''
import re

class User:
    def __init__(self,name,age):
        if re.fullmatch(r'\b[А-Я]{1}[а-я]{1,}\b',str(name)):
            self._name = name
        else:
            raise ValueError ('Некорректное имя')
            
        if age in range(111) and isinstance(age,int):
            self._age = age
        else:
            raise ValueError ('Некорректный возраст')
    
    def get_name(self):
        return self._name
    
    def get_age(self):
        return self._age
        
    def set_name(self,new_name):
        if re.fullmatch(r'\b[А-Я]{1}[а-я]{1,}\b',str(new_name)):
            self._name = new_name
        else:
            raise ValueError ('Некорректное имя')
            
    def set_age(self,new_age):
        if new_age in range(111) and isinstance(new_age,int):
            self._age = new_age
        else:
            raise ValueError ('Некорректный возраст')
            
            