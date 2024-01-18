class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width                           
        
    def __repr__(self):
        return f'Rectangle({self.length}, {self.width})'    
        
        
rectangle = Rectangle(1, 2)

print(str(rectangle))
print(repr(rectangle))        
        