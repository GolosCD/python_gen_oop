'''
Декоратор @CachedFunction
Реализуйте декоратор @CachedFunction, который кэширует вычисленные значения декорируемой функции. Кэш должен быть доступен по атрибуту cache и представлять собой словарь, ключом в котором является кортеж с аргументами, а значением — возвращаемое значение декорируемой функции при вызове с этими аргументами.

Примечание 1. Для однозначного кеширования гарантируется, что декорируемая функция принимает только позиционные аргументы.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый декоратор @CachedFunction, но не код, вызывающий его.
'''

class CachedFunction:
    def __init__ (self,func):
        self.func = func
        self.cache = dict()
        
    def __call__ (self,*args):
        if args not in self.cache:
            self.cache[args] = self.func(*args)
        return self.cache[args]    


@CachedFunction
def slow_fibonacci(n):
    if n == 1:
        return 0
    elif n in (2, 3):
        return 1
    return slow_fibonacci(n - 1) + slow_fibonacci(n - 2)
    
print(slow_fibonacci(100))
Sample Output 1:

218922995834555169026
Sample Input 2:

@CachedFunction
def slow_fibonacci(n):
    if n == 1:
        return 0
    elif n in (2, 3):
        return 1
    return slow_fibonacci(n - 1) + slow_fibonacci(n - 2)
    
slow_fibonacci(5)

for args, value in sorted(slow_fibonacci.cache.items()):
    print(args, value)
Sample Output 2: