'''
Класс ReversibleString
Реализуйте класс ReversibleString, описывающий строку. При создании экземпляра класс должен принимать один аргумент:

string — значение строки
Экземпляр класса ReversibleString должен иметь следующее неформальное строковое представление:

<значение строки>
Также экземпляр класса ReversibleString должен поддерживать унарный оператор -, результатом которого должен являться новый экземпляр класса ReversibleString со значением строки в обратном порядке.

Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса ReversibleString нет, она может быть произвольной.
'''

class ReversibleString:
    def __init__(self,string):
        self.string = string
        
    def __str__(self):
        return self.string
        
    def __neg__(self):
        return ReversibleString(self.string[::-1])
        
        
string = ReversibleString('beegeek')

print(-string)
print(type(-string))        