class ColoredPoint:
    def __init__(self,x,y,color):
        self._x = x
        self._y = y
        self._color = color
        
    def __repr__(self):
        return f"ColoredPoint({self.x}, {self.y}, '{self.color}')"
        
    def __eq__(self,other):
        if isinstance(other,ColoredPoint):
            return self.x  == other.x and self.y == other.y and self.color==other.color
        else:
            return NotImplemented
        
    def __hash__(self):
        return hash(self._fields)
        
    @property    
    def _fields(self):
        return self.x,self.y,self.color
        
    @property    
    def x(self):
        return self._x
    
    @property    
    def y(self):
        return self._y
        
    @property    
    def color(self):
        return self._color      