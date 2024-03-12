'''
Декоратор @exception_decorator
Реализуйте класс декоратор @exception_decorator, который возвращает

кортеж (value, None), если декорируемая функция завершила свою работу без возбуждения исключения, где value — возвращаемое значение декорируемой функции
кортеж (None, errortype), если во время выполнения декорируемой функции было возбуждено исключение, где errortype — тип возбужденного исключения
Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции, а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый декоратор @exception_decorator, но не код, вызывающий его. 
'''

from functools import update_wrapper

class exception_decorator:
    def __init__(self,func):
        self.func = func
        update_wrapper(self,func)

    def __call__(self,*args,**kwargs):
        try:
            value = self.func(*args,**kwargs)
            return (value,None)
        except Exception as err:
            return (None,err.__name__)
            
# INPUT DATA:

# TEST_1:
@exception_decorator
def func(x):
    return 2*x + 1
    
print(func(1))
print(func('bee'))

# TEST_2:
@exception_decorator
def f(x, y):
    return x * y
    
print(f('stepik', 10))

# TEST_3:
@exception_decorator
def f(x, y):
    return x * y
    
print(f('stepik', 'stepik'))

# TEST_4:
@exception_decorator
def f(*args, **kwargs):
    return sum(args) + sum(kwargs.values())
    
print(f(1, 2, 3, param1=4, param2=10))

# TEST_5:
@exception_decorator
def f(*args, **kwargs):
    """sum args and kwargs"""
    return sum(args) + sum(kwargs.values())


print(f.__name__)
print(f.__doc__)
print(f(1, 2, 3, param1=4, param2='10'))

# TEST_6:
sum = exception_decorator(sum)

print(sum(['199', '1', 187]))            