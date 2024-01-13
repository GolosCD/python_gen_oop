'''

'''
class QuadraticPolynomial:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        
    @classmethod
    def from_iterable(cls,seq):
        return cls(*seq)
        
    @classmethod
    def from_str(cls,string):
        a = [float(i) for i in string.split()]
        return cls(*a)
        
polynom = QuadraticPolynomial.from_str('-1.5 4 14.8')

print(polynom.a)
print(polynom.b)
print(polynom.c)
print(polynom.a + polynom.b + polynom.c)