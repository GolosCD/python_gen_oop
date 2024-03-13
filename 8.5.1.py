from functools import wraps

def track_instances(cls):
    old__init__ = cls.__init__
    if not hasattr(cls,'instances'):
        cls.instances = []
        
    
    @wraps(old__init__)
    def new_init(self,*args,**kwargs):
        old__init__(self,*args,**kwargs)
        cls.instances.append(self)
        
    cls.__init__ =  new_init
    
    return cls
        
@track_instances
class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Person({self.name!r})'


obj1 = Person('object 1')
obj2 = Person('object 2')

print(Person.instances)        