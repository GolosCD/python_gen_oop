class LowerString(str):
    def __new__(cls,obj=''):
        inst = super().__new__(cls, obj)
        return inst.lower()
    
    def __init__(self,obj):
        self.obj  = obj
    
    def __str__(self):
        return f'{self.obj}'
        
    def __type__(self):
        if self.obj =='':
            return  type(self)
        return type(self.obj)    
         
lowerstring = LowerString()
print(type(lowerstring))