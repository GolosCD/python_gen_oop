'''
Класс NonNegativeObject
Реализуйте класс NonNegativeObject. При создании экземпляра класс должен принимать произвольное количество именованных аргументов. Все передаваемые аргументы должны устанавливаться создаваемому экземпляру в качестве атрибутов, причем если значением атрибута является отрицательное число, оно должно быть взято с противоположным знаком.

Примечание 1. Числами будем считать экземпляры классов int и float.

Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 3. Никаких ограничений касательно реализации класса NonNegativeObject нет, она может быть произвольной.
'''

class NonNegativeObject:
    def __init__(self,**kwargs):
        for key,value in kwargs.items():
            if isinstance(value,(int,float)):
                object.__setattr__(self,key,abs(value))
            else:
                object.__setattr__(self,key,value)
        
    # def __setattr__(self,key,value):
        # object.__setattr__(self,key,abs(value))
        
        
point = NonNegativeObject(x=1, y=-2, z=0, color='black')

print(point.x)
print(point.y)
print(point.z)
print(point.color)        