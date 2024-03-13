'''
Декоратор @add_attr_to_class
Словарь атрибутов класса, в отличие от словаря атрибутов экземпляра класса, является объектом типа mappingproxy, а не dict.

Приведенный ниже код:

class MyClass:
    pass


print(type(MyClass.__dict__))
выводит:

<class 'mappingproxy'>
Тип mappingproxy представляет собой упрощенный словарь. От типа dict он отличается меньшим количеством методов, а главное — отсутствием магического метода __setitem__(). Это значит, в объект типа mappingproxy нельзя напрямую добавить новую пару ключ-значение, а также изменить значение имеющегося ключа.

Приведенный ниже код:

class MyClass:
    pass


MyClass.__dict__['__doc__'] = 'docstring'
приводит к возбуждению исключения:

TypeError: 'mappingproxy' object does not support item assignment
Для добавления классу необходимого атрибута можно использовать функцию setattr().

Приведенный ниже код:

class MyClass:
    pass


setattr(MyClass, '__doc__', 'docstring')

print(MyClass.__doc__)
выводит:

docstring
Реализуйте декоратор @add_attr_to_class для декорирования класса. Декоратор должен принимать произвольное количество именованных аргументов и добавлять их декорируемому классу в качестве атрибутов.

Примечание. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input:

@add_attr_to_class(first_attr=1, second_attr=2)
class MyClass:
    pass

print(MyClass.first_attr)
print(MyClass.second_attr)
Sample Output:

1
2
'''

from functools import wraps

def add_attr_to_class(*args,**kwargs):
    def decorator(cls):
        for key in kwargs:
            setattr(cls, key, kwargs.get(key))
        return cls
    return decorator    
        
        
@add_attr_to_class(first_attr=1, second_attr=2)
class MyClass:
    pass

print(MyClass.first_attr)
print(MyClass.second_attr)    