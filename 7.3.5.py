'''
Класс SuperInt
Реализуйте класс SuperInt, наследника класса int, описывающий целое число с дополнительным функционалом. Процесс создания экземпляра класса SuperInt должен совпадать с процессом создания экземпляра класса int.

Класс SuperInt должен иметь четыре метода экземпляра:

repeat() — метод, принимающий в качестве аргумента целое число n, по умолчанию равное 2, и возвращающий экземпляр класса SuperInt, продублированный n раз
to_bin() — метод, возвращающий двоичное представление экземпляра класса SuperInt. Двоичное представление может быть как в виде экземпляра класса str, так и int
next() — метод, возвращающий новый экземпляр класса SuperInt, который больше текущего на единицу
prev() — метод, возвращающий новый экземпляр класса SuperInt, который меньше текущего на единицу
Также экземпляр класса SuperInt должен быть итерируемым объектом, элементами которого являются его цифры слева направо. Сами цифры так же должны быть представлены в виде экземпляров класса SuperInt.

Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса SuperInt нет, она может быть произвольной.
'''

class SuperInt(int):
    def __new__(cls,n):
        return int.__new__(cls,n)
        
    def repeat(self,n=2):
        if self>0:
            return SuperInt(str(self)*n)
        return f'-{str(abs(self))*n}'  

    def to_bin(self):
        return f'{self:b}'
        
    def next(self):
        return SuperInt(self+1)
        
    def prev(self):    
        return SuperInt(self-1)
        
    def __iter__(self):
        return (SuperInt(i) for i in str(abs(self)))
        
# INPUT DATA:

# TEST_1:
superint1 = SuperInt(17)
superint2 = SuperInt(-17)

print(superint1.repeat())
print(superint2.repeat(3))

# TEST_2:
superint1 = SuperInt(17)
superint2 = SuperInt(-17)

print(superint1.to_bin())
print(superint2.to_bin())

# TEST_3:
superint = SuperInt(17)

print(superint.prev())
print(superint.next())

# TEST_4:
superint1 = SuperInt(1337)
superint2 = SuperInt(-2077)

print(*superint1)
print(*superint2)

# TEST_5:
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
superint = SuperInt(30)

for n in digits:
    print(superint.repeat(n))

# TEST_6:
superint = SuperInt(30)

for i in range(10):
    superint = superint.next()
    print(superint)

# TEST_7:
superint = SuperInt(30)

for i in range(10):
    superint = superint.prev()
    print(superint)

# TEST_8:
superint = SuperInt(50)

for i in range(0, 50, 3):
    superint = superint.next()
    print(superint.to_bin())

# TEST_9:
superint = SuperInt(-200)

for i in range(0, 100, 3):
    superint = superint.next()
    print(superint.to_bin())

# TEST_10:
superint = SuperInt(50)

for i in range(0, 50, 3):
    superint = superint.next()
    print(*superint)

# TEST_11:
superint = SuperInt(-200)

for i in range(0, 100, 3):
    superint = superint.next()
    print(*superint)

# TEST_12:
superint = SuperInt(100)
print(type(superint))
print(type(superint.next()))
print(type(superint.prev()))
print(type(superint.repeat()))

# TEST_13:
superint1 = SuperInt(2023)

for item in superint1:
    print(item, type(item))