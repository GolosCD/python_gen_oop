'''
Класс QuadraticPolynomial
Квадратный трехчлен – это многочлен вида 
�
�
2
+
�
�
+
�
ax 
2
 +bx+c, где 
�
≠
0
a

=0. Например:
�
2
+
1
�
2
−
5
�
+
6
x 
2
 +1
x 
2
 −5x+6
Значение переменной 
�
x, при котором квадратный трехчлен обращается в ноль, называют его корнем. Квадратный трехчлен может иметь один корень, два корня или вовсе не иметь корней. Корни квадратного трехчлена, если они существуют, находятся по формуле:
�
1
,
2
=
−
�
±
�
2
−
4
�
�
2
�
x 
1,2
​
 = 
2a
−b± 
b 
2
 −4ac
​
 
​
 
Реализуйте класс QuadraticPolynomial, описывающий квадратный трехчлен. При создании экземпляра класс должен принимать три аргумента в следующем порядке:

a — коэффициент 
�
a квадратного трехчлена
b — коэффициент 
�
b квадратного трехчлена
c — коэффициент 
�
c квадратного трехчлена
Экземпляр класса QuadraticPolynomial должен иметь три атрибута:

a — коэффициент 
�
a квадратного трехчлена
b — коэффициент 
�
b квадратного трехчлена
c — коэффициент 
�
c квадратного трехчлена
Класс QuadraticPolynomial должен иметь четыре свойства:

x1 — свойство, доступное только для чтения, возвращающее корень квадратного трехчлена, вычисленный по формуле:
�
1
=
−
�
−
�
2
−
4
�
�
2
�
x 
1
​
 = 
2a
−b− 
b 
2
 −4ac
​
 
​
 
Если квадратный трехчлен не имеет корней (
�
2
−
4
�
�
<
0
b 
2
 −4ac<0), значением свойства должно быть значение None
x2 — свойство, доступное только для чтения, возвращающее корень квадратного трехчлена, вычисленный по формуле:
�
2
=
−
�
+
�
2
−
4
�
�
2
�
x 
2
​
 = 
2a
−b+ 
b 
2
 −4ac
​
 
​
 
Если квадратный трехчлен не имеет корней (
�
2
−
4
�
�
<
0
b 
2
 −4ac<0), значением свойства должно быть значение None
view — свойство, доступное только для чтения, возвращающее строку вида:
ax^2 + bx + c
где a, b и с представляют коэффициенты квадратного трехчлена

coefficients — свойство, доступное для чтения и записи, возвращающее кортеж вида:
(a, b, c)
где a, b и с представляют коэффициенты квадратного трехчлена
Примечание 1. Если квадратный трехчлен имеет лишь один корень, значения свойств x1 и x2 должны совпадать.

Примечание 2. При изменении коэффициентов квадратного трехчлена через соответствующие атрибуты или свойство coefficients значения свойств x1, x2, view и coefficients также должны изменяться.

Примечание 3. Если какие-либо коэффициенты квадратного трехчлена равны нулю, они по-прежнему должны присутствовать в строке, возвращаемой свойством view, дополнительно их убирать не нужно.

Примечание 4. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 5. Никаких ограничений касательно реализации класса QuadraticPolynomial нет, она может быть произвольной.
'''

from math import pow,sqrt

class QuadraticPolynomial:
     def __init__ (self,a,b,c):
         self.a = a
         self.b = b
         self.c = c
         self.d = (pow(self.b,2)-4*self.a*self.c)<0
         
     @property
     def x1(self):
         if self.d:
             return None
         else:
             x1 = (-self.b-sqrt(pow(self.b,2)-4*self.a*self.c))/(2*self.a)
             return x1
             
     @property
     def x2(self):
         if self.d:
             return None
         else:
             x2 = (-self.b+sqrt(pow(self.b,2)-4*self.a*self.c))/(2*self.a)
             return x2
             
     @property
     def view(self):
         return f'{self.a}x^2 {"+" if self.b>=0 else "-"} {abs(self.b)}x {"+" if self.c>=0 else "-"} {abs(self.c)}'

     @property
     def coefficients (self):
         return (self.a,self.b,self.c)

     @coefficients.setter
     def coefficients (self,*args):
         self.a,self.b,self.c = args[0]
         self.d = (pow(self.b,2)-4*self.a*self.c)<0


# INPUT DATA:

# TEST_1:
polynom = QuadraticPolynomial(1, 2, -3)

print(polynom.a)
print(polynom.b)
print(polynom.c)

# TEST_2:
polynom = QuadraticPolynomial(1, 2, -3)

print(polynom.x1)
print(polynom.x2)

# TEST_3:
polynom = QuadraticPolynomial(1, 2, -3)

print(polynom.view)
print(polynom.coefficients)

# TEST_4:
polynom = QuadraticPolynomial(1, 2, -3)

polynom.coefficients = (1, -5, 6)
print(polynom.x1)
print(polynom.x2)
print(polynom.view)

# TEST_5:
polynom = QuadraticPolynomial(1, 2, -3)

polynom.coefficients = (1, -5, 0)
print(polynom.x1)
print(polynom.x2)
print(polynom.view)

# TEST_6:
polynom = QuadraticPolynomial(1, 2, -3)

polynom.coefficients = (1, 0, -9)
print(polynom.x1)
print(polynom.x2)
print(polynom.view)

# TEST_7:
polynom = QuadraticPolynomial(1, 2, -3)

polynom.coefficients = (5, 0, 0)
print(polynom.x1)
print(polynom.x2)
print(polynom.view)

# TEST_8:
polynom = QuadraticPolynomial(500, -601, 101)

print(polynom.a, polynom.b, polynom.c)
print(polynom.x1)
print(polynom.x2)
print(polynom.coefficients)
print(polynom.view)

print()

polynom.coefficients = (-1000, 1202, -202)
print(polynom.a, polynom.b, polynom.c)
print(polynom.x1)
print(polynom.x2)
print(polynom.coefficients)
print(polynom.view)

# TEST_9:
polynom = QuadraticPolynomial(1, 2, -3)

polynom.coefficients = (5, 3, 1)
print(polynom.x1)
print(polynom.x2)
print(polynom.view)