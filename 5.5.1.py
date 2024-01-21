'''
Класс FoodInfo
Реализуйте класс FoodInfo, описывающий пищевую ценность продуктов. При создании экземпляра класс должен принимать три аргумента в следующем порядке:

proteins — количество белков в граммах
fats — количество жиров в граммах
carbohydrates — количество углеводов в граммах
Экземпляр класса FoodInfo должен иметь три атрибута:

proteins — количество белков в граммах
fats — количество жиров в граммах
carbohydrates — количество углеводов в граммах
И следующее формальное строковое представление:

FoodInfo(<количество белков>, <количество жиров>, <количество углеводов>)
Также экземпляры класса FoodInfo должны поддерживать между собой операцию сложения с помощью оператора +, результатом которой должен являться новый экземпляр класса FoodInfo с суммарным количеством белков, жиров и углеводов исходных экземпляров.

Наконец, экземпляр класса FoodInfo должен поддерживать операции умножения, деления и деления нацело на число n с помощью операторов *, / и // соответственно:

результатом умножения должен являться новый экземпляр класса FoodInfo, количество белков, жиров и углеводов которого умножены на n
результатом деления должен являться новый экземпляр класса FoodInfo, количество белков, жиров и углеводов которого поделены на n
результатом деления нацело должен являться новый экземпляр класса FoodInfo, количество белков, жиров и углеводов которого поделены нацело на n
Примечание 1. Числами будем считать экземпляры классов int и float. Также будем гарантировать, что экземпляр класса FoodInfo всегда делится на ненулевое число.

Примечание 2. Если объект, с которым выполняется арифметическая операция, некорректен, метод, реализующий эту операцию, должен вернуть константу NotImplemented.

Примечание 3. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 4. Никаких ограничений касательно реализации класса FoodInfo нет, она может быть произвольной.
'''

class FoodInfo:
    def __init__ (self, proteins, fats, carbohydrates):
        self.proteins = proteins
        self.fats = fats
        self.carbohydrates =carbohydrates
        
    def __repr__(self):
        return f'FoodInfo({self.proteins}, {self.fats}, {self.carbohydrates})'
        
    def __add__(self,other):
        if isinstance(other,FoodInfo):
            return FoodInfo(self.proteins+other.proteins, self.fats+other.fats, self.carbohydrates+other.carbohydrates)
        else:
            return NotImplemented
        
    def __mul__(self,n):
        if isinstance(n,(int,float)):
            return FoodInfo(self.proteins*n, self.fats*n, self.carbohydrates*n)
        else:
            return NotImplemented        

    def __truediv__(self,n):
        if isinstance(n,(int,float)):
            return FoodInfo(self.proteins/n, self.fats/n, self.carbohydrates/n) 
        else:
            return NotImplemented            
    
    def __floordiv__(self,n):
        if isinstance(n,(int,float)):
            return FoodInfo(self.proteins//n, self.fats//n, self.carbohydrates//n) 
        else:
            return NotImplemented
        
        
pfc = [(751.26, 778.77, 947.51), (597.41, 508.5, 532.96), (800.55, 617.5, 525.14), (741.99, 785.53, 664.71),
       (525.69, 892.41, 541.41), (888.8, 802.56, 868.78), (609.65, 855.43, 949.44), (705.25, 592.28, 738.72),
       (514.88, 617.22, 557.5), (948.62, 938.7, 817.17), (783.98, 628.32, 686.38), (894.9, 815.81, 715.19),
       (586.79, 826.68, 637.5), (670.53, 683.69, 841.56), (583.9, 607.34, 853.35), (954.67, 950.76, 822.19),
       (718.94, 658.12, 537.2), (556.53, 686.17, 622.61), (699.8, 872.49, 908.3), (622.3, 920.97, 801.17)]

FoodInfo.__round__ = lambda instance: FoodInfo(
    round(instance.proteins, 2),
    round(instance.fats, 2),
    round(instance.carbohydrates, 2)
)

food1 = FoodInfo(1000, 2000, 3000)
for p, f, c in pfc:
    food2 = FoodInfo(p, f, c)
    add_food = food1 + food2
    mul_food = food1 * p
    truediv_food = food1 // c
    print(round(add_food), round(mul_food), round(truediv_food))