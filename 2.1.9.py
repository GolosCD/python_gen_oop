'''
Функция is_integer()
Целым числом будем считать последовательность из одной или более цифр, которая может начинаться с необязательного символа дефиса -.

Реализуйте функцию is_integer(), которая принимает один аргумент:

string — строка, содержащая произвольный набор символов
Функция должна возвращать True, если строка string представляет собой целое число, или False в противном случае.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию is_integer(), но не код, вызывающий ее.
'''

def is_integer(string):
    try:
        int(string)
        return True
    except:
        return False

# INPUT DATA:

# TEST_1:
print(is_integer('199'))

# TEST_2:
print(is_integer('-43'))

# TEST_3:
print(is_integer('5f'))

# TEST_4:
print(is_integer('5.0'))

# TEST_5:
print(is_integer('1.1'))

# TEST_6:
print(is_integer('1-1'))

# TEST_7:
print(is_integer('58593485349483423'))

# TEST_8:
print(is_integer('585934853t49483423'))

# TEST_9:
print(is_integer('1-2-3'))

# TEST_10:
print(is_integer('5-'))

# TEST_11:
print(is_integer('-p'))

# TEST_12:
print(is_integer('1111111111'))

# TEST_13:
print(is_integer('--9'))

# TEST_14:
print(is_integer('-0001'))
print(is_integer('0001'))