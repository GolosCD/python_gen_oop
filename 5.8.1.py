'''
Класс Item
Требовалось реализовать класс Item, описывающий предмет. При создании экземпляра класс должен был принимать три аргумента в следующем порядке:

name — название предмета
price — цена предмета в рублях
quantity — количество предметов
Предполагалось, что при обращении к атрибуту name экземпляра класса Item будет возвращаться его название с заглавной буквы, а при обращении к атрибуту total — произведение цены предмета на его количество.

Программист торопился и решил задачу неправильно. Дополните приведенный ниже код и реализуйте правильный класс Item.

Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
'''

class Item:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price 
        self.quantity=quantity
        
    def __getattribute__(self,attr):
        if attr == 'name':  
            name_ret = object.__getattribute__(self,attr)
            return name_ret.title()
        elif attr == 'total':
            p = self.__dict__['price']
            q = self.__dict__['quantity']
            return p*q
        else:
            return object.__getattribute__(self,attr)
            
            
course = Item('pygen', 3900, 2)

print(course.name)
print(course.price)
print(course.quantity)
print(course.total)            