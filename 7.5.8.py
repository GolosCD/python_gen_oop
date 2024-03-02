'''
Класс SortedList
Реализуйте класс SortedList, описывающий список, который автоматически сортируется при создании и любом изменении. При создании экземпляра класс должен принимать один аргумент:

iterable — итерируемый объект, определяющий начальный набор элементов отсортированного списка. Если не передан, начальный набор элементов считается пустым
Класс SortedList должен иметь три метода экземпляра:

add() — метод, принимающий в качестве аргумента произвольный объект и добавляющий его в экземпляр класса SortedList
discard() — метод, принимающий в качестве аргумента произвольный объект и удаляющий все его включения из экземпляра класса SortedList, если он в нем присутствует
update() — метод, принимающий в качестве аргумента итерируемый объект и добавляющий все его элементы в экземпляр класса SortedList
Также класс SortedList должен иметь такие методы экземпляра, как append(), insert(), extend() и reverse(), при попытке воспользоваться которыми должно быть возбуждено исключение NotImplementedError.

Экземпляр класса SortedList должен иметь следующее формальное строковое представление:

SortedList([<первый элемент списка>, <второй элемент списка>, ...])
При передаче экземпляра класса SortedList в функцию len() должно возвращаться количество элементов в нем. При попытке передачи экземпляра класса SortedList в функцию reversed() должно быть возбуждено исключение NotImplementedError.

Помимо этого, экземпляр класса SortedList должен быть итерируемым объектом, то есть позволять перебирать свои элементы, например, с помощью цикла for.

Также экземпляр класса SortedList должен поддерживать операцию проверки на принадлежность с помощью оператора in.

Вдобавок ко всему, экземпляр класса SortedList должен позволять получать и удалять значения своих элементов с помощью индексов, причем как положительных, так и отрицательных. При попытке изменить значение элемента по его индексу должно быть возбуждено исключение NotImplementedError.

Экземпляры класса SortedList должны поддерживать между собой арифметические операции с помощью операторов + и +=:

оператор + должен выполнять операцию сложения двух отсортированных списков путем их конкатенации и последующей сортировки. Результатом работы оператора должен являться новый экземпляр класса SortedList
оператор += должен выполнять операцию сложения двух отсортированных списков путем их конкатенации и последующей сортировки. Результатом работы оператора должен являться левый экземпляр класса SortedList
Наконец, экземпляр класса SortedList должен поддерживать операцию умножения на целое число n с помощью операторов * и *=:

оператор * должен выполнять операцию умножения отсортированного списка на число с последующей его сортировкой. Результатом работы оператора должен являться новый экземпляр класса SortedList
оператор *= должен выполнять операцию умножения отсортированного списка на число с последующей его сортировкой. Результатом работы оператора должен являться левый экземпляр класса SortedList
Примечание 1. Гарантируется, что элементами одного экземпляра класса SortedList являются объекты, сравнимые между собой.

Примечание 2. Перед решением подумайте, какой абстрактный класс из модуля collections.abc будет удобен в качестве родительского.

Примечание3. Экземпляр класса SortedList не должен зависеть от итерируемого объекта, на основе которого он был создан. Другими словами, если исходный итерируемый объект изменится, то экземпляр класса SortedList измениться  не должен.

Примечание 4.  Если объект, с которым выполняется арифметическая операция, некорректен, метод, реализующий операцию сравнения, должен вернуть константу NotImplemented.

Примечание 5. Никаких ограничений касательно реализации класса SortedList нет, она может быть произвольной. Однако попробуйте решить задачу так, чтобы операция добавления элементов в список выполнялась как можно быстрее.
'''

#Моя реализация
from collections.abc import MutableSequence

class SortedList(MutableSequence):
    def __init__(self, data :list = None):
        self.data =[]
        self.data[:] = sorted(data) if data else []
        
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
        if not isinstance(other, SortedList):
            return NotImplemented
        return self.__class__(self.data + other.data)
           
    def __iadd__(self, other):
        if not isinstance(other, SortedList):
            return NotImplemented 
        self.data += other.data
        self.data.sort()
        return self        
        
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
        if not isinstance(other, int):
            return NotImplemented
        self.data=self.data*other
        self.data.sort()
        return self
        
    def __imul__(self,other):
        if not isinstance(other, int):
            return NotImplemented
        self.data*=other
        self.data.sort()
        return self    
#Реализация Валерия с читами
'''
Модуль bisect реализует алгоритм двоичного поиска. Документация по нему на русском и английском языках.

Так же вам может быть интересен этот модуль.
'''
from bisect import bisect_left, bisect_right, insort
from collections.abc import MutableSequence


class SortedList(MutableSequence):
    def __init__(self, iterable=()):
        self._data = sorted(iterable)

    def add(self, obj):
        insort(self._data, obj)

    def discard(self, obj):
        left = bisect_left(self._data, obj)
        right = bisect_right(self._data, obj)
        self._data[left:right] = []

    def update(self, iterable):
        for it in iterable:
            self.add(it)

    def __getitem__(self, index):
        return self._data[index]

    def __delitem__(self, index):
        del self._data[index]

    def __len__(self):
        return len(self._data)

    def __contains__(self, item):
        return item in self._data

    def __iter__(self):
        yield from self._data

    def __add__(self, other):
        if isinstance(other, type(self)):
            return type(self)(self._data + other._data)
        return NotImplemented

    def __iadd__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        self.update(other._data)
        return self

    def __mul__(self, other):
        if isinstance(other, int):
            return type(self)(self._data * other)
        return NotImplemented

    def __imul__(self, other):
        if not isinstance(other, int):
            return NotImplemented
        self._data.clear() if other <= 0 else self.update(self._data * (other - 1))
        return self

    def __repr__(self):
        return f'SortedList({self._data})'

    def append(self, value):
        raise NotImplementedError

    def insert(self, index, value):
        raise NotImplementedError

    def extend(self, values):
        raise NotImplementedError

    def reverse(self):
        raise NotImplementedError

    def __reversed__(self):
        raise NotImplementedError

    def __setitem__(self, key, value):
        raise NotImplementedError        

#Как по мне лучшая реализация с декоратором
from collections import UserList
from collections.abc import Iterable
from functools import wraps
from typing import Any, Callable, Iterable, Iterator, NoReturn, Optional


class SortedList(UserList):
    def __init__(self, iterable: Optional[Iterable] = None):
        super().__init__(iterable)
        self.sort()

    @staticmethod
    def __raise_not_implemented(func: Callable) -> Callable[..., NoReturn]:
        """Декоратор, райзящий ошибку при обращении к функции"""

        @wraps(func)
        def wrapper(*args, **kwargs) -> NoReturn:
            raise NotImplementedError

        return wrapper

    @staticmethod
    def __int_only(func: Callable):
        """Декоратор для валидации типов аргументов"""

        @wraps(func)
        def wrapper(self, n):
            if not isinstance(n, int):
                return NotImplemented
            return func(self, n)

        return wrapper

    @staticmethod
    def __self_type_only(func: Callable):
        """Декоратор для проверки, что второй аргумент того же класса"""

        @wraps(func)
        def wrapper(self, iterable):
            if not isinstance(iterable, self.__class__):
                return NotImplemented
            return func(self, iterable)

        return wrapper

    def sort(self):
        self.data.sort()

    def add(self, obj: Any):
        self.data.append(obj)
        self.sort()

    def discard(self, obj: Any):
        while obj in self.data:
            self.data.remove(obj)

    def update(self, iterable: Iterable):
        self.data.extend(iterable)
        self.sort()

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.data})"

    @__self_type_only
    def __add__(self, other):
        result = super().__add__(other)
        result.sort()
        return result

    @__self_type_only
    def __iadd__(self, other):
        super().__iadd__(other)
        self.sort()
        return self

    @__int_only
    def __mul__(self, n: int):
        result = super().__mul__(n)
        result.sort()
        return result

    @__int_only
    def __imul__(self, n: int):
        super().__imul__(n)
        self.sort()
        return self

    @__raise_not_implemented
    def __setitem__(self, index: int, value: Any): ...

    @__raise_not_implemented
    def append(self, item: Any) -> None: ...

    @__raise_not_implemented
    def insert(self, i: int, item: Any) -> None: ...

    @__raise_not_implemented
    def extend(self, other: Iterable) -> None: ...

    @__raise_not_implemented
    def reverse(self) -> None: ...

    @__raise_not_implemented
    def __reversed__(self) -> Iterator: ...

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
