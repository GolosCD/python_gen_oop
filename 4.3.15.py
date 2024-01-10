'''
Класс Knight ♞
Реализуйте класс Knight, описывающий шахматного коня. При создании экземпляра класс должен принимать три аргумента в следующем порядке:

horizontal — координата коня по горизонтальной оси, представленная латинской буквой от a до h
vertical — координата коня по вертикальной оси, представленная целым числом от 1 до 8 включительно
color — цвет коня (black или white)
Экземпляр класса Knight должен иметь три атрибута:

horizontal — координата коня на шахматной доске по горизонтальной оси
vertical — координата коня на шахматной доске по вертикальной оси
color — цвет коня
Класс Knight должен иметь четыре метода экземпляра:

get_char() — метод, возвращающий символ N

can_move() — метод, принимающий в качестве аргументов координаты клетки по горизонтальной и по 
вертикальной осям и возвращающий True, если конь может переместиться на клетку с данными координатами, или False в противном случае

move_to() — метод, принимающий в качестве аргументов координаты клетки по горизонтальной и по 
вертикальной осям и заменяющий текущие координаты коня на переданные. Если конь из текущей клетки 
не может переместиться на клетку с указанными координатами, его координаты должны остаться неизменными

draw_board() — метод, печатающий шахматное поле, отмечающий на этом поле коня и клетки, на которые 
может переместиться конь. Пустые клетки должны быть отображены символом ., конь — символом N, клетки, на которые может переместиться конь, — символом *
'''
class Knight:
    def __init__(self,horizontal,vertical,color):
        self.horizontal = horizontal
        self.vertical = vertical
        self.color = color
        self.x1 = ord(horizontal) - 97
        self.y1 = 8 - vertical
        
    def get_char(self):
        return 'N'
        
    def can_move(self,horizontal_new,vertical_new):
        x2 = ord(horizontal_new) - 97
        y2 = 8-vertical_new

        if abs(self.x1-x2)*abs(self.y1-y2)==2:
            return True
        else:
            return False

    def move_to(self,horizontal_new,vertical_new):      
                
        if self.can_move(horizontal_new,vertical_new):
            self.x1=ord(horizontal_new) - 97
            self.y1=8 - vertical_new
            self.horizontal = horizontal_new
            self.vertical = vertical_new

    def draw_board(self):
        pole = [['.' for i in range(8)] for _ in range(8)]
        pole[self.y1][self.x1] = self.get_char()
        
        for i in range(8):
            for j in range(8):
                if abs(self.y1 - i) * abs(self.x1 - j) == 2:
                    pole[i][j] = '*'
                             
        for row in pole:
            print(''.join(row))



knight = Knight('e', 5, 'black')

knight.draw_board()
print(knight.can_move('d', 3))
knight.move_to('d', 3)
print()
knight.draw_board()   
'''
# TEST_4:
........
...*.*..
..*...*.
....N...
..*...*.
...*.*..
........
........

........
........
........
..*.*...
.*...*..
...N....
.*...*..
..*.*...
'''
