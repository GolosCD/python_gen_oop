class MyClass:
    def __init__(self, a):
        self._a = a

    def __getattribute__(self, attr):
        if attr == 'a':
            return 8
        else:
            return object.__getattribute__(self, attr)
        
        
        
test = MyClass(5)


print(test.a)