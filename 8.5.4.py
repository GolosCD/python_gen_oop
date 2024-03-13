'''
Декоратор @singleton
Реализуйте декоратор @singleton для декорирования класса. Декоратор должен превращать декорируемый класс в синглтон, то есть в класс, при первом вызове создающий единственный свой экземпляр и при последующих вызовах возвращающий его же.
'''

def singleton(cls):
    old_new = cls.__new__
    cls._inst = None
    
    def new_cls(self, *args, **kwargs): 
    
        if cls._inst is None:
            cls._inst = old_new(cls)
            
        return cls._inst
    cls.__new__ = new_cls
    return cls         
    
# INPUT DATA:

# TEST_1:
@singleton
class MyClass:
    pass
    
obj1 = MyClass()
obj2 = MyClass()

print(obj1 is obj2)

# TEST_2:
@singleton
class MyClass:
    pass


instances = [MyClass() for _ in range(100)]
obj = MyClass()
print(all(instance is obj for instance in instances))

# TEST_3:
@singleton
class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Person({self.name!r})'


instances = [Person('John Doe') for _ in range(1000)]
person = Person('Doe John')
print(person)
print(instances[389])
print(all(instance is person for instance in instances))