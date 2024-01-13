a = 10

class c1:
    @classmethod
    def f(cls):
        cls.a = a
    
    
f = c1()


print(f.a)