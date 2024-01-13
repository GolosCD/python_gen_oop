'''
Класс Circle
Реализуйте класс Circle, описывающий круг. При создании экземпляра класс должен принимать один аргумент:

radius — радиус круга
Экземпляр класса Circle должен иметь один атрибут:

radius — радиус круга
Класс Circle должен иметь один метод класса:

from_diameter() — метод, принимающий в качестве аргумента диаметр круга и возвращающий экземпляр класса Circle, созданный на основе переданного диаметра
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
'''
class Circle:
    def __init__(self,radius):
        self.radius = radius
        
        
    @property
    def radius(self):
        return self._radius
        
    @radius.setter
    def radius(self,radius):
        self._radius = radius
        
    @classmethod
    def from_diameter(cls,diametr):
        return cls(diametr/2)
        
        
circle = Circle.from_diameter(10)

print(circle.radius)        
        