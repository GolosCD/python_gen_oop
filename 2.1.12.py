'''
Функция intersperse()
Реализуйте генераторную функцию intersperse(), которая принимает два аргумента в следующем порядке:

iterable — итерируемый объект
delimiter — значение-разделитель
Функция должна возвращать генератор, порождающий последовательность из элементов итерируемого объекта iterable, между которыми располагается значение-разделитель delimiter.

Примечание 1. Рассмотрим первый тест, в котором в качестве итерируемого объекта передается список чисел от 1 до 3, а в качестве значения-разделителя — 0. Порождаемая генератором последовательность состоит из чисел 1, 2 и 3, между которыми располагается число 0:

1 0 2 0 3
Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию intersperse(), но не код, вызывающий ее.
'''
import itertools as it

from typing import Any,Generator

def intersperse(iterable :Any, delimetr :int|str) ->Generator:
    
    
    #Делаем две копии итератора, что бы одну копию пустить на расчет длинны итератора
    iterable,copy_iterable =  it.tee(iterable,2)
    
    # используем zip_longest поэтмоу получаем лишний символ разделителя
    # что бы его отрезать используем islice которому нужно четко передать длинну итератора мину 1 лишний символ
    max_ln = max(0,(len(list(copy_iterable))*2)-1)
  
    return it.islice((j for i in it.zip_longest(iterable,it.repeat(iterable,0),fillvalue=delimetr) for j in i),0,max_ln)




# INPUT DATA:

# TEST_1:
print(*intersperse([1, 2, 3], 0))

# TEST_2:
inter = intersperse('beegeek', '!')
print(next(inter))
print(next(inter))
print(*inter)

# TEST_3:
print(*intersperse('A', '...'))

# TEST_4:
print(*intersperse(range(5), '>'))

# TEST_5:
iterable = iter('Beegeek')

print(*intersperse(iterable, '+'))

# TEST_6:
iterable = iter('Be')

print(*intersperse(iterable, '---'))

# TEST_7:
print(*intersperse([], 100))

# TEST_8:
print(*intersperse('beegeek', '   '))

# TEST_9:
data = intersperse(range(5), -1)
print(list(data))

# TEST_10:
data = intersperse(range(5), '!!!')
print(list(data))

# TEST_11:
data = intersperse(['John Warner Backus', 5, 'Niklaus Emil Wirth', True, 'Lawrence Gordon Tesler', None, {1, 2, 3}, {'hello': 'world'}], '—')
print(list(data))



'''
# OUTPUT DATA:

# TEST_1:
1 0 2 0 3

# TEST_2:
b
!
e ! e ! g ! e ! e ! k

# TEST_3:
A

# TEST_4:
0 > 1 > 2 > 3 > 4

# TEST_5:
B + e + e + g + e + e + k

# TEST_6:
B --- e

# TEST_7:


# TEST_8:
b     e     e     g     e     e     k

# TEST_9:
[0, -1, 1, -1, 2, -1, 3, -1, 4]

# TEST_10:
[0, '!!!', 1, '!!!', 2, '!!!', 3, '!!!', 4]

# TEST_11:
['John Warner Backus', '—', 5, '—', 'Niklaus Emil Wirth', '—', True, '—', 'Lawrence Gordon Tesler', '—', None, '—', {1, 2, 3}, '—', {'hello': 'world'}]

'''