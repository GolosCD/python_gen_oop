'''
Класс Reloopable
Реализуйте класс Reloopable. При создании экземпляра класс должен принимать один аргумент:

file — открытый на чтение файловый объект
Экземпляр класса Reloopable должен являться контекстным менеджером, который позволяет многократно итерироваться по файловому объекту file внутри блока with. Также контекстный менеджер должен закрывать используемый им файловый объект после выполнения кода внутри блока with.

Примечание 1. Наглядные примеры использования класса Reloopable продемонстрированы в тестовых данных.

Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 3. Класс Reloopable должен удовлетворять протоколу контекстного менеджера, то есть иметь методы __enter__() и __exit__(). Реализация же протокола может быть произвольной.
'''

class Reloopable:
    def __init__(self,file):
        self.file = file
    
    def __enter__(self):
        # return [line.strip('\n') for line in self.file.readlines()]
        return self.file.readlines()
        
    def __exit__(self, exc_type,exc_value,traceback):
        self.file.close()
        
with open('file.txt', 'w') as file:
    pass
    
file = open('file.txt')
print(file.closed)

with Reloopable(file) as reloopable:
    pass

print(file.closed)      