'''
Класс Formatter
Реализуйте класс Formatter. При создании экземпляра класс не должен принимать никаких аргументов.

Класс Formatter должен иметь один статический метод:

format() — метод, принимающий в качестве аргумента объект типа int, float, tuple, list или dict и выводящий информацию о переданном объекте в формате, зависящем от его типа. Если переданный объект принадлежит какому-либо другому типу, должно быть возбуждено исключение TypeError с текстом:
Аргумент переданного типа не поддерживается
Примечание 1. Примеры форматирования объектов всех типов показаны в тестовых данных.

Примечание 2. Обратите внимание, что метод format() должен обрамлять апострофами строковые элементы коллекций.

Примечание 3. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 4. Никаких ограничений касательно реализации класса Formatter нет, она может быть произвольной.
'''
from functools import singledispatch

class Formatter:

    @singledispatch
    @staticmethod
    def format(data):
        raise TypeError ('Аргумент переданного типа не поддерживается')
        
    @format.register(float)
    @format.register(int)
    @staticmethod
    def _from_format(data):
        txt = "Целое" if isinstance(data,int) else "Вещественное"
        print( f'{txt} число: {data}')
    
    @format.register(list)
    @format.register(tuple)
    @staticmethod
    def _from_format(data):
        txt = "списка" if isinstance(data,list) else "кортежа"
        obj = [str(i) for i in data]
        print( f'Элементы {txt}: {", ".join(obj)}')    
        
    @format.register(dict)
    @staticmethod
    def _from_format(data):
        obj = [str(i) for i in data.items()]
        print( f'Пары словаря: {", ".join(obj)}')      
    
Formatter.format([10, 20, 30, 40, 50])
Formatter.format(([1, 3], [2, 4, 6]))    