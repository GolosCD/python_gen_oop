'''
Класс Point
Реализуйте класс данных Point, описывающий точку на координатной плоскости. При создании экземпляра класс должен принимать два аргумента в следующем порядке:

x — координата точки по оси 
x (тип float), по умолчанию имеет значение 0.0
y — координата точки по оси 

y (тип float), по умолчанию имеет значение 0.0
Экземпляр класса Point должен иметь три атрибута:

x — координата точки по оси 

y — координата точки по оси 

quadrant — координатная четверть, к которой принадлежит точка (тип int). Если точка лежит на одной из осей, координатная четверть считается равной 0
Класс Point должен иметь два метода экземпляра:

symmetric_x() — метод, возвращающий новый экземпляр класса Point, представляющий точку, симметричную текущей точке относительно оси 
symmetric_y() — метод, возвращающий новый экземпляр класса Point, представляющий точку, симметричную текущей точке относительно оси 
Экземпляр класса Point должен иметь следующее формальное строковое представление:

Point(x=<координата x>, y=<координата y>, quadrant=<координатная четверть>)
Наконец, экземпляры класса Point должны поддерживать между собой операцию сравнения с помощью операторов == и!=. Две точки считаются равными, если их координаты по обеим осям совпадают.

Примечание 1. Для точки с координатами (x,y) симметричной относительно оси 
x будем считать точку с координатами 
(x,−y), симметричной относительно оси 

y — точку с координатами 
(−x,y).
'''


from dataclasses import dataclass, field

@dataclass
class Point:
    x: float =0.0
    y: float =0.0
    quadrant: int = field(default=None,compare = False)
    
    def __post_init__(self):
        if self.x==0.0 or self.y==0.0:
            self.quadrant = 0
        elif self.x<0.0 and self.y>0.0:
            self.quadrant = 2
        elif self.x>0.0 and self.y>0.0:
            self.quadrant = 1
        elif self.x<0.0 and self.y<0.0:
            self.quadrant=3
        else:
            self.quadrant =4
            
    def symmetric_x(self):
        return Point(self.x,self.y*-1)
        
    def symmetric_y(self):
        return Point(self.x*-1,self.y)    

'''           
# INPUT DATA:

# TEST_1:
point = Point()

print(point)
print(point.x)
print(point.y)
print(point.quadrant)

# TEST_2:
point = Point(1.0, 2.0)

print(point.symmetric_x())
print(point.symmetric_y())

# TEST_3:
point1 = Point(1, 2)
point2 = Point(1, 2)
point3 = Point(3, 4)

print(point1 == point2)
print(point1 == point3)
print(point2 != point3)

# TEST_4:
for x in range(-3, 4):
    for y in range(-3, 4):
        point = Point(x, y)
        print(point)
'''
# TEST_5:
for x in range(-3, 4):
    for y in range(-3, 4):
        point = Point(x, y)
        print(point.symmetric_x())
'''
# TEST_6:
for x in range(-3, 4):
    for y in range(-3, 4):
        point = Point(x, y)
        print(point.symmetric_y())'''