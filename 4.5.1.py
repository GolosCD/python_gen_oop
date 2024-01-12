'''
Класс Rectangle
Реализуйте класс Rectangle, описывающий прямоугольник. 
При создании экземпляра класс должен принимать два аргумента в следующем порядке:

length — длина прямоугольника
width — ширина прямоугольника
Экземпляр класса Rectangle должен иметь два атрибута:

length — длина прямоугольника
width — ширина прямоугольника
Класс Rectangle должен иметь два свойства:

perimeter — свойство, доступное только для чтения, возвращающее периметр прямоугольника
area — свойство, доступное только для чтения, возвращающее площадь прямоугольника
Примечание 1. При изменении сторон прямоугольника должны изменяться его периметр и площадь.

Примечание 2. Дополнительная проверка данных на корректность не требуется. 
Гарантируется, что реализованный класс используется только с корректными данными.
'''
class Rectangle:
    def __init__(self,length,width):
        self._length = length
        self._width = width
        
    def get_length(self):
        return self._length
        
    def set_length(self,length):
        self._length = length
        
    def get_width(self):
        return self._width
        
    def set_width(self,width):
        self._width = width
        
    def get_perimeter(self):
        return 2*(self.length+self.width)
    
    def get_area (self):
        return self.length*self.width
        
    length = property(fget = get_length,fset = set_length)
    width = property(fget = get_width,fset = set_width)
    perimeter = property(fget = get_perimeter)
    area = property(fget = get_area)
    
    
rectangle = Rectangle(4, 5)

rectangle.length = 2
rectangle.width = 3
print(rectangle.length)
print(rectangle.width)
print(rectangle.perimeter)
print(rectangle.area)    
    
    
    
    