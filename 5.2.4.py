from functools import singledispatchmethod



class IPAddress:
    @singledispatchmethod
    def __init__(self,date):
        self.ipaddress = date
        
    @__init__.register(tuple)
    @__init__.register(list)
    def from_init(self,date):
        self.ipaddress = '.'.join(map(str,date))
        
        
    def __repr__(self):
        return f"IPAddress('{self.ipaddress}')"

    def __str__(self):
        return f'{self.ipaddress}'
        
        
ip = IPAddress('8.8.1.1')

print(str(ip))
print(repr(ip))        