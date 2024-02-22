'''
Классы Triangle и EquilateralTriangle
Реализуйте класс Triangle, описывающий треугольник. При создании экземпляра класс должен принимать три аргумента в следующем порядке:

a — длина стороны треугольника
b — длина стороны треугольника
c — длина стороны треугольника
Класс Triangle должен иметь один метод экземпляра:

perimeter() — метод, возвращающий периметр треугольника
Также реализуйте класс EquilateralTriangle, наследника класса Triangle, описывающий равносторонний треугольник. При создании экземпляра класс должен принимать один аргумент:

side — длина стороны треугольника
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации классов нет, она может быть произвольной.
'''

class Triangle:
    
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def  perimeter(self):
        return self.a+self.b+self.c
        
        
class EquilateralTriangle(Triangle):
    def __init__(self,side):
        super().__init__(side,side,side)
        
        
triangle1 = Triangle(3, 4, 5)
triangle2 = EquilateralTriangle(3)

print(triangle1.perimeter())
print(triangle2.perimeter())        