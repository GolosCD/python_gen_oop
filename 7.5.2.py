'''
Классы ChessPiece, King и Knight
1. Реализуйте абстрактный класс ChessPiece, описывающий шахматную фигуру. Инициализатор класса должен принимать два аргумента в следующем порядке:

horizontal — координата фигуры по горизонтали, представленная латинской буквой от a до h
vertical — координата фигуры по вертикали, представленная целым числом от 1 до 8 включительно
Класс ChessPiece должен иметь один метод экземпляра:

can_move() — пустой абстрактный метод
2. Также реализуйте класс King, наследника класса ChessPiece, описывающий шахматного короля. Процесс создания экземпляра класса King должен совпадать с процессом создания экземпляра класса ChessPiece.

Класс King должен иметь один метод экземпляра:

can_move() — метод, принимающий в качестве аргументов шахматные координаты по горизонтали и вертикали и возвращающий True, если фигура может переместиться по указанным координатам, или False в противном случае
Экземпляр класса King  должен иметь два атрибута:

horizontal — координата фигуры по горизонтали, представленная латинской буквой от a до h
vertical — координата фигуры по вертикали, представленная целым числом от 1 до 8 включительно
3. Наконец, реализуйте класс Knight, наследника класса ChessPiece, описывающий шахматного коня. Процесс создания экземпляра класса Knight должен совпадать с процессом создания экземпляра класса ChessPiece.

Класс Knight должен иметь один метод экземпляра:

can_move() — переопределенный родительский метод, принимающий в качестве аргументов координаты по горизонтали и вертикали и возвращающий True, если фигура может переместиться по указанным координатам, и False в противном случае
Экземпляр класса Knight  должен иметь два атрибута:

horizontal — координата фигуры по горизонтали, представленная латинской буквой от a до h
vertical — координата фигуры по вертикали, представленная целым числом от 1 до 8 включительно
'''

# from abc import ABC, abstractmethod
# from typing import Literal

# Horizontal =Literal['a','b','c','d','e','f','g','h']
# Vertical = Literal[1,2,3,4,5,6,7,8]


# class ChessPiece:
    
    # def __init__(self, horizontal: Horizontal, vertical: Vertical,/):
        # self.horizontal = horizontal
        # self.vertical = vertical
        # self.data = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}
        
    # @abstractmethod    
    # def can_move(self,horizontal: Horizontal, vertical: Vertical,/)->bool: pass
        
# class King(ChessPiece):
    # def can_move(self,lin2: Horizontal, col2: Vertical,/):
        # col1 = self.vertical
        # lin1 = self.data.get(self.horizontal)
        # lin2 = self.data.get(lin2)
        # if col1-1<=col2<=col1+1 and lin1-1<=lin2<=lin1+1:
            # return True
        # else:
            # return False
            
# class Knight(ChessPiece):
    # def can_move(self,dcol: Horizontal, bline: Vertical,/):
        # aline = self.vertical
        # bcol = self.data.get(self.horizontal)
        # dcol = self.data.get(dcol)
        # if aline==bline and (dcol>bcol or dcol<bcol):
            # return True
        # elif dcol==bcol and (bline>aline or bline<aline):
            # return True
        # else:
            # return False           
                
        
# class King(ChessPiece):
    # def can_move(self,horizontal: Horizontal, vertical: Vertical,/):
        # if self.vertical-1<=vertical<=self.vertical+1 and self.data.get(self.horizontal)-1<=self.data.get(horizontal)<=self.data.get(self.horizontal)+1:
            # return True
        # else:
            # return False
            
# class King(ChessPiece):
    # def can_move(self, new_horizontal, new_vertical):
        # if abs(ord(new_horizontal) - ord(self.horizontal)) <= 1 and abs(new_vertical - self.vertical) <= 1:
            # return True
        # else:
            # return False            
        
# class Knight(ChessPiece):
    # def can_move(self, new_horizontal, new_vertical):
        # if abs(ord(new_horizontal) - ord(self.horizontal)) == 2 and abs(new_vertical - self.vertical) == 1:
            # return True
        # elif abs(ord(new_horizontal) - ord(self.horizontal)) == 1 and abs(new_vertical - self.vertical) == 2:
            # return True
        # else:
            # return False        
        
        
# class Knight  (ChessPiece):
    # def can_move(self,horizontal: Horizontal, vertical: Vertical,/):
        # if self.data.get(self.horizontal)==self.data.get(horizontal) and (self.vertical>vertical or self.vertical<vertical):
            # return True
        # elif self.vertical==vertical and (self.data.get(horizontal)>self.data.get(self.horizontal) or self.data.get(horizontal)<self.data.get(self.horizontal)):
            # return True
        # else:
            # return False
            
from abc import ABC, abstractmethod


class ChessPiece(ABC):
    def __init__(self, horizontal, vertical):
        self.horizontal = horizontal
        self.vertical = vertical

    @abstractmethod
    def can_move(self, horizontal, vertical):
        return


class King(ChessPiece):

    def can_move(self, horizontal, vertical):
        if self.horizontal != horizontal and self.vertical != vertical:
            return abs(ord(self.horizontal) - ord(horizontal)) + abs(self.vertical - vertical) == 2
        return abs(ord(self.horizontal) - ord(horizontal)) + abs(self.vertical - vertical) == 1


class Knight(ChessPiece):

    def can_move(self, horizontal, vertical):
        return abs(ord(self.horizontal) - ord(horizontal)) * abs(self.vertical - vertical) == 2
            


# INPUT DATA:

# TEST_1:
king = King('b', 2)

print(king.can_move('c', 3))
print(king.can_move('a', 1))
print(king.can_move('f', 7))

# TEST_2:
knight = Knight('c', 3)

print(knight.can_move('e', 5))
print(knight.can_move('e', 4))

# TEST_3:
king = King('e', 3)

print(king.can_move('e', 3))
print(king.can_move('e', 4))
print(king.can_move('b', 1))

# TEST_4:
knight = Knight('h', 8)

print(knight.can_move('h', 8))
print(knight.can_move('a', 6))
print(knight.can_move('a', 1))
print(knight.can_move('g', 6))

# TEST_5:
knight = Knight('a', 1)

for horizontal in 'abcdefg':
    for vertical in range(1, 9):
        print(f'{horizontal}{vertical}', knight.can_move(horizontal, vertical))

# TEST_6:
king = King('a', 1)

for horizontal in 'abcdefg':
    for vertical in range(1, 9):
        print(f'{horizontal}{vertical}', king.can_move(horizontal, vertical))

# TEST_7:
kings = [King(h, v) for h in 'abcdefgh' for v in range(1, 9)]

for king in kings:
    print('*' * 20)
    for horizontal in 'abcdefgh':
        for vertical in range(1, 9):
            if king.can_move(horizontal, vertical):
                print(f'King({king.horizontal}{king.vertical})', f'{horizontal}{vertical}',
                      king.can_move(horizontal, vertical))

# TEST_8:
knights = [Knight(h, v) for h in 'abcdefgh' for v in range(1, 9)]

for knight in knights:
    print('*' * 20)
    for horizontal in 'abcdefgh':
        for vertical in range(1, 9):
            if knight.can_move(horizontal, vertical):
                print(f'Knight({knight.horizontal}{knight.vertical})', f'{horizontal}{vertical}',
                      knight.can_move(horizontal, vertical))