'''
Декоратор @CountCalls
Реализуйте декоратор @CountCalls, который считает количество вызовов декорируемой функции. Счетчик вызовов должен быть доступен по атрибуту calls.

Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции, а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый декоратор @CountCalls, но не код, вызывающий его.
'''


class CountCalls:
    def __init__(self,func,calls=0):
        self.func = func
        self.calls = calls
        
    def __call__(self,*args,**kwargs):
        self.calls +=1
        return self.func(*args,**kwargs)
        
        
@CountCalls
def square(a):
    return a ** 2
    
for i in range(100):
    square(i)
    
print(square.calls)        