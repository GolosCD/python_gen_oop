'''
Класс Temperature
Реализуйте класс Temperature, описывающий температуру в градусах по шкале Цельсия. При создании экземпляра класс должен принимать один аргумент:

temperature — температура в градусах по шкале Цельсия
Класс Temperature должен иметь один метод экземпляра:

to_fahrenheit() — метод, возвращающий температуру по шкале Фаренгейта
Класс Temperature должен иметь один метод класса:

from_fahrenheit() — метод, принимающий в качестве аргумента температуру по шкале Фаренгейта и возвращающий экземпляр класса Temperature, созданный на основе переданной температуры
Экземпляр класса Temperature должен иметь следующее неформальное строковое представление:

<температура в градусах по шкале Цельсия с округлением до двух знаков после запятой>°C
Также экземпляр класса Temperature должен поддерживать приведение к типам bool, int и float:

при приведении к типу bool значением экземпляра класса Temperature должно являться значение True, если его температура выше нуля, или False в противном случае
при приведении к типу int значением экземпляра класса Temperature должна являться его температура в виде целого числа с отброшенной дробной частью
при приведении к типу float значением экземпляра класса Temperature должна являться его температура в виде вещественного числа
Примечание 1. Перевести температуру из шкалы Фаренгейта в шкалу Цельсия позволяет формула:
�
�
=
5
9
(
�
�
–
32
)
t 
C
​
 = 
9
5
​
 (t 
F
​
 –32)
где 
�
�
t 
C
​
  — температура в градусах по шкале Цельсия, 
�
�
t 
F
​
  — температура в градусах по шкале Фаренгейта.

Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 3. Никаких ограничений касательно реализации класса Temperature нет, она может быть произвольной.
'''


class Temperature:
    def __init__ (self,temperature):
        self.temperature = temperature
        
    def  to_fahrenheit(self):
        return 9/5*self.temperature +32
    
    @classmethod
    def from_fahrenheit(cls,temperature):
        fahra = 5/9 *(temperature-32)
        return cls(fahra)
        
    def __bool__(self):
        return self.temperature>0
    
    def __int__(self):
        return int(self.temperature)
        
    def __float__(self):
        return float(self.temperature)
        
    def __str__(self):
        return f'{round(self.temperature,2)} u"\N{DEGREE SIGN}"C'


Sample Input 1:

t = Temperature(5.5)

print(t)
print(int(t))
print(float(t))
print(t.to_fahrenheit())
Sample Output 1:

5.5°C
5
5.5
41.9
Sample Input 2:

t1 = Temperature(1)
t2 = Temperature(0)
t3 = Temperature(-1)

print(bool(t1))
print(bool(t2))
print(bool(t3))
Sample Output 2:

True
False
False
Sample Input 3:

t = Temperature.from_fahrenheit(41)

print(t)
print(int(t))
print(float(t))
print(t.to_fahrenheit())
Sample Output 3:

5.0°C
5
5.0
41.0
 