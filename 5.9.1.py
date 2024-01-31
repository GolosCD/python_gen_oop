'''
Функция hash_function()
Реализуйте функцию hash_function(), которая принимает один аргумент:

obj — произвольный объект
Функция должна вычислять хеш-значение объекта obj согласно следующему алгоритму:

вычисление значения выражения:
ord(obj[0]) * ord(obj[-1]) + ord(obj[1]) * ord(obj[-2]) + ord(obj[2]) * ord(obj[-3]) + ...
где obj — объект, преобразованный в строку с помощью функции str(). Обратите внимание, что суммироваться должны произведения первого и последнего элементов, второго и предпоследнего, и так далее до середины. Если obj имеет нечетное количество символов, то серединный элемент должен прибавляться без перемножения
вычисление значения выражения:
ord(obj[0]) * 1 - ord(obj[1]) * 2 + ord(obj[2]) * 3 - ord(obj[3]) * 4 + ...
где obj — объект, преобразованный в строку с помощью функции str()
вычисление значения выражения:
(temp1 * temp2) % 123456791
где temp1 — значение, полученное в первом шаге, temp2 — значение, полученное во втором шаге
и возвращать значение, полученное в третьем шаге.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию hash_function(), но не код, вызывающий ее.
'''


import math as m
from functools import reduce

def hash_function(obj_i):
    obj = str(obj_i)
    
    def _first():
        #расчет длина строки
        seq_len = len(obj)
        
        #первая часть ключа
        first_val = sum(ord(obj[i])*ord(obj[~i]) for i in range(seq_len//2))
        
        if len(obj) % 2 != 0:
            first_val += ord(obj[seq_len// 2])
        return first_val
    
    def _two():
        total_list = [ord(value)*~index if (~index*-1)%2==0 else ord(value)*~index*-1 for index,value in enumerate(obj)]
        print(total_list)
        second_val = reduce(lambda x,y: x+y,total_list,0)
        print(second_val)
        return second_val
        
    return (_first() * _two()) % 123456791    
            


# INPUT DATA:

# TEST_1:
print(hash_function('python'))

# TEST_2:
print(hash_function(12345))

# TEST_3:
print(hash_function(None))

# TEST_4:
print(hash_function([1, 2, 3, 'python']))

# TEST_5:
array = [8022, 530.602391530928, 'lycmfojREEBSKNcNoIjM', False, {'написать': False, 'собеседник': True},
         (1448, True, -3913.85417440914, True),
         [True, True, 554, 'FCLRrFheVhkrubirMUts', -33242154218.4859, 885507704053.121]]

for obj in array:
    print(hash_function(obj))

