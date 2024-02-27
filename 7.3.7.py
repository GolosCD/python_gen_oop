'''
Класс AdvancedTuple
Реализуйте класс AdvancedTuple, наследника класса tuple, который описывает кортеж, умеющий выполнять операцию сложения (+, +=) не только с экземплярами классов AdvancedTuple и tuple, но и с любыми итерируемыми объектами. Процесс создания экземпляра класса AdvancedTuple должен совпадать с процессом создания экземпляра класса tuple.

Примечание 1. Как бы ни выполнялось сложение, с помощью оператора + или +=, результатом операции должен являться новый экземпляр класса AdvancedTuple.

Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 3. Никаких ограничений касательно реализации класса AdvancedTuple нет, она может быть произвольной.
'''


# мой ответ
class AdvancedTuple(tuple):

    def __new__(cls,value):
        instance = tuple.__new__(cls,value)
        instance.value = tuple.__new__(cls,value)
        return instance
        
    def __add__(self,other):
        result_add = tuple.__add__(self,self.create_tuple(other))
        return AdvancedTuple(result_add)
            
    def __radd__(self,other):
        result_add = tuple.__add__(self.create_tuple(other),self)
        return AdvancedTuple(result_add)       
        
    def create_tuple(self,sequence) -> tuple:
        ''' На вход принимает любое значение,
            если это последовательность, то
            рекурсивно ее перебирает.
            На выходе всегда возращает кортеж '''
            
        result = []
        for item in sequence:
            if not isinstance(item, (int,str)):
                result.extend(self.create_tuple(item))
            else:
                result.append(item)
        return tuple(result)\
        
# нормальный ответ
class AdvancedTuple(tuple):
    def __add__(self, other):
        return AdvancedTuple(tuple(self) + tuple(other))

    def __radd__(self, other):
        return AdvancedTuple(tuple(other) + tuple(self))        
  
        
# INPUT DATA:

# TEST_1:
advancedtuple = AdvancedTuple([1, 2, 3])

print(advancedtuple + (4, 5))
print(advancedtuple + [4, 5])
print({'a': 1, 'b': 2} + advancedtuple)

# TEST_2:
advancedtuple = AdvancedTuple([1, 2, 3])

advancedtuple += [4, 5]
advancedtuple += iter([6, 7, 8])
print(advancedtuple)
print(type(advancedtuple))

# TEST_3:
data = [[4, 5, 6], {4: None, 5: None, 6: None}, (4, 5, 6), '456', iter([4, 5, 6]), AdvancedTuple([4, 5, 6])]

advancedtuple = AdvancedTuple([1, 2, 3])

for item in data:
    print(advancedtuple + item, end=' ')
    print(item + advancedtuple)

# TEST_4:
data = ['456', [7, 8, 9], {10: None, 11: None, 12: None}, (13, 14, 15), iter([16, 17, 18]), AdvancedTuple([20, 21, 22])]

advancedtuple = AdvancedTuple([1, 2, 3])

for item in data:
    advancedtuple += item

print(advancedtuple)

# TEST_5:
advancedtuple = AdvancedTuple([1, 2, 3])
advancedtuple += []
print(advancedtuple)        