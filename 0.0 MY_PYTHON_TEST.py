class MyClass:
    test = 'Hello world'
    
    def print(self):
        print('__class__.test',__class__.test)
        print('MyClass.test',MyClass.test)
        print('type(self).test',type(self).test)
        print('type(self).test',type(self))
        
        
        
g = MyClass()


g.print()