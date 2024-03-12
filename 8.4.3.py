'''
Декоратор @takes_numbers
Реализуйте класс декоратор @takes_numbers, который проверяет, что все аргументы, передаваемые в декорируемую функцию, принадлежат типам int или float. Если хотя бы один аргумент принадлежит какому-либо другому типу, должно быть возбуждено исключение TypeError с текстом:

Аргументы должны принадлежать типам int или float
Примечание 1. Не забывайте, что декоратор не должен поглощать возвращаемое значение декорируемой функции, а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый декоратор @takes_numbers, но не код, вызывающий его.
'''

from functools import update_wrapper

class takes_numbers:
    def __init__(self,func):
        self.func = func
        update_wrapper(self,func)
        
    def __call__(self,*args,**kwargs):
        for i in (*args,*kwargs.values()):
            if not isinstance(i,(int,float)):
                raise TypeError ('Аргументы должны принадлежать типам int или float')
        return self.func(*args,**kwargs)
@takes_numbers
def mul(a, b):
    return a * b
    
try:
    print(mul(1, '2'))
except TypeError as error:
    print(error)