'''
Класс BitArray
Реализуйте класс BitArray, описывающий битовый список, то есть список, элементами которого являются только нули и единицы. При создании экземпляра класс должен принимать один аргумент:

iterable — итерируемый объект, определяющий начальный набор элементов битового списка. Если не передан, начальный набор считается пустым
Экземпляр класса BitArray должен иметь следующее неформальное строковое представление:

[<первый элемент битового списка>, <второй элемент битового списка>, ...]
При передаче экземпляра класса BitArray в функцию len() должно возвращаться количество элементов в нем. При передаче экземпляра класса BitArray в функцию reversed() должен возвращаться итератор, элементами которого являются элементы переданного экземпляра класса BitArray , расположенные в обратном порядке.

Экземпляр класса BitArray должен быть итерируемым объектом, то есть позволять перебирать свои элементы, например, с помощью цикла for.

Помимо этого, экземпляр класса BitArray должен поддерживать операцию проверки на принадлежность с помощью оператора in.

Также экземпляр класса BitArray должен позволять получать значения своих элементов с помощью индексов, причем как положительных, так и отрицательных.

Вдобавок ко всему, экземпляр класса BitArray должен поддерживать унарный оператор ~, выполняющий операцию логического отрицания для каждого бита битового списка, тем самым преобразуя 0 в 1, а 1 в 0. Результатом работы оператора должен являться новый экземпляр класса BitArray.

Наконец, экземпляры класса BitArray должны поддерживать между собой логические операции с помощью операторов & и |:

оператор & должен выполнять операцию логического И над каждой парой битов двух битовых списков равной длины. Результатом работы оператора должен являться новый экземпляр класса BitArray

оператор | должен выполнять операцию логического ИЛИ над каждой парой битов двух битовых списков равной длины. Результатом работы оператора должен являться новый экземпляр класса BitArray

Примечание 1. Перед решением подумайте, какой абстрактный класс из модуля collections.abc будет удобен в качестве родительского.

Примечание 2. Экземпляр класса BitArray не должен зависеть от итерируемого объекта, на основе которого он был создан. Другими словами, если исходный итерируемый объект изменится, то экземпляр класса BitArray измениться  не должен.

Примечание 3. Если объект, с которым выполняется логическая операция, некорректен, метод, реализующий эту операцию, должен вернуть константу NotImplemented.

Примечание 4. Никаких ограничений касательно реализации класса BitArray нет, она может быть произвольной.
'''

from collections.abc import Set


class BitArray(Set):
        
    def __init__(self,data=None):
        self.data = data[:] if data else []
        
    def __repr__(self):
        return f"{self.data}"        
        
    def __invert__(self):
        return BitArray([int(not i) for i in self.data])
        
    def __contains__(self,item):
        return item in self.data
        
    def __iter__(self):
        return iter(self.data)
    
    def __len__(self):
        return len(self.data)
        
    def __getitem__(self,index):
        return self.data[index]
        
    def __setitem__(self, index, value):
        self.data[index] = value        
        
    def __and__(self, other):
        if not isinstance(other,BitArray):
            return NotImplemented
        if len(self) != len(other):
            raise TypeError
        return BitArray([a & b for a, b in zip(self, other)])

    def __or__(self, other):
        if not isinstance(other,BitArray):
            return NotImplemented
        if len(self) != len(other): 
            raise TypeError
        return BitArray([a | b for a, b in zip(self, other)])

# from collections.abc import MutableSequence

# class BitArray(MutableSequence):
    # def __init__(self, iterable=None):
        # self._data = []
        # if iterable:
            # self._data.extend([1 if item else 0 for item in iterable])

    # def __repr__(self):
        # return f"{self._data}"

    # def __len__(self):
        # return len(self._data)

    # def __getitem__(self, index):
        # return self._data[index]

    # def __setitem__(self, index, value):
        # self._data[index] = value

    # def __delitem__(self, index):
        # del self._data[index]

    # def __iter__(self):
        # return iter(self._data)

    # def __contains__(self, item):
        # return item in self._data

    # def __invert__(self):
        # return BitArray([0 if item else 1 for item in self._data])

    # def __and__(self, other):
        # if len(self) != len(other):
            # return NotImplemented
        # return BitArray([a & b for a, b in zip(self, other)])

    # def __or__(self, other):
        # if len(self) != len(other):
            # return NotImplemented
        # return BitArray([a | b for a, b in zip(self, other)])

    # def insert(self, index, value):
        # self._data.insert(index, value)


# INPUT DATA:
'''
# TEST_1:
bitarray = BitArray([1, 0, 1, 1])

print(bitarray)
print(~bitarray)
print(bitarray[0])
print(bitarray[1])
print(bitarray[-1])
print(0 in bitarray)
print(1 not in bitarray)

# TEST_2:
bitarray1 = BitArray([1, 0, 1, 1])
bitarray2 = BitArray([0, 0, 0, 1])

bitarray3 = bitarray1 | bitarray2
bitarray4 = bitarray1 & bitarray2
bitarray5 = ~bitarray1

print(bitarray3, type(bitarray3))
print(bitarray4, type(bitarray4))
print(bitarray5, type(bitarray5))

# TEST_3:
data = [1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1,
        1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0]

bitarray = BitArray(data)

print(*bitarray)
print(*reversed(bitarray))
print(~bitarray)
'''
# TEST_4:
data = [1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0,
        0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0]

bitarray = BitArray(data)

print(bitarray)
data.extend([0, 0, 1, 0, 1, 1])

print(data)
print(bitarray)
'''
# TEST_5:
data1 = [0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1,
         1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0]

data2 = [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1,
         1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1]

bitarray1 = BitArray(data1)
bitarray2 = BitArray(data2)


print(len(bitarray1) == len(bitarray2))
print(bitarray1 | bitarray2)
print(bitarray1 & bitarray2)

# TEST_6:
bitarray = BitArray([1, 0, 1, 1])
print(bitarray.__or__(1))
print(bitarray.__and__(1.1))

# TEST_7:
bitarray = BitArray()
print(bitarray)

# TEST_8:
data1 = [0, 1, 1, 0, 0, 1]
data2 = [1, 1, 1, 1, 1]

bitarray1 = BitArray(data1)
bitarray2 = BitArray(data2)

try:
    print(bitarray1 | bitarray2)
except TypeError:
    print('Списки должны быть равной длины')

try:
    print(bitarray1 & bitarray2)
except TypeError:
    print('Списки должны быть равной длины')'''