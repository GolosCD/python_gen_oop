from collections.abc import MutableSequence

class SortedList(MutableSequence):
    def __init__(self, data :list = None):
        self.data = sorted(data)[:] if data else []
        
    def __str__(self):
        return f'SortedList({self.data})'
        
    def append(self,value):
        raise NotImplementedError
    def insert(self,index,value):
        raise NotImplementedError
    def extend(self,value):
        raise NotImplementedError
    def __reversed__(self):
        raise NotImplementedError
    def __getitem__(self,i):
        return self.data[i]       
    def __setitem__(self,i,value):
        raise NotImplementedError
        
    def __delitem__(self, i):
        del self.data[i]    
        
    def __len__(self):
        return len(self.data)
        
    def __add__(self,other):
        if isinstance(other, SortedList):
            return self.__class__(self.data + other.data)
        elif isinstance(other, type(self.data)):
            return self.__class__(self.data + other)
        return self.__class__(self.data + list(other))
        
    def __iadd__(self, other):
        if isinstance(other, SortedList):
            self.data += other.data
        elif isinstance(other, type(self.data)):
            self.data += other
        else:
            self.data += list(other)
        return self.__class__(self.data)        
        
    def add(self,obj):
        if isinstance(obj,(int,float)):
            self.data.append(obj)
        else:
            self.data.extend(obj)
        self.data.sort()
        
    def discard (self,value):
        self.data = [i for i in self.data if i!=value]
        self.data.sort()
        
    def update(self,obj):
        if isinstance(obj,(int,float)):
            self.data.append(obj)
        else:
            self.data.extend(obj)
        self.data.sort()
        
    def __mul__(self,other):
        self.data=list.__mul__(self.data,other) 
        return self.__class__(self.data)    

        





# INPUT DATA:

# TEST_1:
print('# TEST_1:')
numbers = SortedList([5, 3, 4, 2, 1])


print(numbers)
print(numbers[1])
print(numbers[-2])
numbers.add(0)
print(numbers)
numbers.discard(4)
print(numbers)
numbers.update([4, 6])
print(numbers)

# TEST_2:
print('# TEST_2:')
numbers = SortedList([5, 3, 4, 2, 1])

print(len(numbers))
print(*numbers)
print(1 in numbers)
print(6 in numbers)

# TEST_3:
print('# TEST_3:')
numbers1 = SortedList([1, 3, 5])
numbers2 = SortedList([2, 4])

print(numbers1 + numbers2)
print(numbers1 * 2)
print(numbers2 * 2)

# TEST_4:
print('# TEST_4:')
numbers = SortedList([5, 4, 3, 2, 1])

print(numbers)
del numbers[1]

print(numbers)
del numbers[-1]

print(numbers)

try:
    numbers[0] = 7
except NotImplementedError:
    print('Неподдерживаемая операция')

# TEST_5:
print('# TEST_5:')
numbers = SortedList([1, 2, 3, 4, 5])

try:
    numbers.append(6)
except NotImplementedError:
    print('Неподдерживаемая операция')

# TEST_6:
print('# TEST_6:')
numbers = SortedList([1, 2, 3, 4, 5])

try:
    numbers.insert(0, 0)
except NotImplementedError:
    print('Неподдерживаемая операция')

# TEST_7:
print('# TEST_7:')
numbers = SortedList([1, 2, 3, 4, 5])

try:
    numbers.extend([6, 7, 8, 9, 10])
except NotImplementedError:
    print('Неподдерживаемая операция')

# TEST_8:
print('# TEST_8:')
numbers = SortedList([1, 2, 3, 4, 5])

try:
    numbers.reverse()
except NotImplementedError:
    print('Неподдерживаемая операция')

# TEST_9:
print('# TEST_9:')
numbers = SortedList([1, 2, 3, 4, 5])

try:
    reversed(numbers)
except NotImplementedError:
    print('Неподдерживаемая операция')

# TEST_10:
print('# TEST_10:')
numbers = SortedList([5, 4, 3, 2, 1])

numbers.update([5, 4, 3, 2, 1])
print(*numbers)

numbers *= 3
print(*numbers)

numbers.discard(4)
print(*numbers)

# TEST_11:
print('# TEST_11:')
numbers1 = SortedList([1, 3, 5])
numbers2 = SortedList([2, 4])

id1_numbers1 = id(numbers1)
id1_numbers2 = id(numbers2)

numbers1 += numbers2
numbers2 *= 2

id2_numbers1 = id(numbers1)
id2_numbers2 = id(numbers2)

print(id1_numbers1 == id2_numbers1)
print(id1_numbers2 == id2_numbers2)
print(3 in numbers1)

# TEST_12:
print('# TEST_12:')
data = [5, 4, 3, 2, 1]
numbers = SortedList(data)

print(numbers)
data.pop()

print(data)
print(numbers)

# TEST_13:
print('# TEST_13:')
numbers = SortedList()
print(numbers)

# TEST_14:
print('# TEST_14:')
numbers1 = SortedList([5, 3, 4, 2, 1])
numbers2 = SortedList([10, 9, 8, 7, 6])

numbers1 = numbers1 + numbers2
print(numbers1, type(numbers1))

numbers2 = numbers2 * 2
print(numbers2, type(numbers2))

# TEST_15:
print('# TEST_15:')
numbers1 = SortedList([5, 3, 4, 2, 1])
numbers2 = SortedList([10, 9, 8, 7, 6])

numbers1 += numbers2
print(numbers1, type(numbers1))

numbers2 *= 2
print(numbers2, type(numbers2))

# TEST_16:
print('# TEST_16:')
numbers1 = SortedList([5, 3, 4, 2, 1])
numbers2 = SortedList([10, 9, 8, 7, 6])

numbers1 = numbers1 * -100
print(numbers1)

numbers2 *= 0
print(numbers2)

# TEST_17:
print('# TEST_17:')
numbers = SortedList([5, 3, 4, 2, 1])
print(numbers.__add__(1))
print(numbers.__iadd__(1.1))
print(numbers.__mul__([1, 2, 3]))
print(numbers.__imul__({4, 5, 6}))
