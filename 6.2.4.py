'''
Класс SequenceZip
Реализуйте класс SequenceZip. При создании экземпляра класс должен принимать произвольное количество позиционных аргументов, каждый из которых является последовательностью. Класс SequenceZip должен описывать последовательность, элементами которой являются элементы переданных в конструктор итерируемых объектов, объединенные в кортежи. Объединение должно происходить аналогично тому, как это делает функция zip().

При передаче экземпляра класса SequenceZip в функцию len() должно возвращаться количество элементов в нем.

Также экземпляр класса SequenceZip должен быть итерируемым объектом, то есть позволять перебирать свои элементы, например, с помощью цикла for.

Наконец, экземпляр класса SequenceZip должен позволять получать значения своих элементов с помощью индексов.

Примечание 1. Гарантируется, что при доступе к элементам используются только неотрицательные индексы.

Примечание 2. Экземпляр класса SequenceZip не должен зависеть от последовательностей, на основе которых он был создан. Другими словами, если исходные последовательности изменятся, то экземпляр класса SequenceZip измениться  не должен.

Примечание 3. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 4. Никаких ограничений касательно реализации класса SequenceZip нет, она может быть произвольной.
'''
from itertools import zip_longest
import copy

class SequenceZip:
    def __init__(self,*args):
        self.iterable = copy.deepcopy(args)
        
    def __len__(self):
        if self.iterable:
            return min(len(s) for s in self.iterable)
        return 0    
        
    def __iter__(self):   
        for sequence in zip(*self.iterable):
            yield sequence

        
    def __getitem__(self,key):
        return tuple(sequence[key] for sequence in self.iterable)
        
    def __setitem__ (self,key,value):
        self.iterable
     
        
# INPUT DATA:

# TEST_1:
sequencezip = SequenceZip('ABC', ['bee', 'geek', 'python'], [1, 2, 3])

print(list(sequencezip))
# print(tuple(sequencezip))

# TEST_2:
sequencezip = SequenceZip('ABC', ['bee', 'geek', 'python'], [1, 2, 3])

print(len(sequencezip))
print(tuple(sequencezip))
print(sequencezip[1])
print(sequencezip[2])

# TEST_3:
some = SequenceZip(range(5), [1, 2, 3, 4])

# print(some.iterable)

print(len(SequenceZip([1, 2, 3, 4])))
print(len(SequenceZip(range(5), [1, 2, 3, 4])))
print(len(SequenceZip(range(5), [1, 2, 4], 'data')))

# TEST_4:
x, y, z = [1, 2, 3], [4, 5, 6], [7, 8, 9]
sequencezip = SequenceZip(x, y, z)

print(sequencezip[2])
x[-1], z[-1] = z[-1], x[-1]
print(sequencezip[2])

# TEST_5:
many_large_sequences = [range(100000) for _ in range(100)]
# print(many_large_sequences)
sequencezip = SequenceZip(*many_large_sequences)
print(sequencezip[99999])

# TEST_6:
sequencezip = SequenceZip()
print(len(sequencezip))
print(list(sequencezip))

# TET_7:
data1 = [1, 2, 3, 4, 5]
data2 = 'abcde'

sequencezip = SequenceZip(data1, data2)
data1.extend([6, 7, 8, 9, 10])
data2 += 'fghij'

print(data1)
print(data2)
print(len(sequencezip))
print(list(sequencezip)) 