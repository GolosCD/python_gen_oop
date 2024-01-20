'''
Класс ColoredPoint
Реализуйте класс ColoredPoint, описывающий цветную точку на плоскости. При создании экземпляра класс должен принимать три аргумента в следующем порядке:

x — координата точки по оси 
�
x
y — координата точки по оси 
�
y
color — цвет в формате RGB, представленный кортежем из трех целых чисел в диапазоне [0; 255], по умолчанию имеет значение (0, 0, 0)
Экземпляр класса ColoredPoint должен иметь три атрибута:

x — координата точки по оси 
�
x
y — координата точки по оси 
�
y
color — цвет в формате RGB, представленный кортежем из трех целых чисел от 0 до 255
Также экземпляр класса ColoredPoint должен иметь следующее формальное строковое представление:

ColoredPoint(<координата x>, <координата y>, <цвет точки в виде трехэлементного кортежа>)
И следующее неформальное строковое представление:

(<координата x>, <координата y>)
Наконец, экземпляр класса ColoredPoint должен поддерживать унарные операторы +, - и ~:

результатом унарного + должен являться новый экземпляр класса ColoredPoint c исходными координатами и цветом
результатом унарного - должен являться новый экземпляр класса ColoredPoint c координатами, умноженными на минус единицу, и исходным цветом
результатом унарного ~ должен являться новый экземпляр класса ColoredPoint c координатами, переставленными местами, и инвертированным цветом: значение каждой компоненты цвета отнимается от 255
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса ColoredPoint нет, она может быть произвольной.
'''

class ColoredPoint:
    def __init__(self,x,y, color = (0,0,0)):
        self.x = x
        self.y = y
        self.color = color
        
    def __repr__(self):
        return f'ColoredPoint({self.x}, {self.y}, {self.color})'

    def __str__(self):
        return f'({self.x}, {self.y})'
        
        
    def __pos__(self):
        return ColoredPoint(self.x,self.y,self.color)
        
    def __neg__(self):
        return ColoredPoint(self.x*-1,self.y*-1,self.color) 
        
    def __invert__(self):
        invert_color = tuple(map(lambda x: 255-x,self.color))
        return ColoredPoint(self.y,self.x,invert_color)
        

# INPUT DATA:

# TEST_1:
point = ColoredPoint(2, -3)

print(+point)
print(-point)
print(~point)

# TEST_2:
point1 = ColoredPoint(2, -3)
point2 = ColoredPoint(10, 20, (34, 45, 67))

print(point1.color)
print(point2.color)

# TEST_3:
point1 = ColoredPoint(1, 2, (100, 150, 200))
point2 = ~point1

print(repr(point1))
print(repr(point2))

# TEST_4:
points = [(-63, 49, (35, 0, 105)), (-3, 88, (98, 139, 119)), (-6, -65, (161, 21, 201)), (-37, -41, (102, 50, 8)),
          (-52, 73, (96, 60, 239)), (-3, -99, (195, 52, 4)), (72, -86, (125, 72, 45)), (-53, 12, (14, 4, 47)),
          (10, -54, (36, 226, 195)), (11, -71, (221, 167, 90)), (48, -50, (195, 45, 128)), (21, 69, (253, 118, 111)),
          (98, -74, (186, 175, 142)), (69, -71, (138, 38, 30)), (11, 23, (248, 11, 103)), (88, 1, (167, 91, 151)),
          (81, -71, (85, 54, 50)), (-48, 14, (69, 81, 239)), (52, -34, (133, 85, 145)), (-67, -15, (11, 216, 25)),
          (-77, 77, (23, 161, 48)), (19, 12, (56, 8, 4)), (38, -84, (13, 112, 78)), (55, -34, (6, 25, 17)),
          (-23, 79, (227, 29, 38)), (-88, -97, (240, 9, 253)), (-67, -68, (74, 64, 57)), (82, -18, (136, 211, 65)),
          (67, -1, (10, 205, 188)), (-58, 51, (247, 74, 84)), (-54, 73, (122, 246, 136)), (-63, -30, (121, 120, 245)),
          (-97, 22, (205, 218, 195)), (-24, 39, (97, 242, 65)), (-66, -58, (218, 39, 119)), (-37, 44, (246, 19, 239)),
          (42, 56, (121, 72, 79)), (89, -82, (114, 197, 173)), (-68, 87, (44, 213, 73)), (-62, 30, (136, 187, 198)),
          (41, -68, (232, 93, 251)), (-98, -73, (201, 3, 62)), (28, -19, (241, 137, 163)), (49, 15, (68, 83, 106)),
          (96, -39, (145, 175, 144)), (-32, -3, (39, 20, 53)), (-81, 40, (202, 17, 173)), (-32, -62, (168, 43, 102)),
          (-3, 37, (91, 46, 50)), (11, 82, (51, 56, 196)), (-6, -72, (104, 240, 161)), (85, -24, (83, 155, 58)),
          (0, -85, (153, 117, 150)), (83, -43, (137, 37, 201)), (64, -8, (237, 14, 134)), (-44, -56, (6, 53, 33)),
          (88, -52, (248, 15, 7)), (38, 39, (131, 14, 120)), (48, 60, (108, 158, 165)), (-31, 37, (230, 194, 77)),
          (87, 11, (205, 168, 144)), (-21, 16, (148, 164, 176)), (59, 100, (20, 130, 50)), (20, 89, (150, 103, 131)),
          (11, -87, (190, 59, 226)), (53, 41, (245, 195, 151)), (71, 63, (155, 93, 119)), (-39, -19, (17, 46, 77)),
          (5, 71, (10, 141, 111)), (83, -42, (151, 159, 92)), (95, 51, (109, 125, 42)), (-51, 94, (144, 247, 194)),
          (53, 67, (109, 123, 210)), (27, 59, (58, 40, 123)), (55, -93, (199, 137, 253)), (79, -90, (142, 100, 80)),
          (-61, 63, (33, 199, 84)), (-58, -63, (138, 0, 183)), (-93, 5, (89, 33, 150)), (26, -72, (39, 216, 201)),
          (-89, 42, (39, 79, 123)), (89, 13, (57, 56, 195)), (-66, -87, (64, 14, 51)), (81, -3, (114, 136, 159)),
          (-32, 72, (5, 174, 95)), (-93, -54, (183, 129, 20)), (-100, -32, (33, 254, 94)), (-43, -11, (85, 242, 110)),
          (-89, 79, (232, 240, 236)), (9, 62, (49, 88, 87)), (71, 91, (3, 130, 67)), (-35, -84, (162, 158, 30)),
          (18, 28, (132, 243, 201)), (-54, 61, (128, 231, 135)), (-24, 41, (248, 51, 10)), (-14, -7, (94, 244, 47)),
          (-84, 90, (141, 142, 136)), (13, -28, (205, 26, 65)), (-63, -15, (159, 102, 211)), (-54, -2, (34, 118, 233))]
colored_points = [ColoredPoint(x, y, color) for x, y, color in points]

for point in colored_points:
    print(f'{+point}; {-point}; {~point}; {point.color}')

# TEST_5:
point = ColoredPoint(0, 0, (0, 0, 0))

print(f'{+point}; {-point}; {~point}')
print(point.color)