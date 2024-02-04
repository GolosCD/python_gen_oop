'''
Класс RandomLooper
Реализуйте класс RandomLooper. При создании экземпляра класс должен принимать произвольное количество позиционных аргументов, каждый из которых является итерируемым объектом.

Экземпляр класса RandomLooper должен являться итератором, который генерирует в случайном порядке все элементы всех итерируемых объектов, переданных в конструктор, а затем возбуждает исключение StopIteration.

Примечание 1. Порядок элементов в возвращаемом итераторе необязательно должен совпадать с их порядком в тестовых данных.

Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 3. Класс RandomLooper должен удовлетворять протоколу итератора, то есть иметь методы __iter__() и __next__(). Реализация же протокола может быть произвольной.
'''
import random as r

class RandomLooper:
    def __init__(self,*args):
        tmp_list = [value for obj in args for value in obj]
        r.shuffle(tmp_list)
        self.iterable =iter(tmp_list)
        
    def __iter__(self):
        return self
        
    def __next__(self):
        return next(self.iterable)
        
        
randomlooper = RandomLooper(['red', 'blue', 'green', 'purple'],['black'])


# print(randomlooper.iterable)

print(list(randomlooper))
print(list(randomlooper))        