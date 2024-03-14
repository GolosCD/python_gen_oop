'''
Декоратор @snake_case
Snake Case — стиль написания составных слов, при котором несколько слов разделяются символом нижнего подчеркивания (_) и не имеют пробелов в записи, причём каждое слово пишется с маленькой буквы. Например, bee_geek и hello_world.

Camel Case — стиль написания составных слов, при котором несколько слов пишутся слитно без пробелов, при этом каждое слово пишется с заглавной буквы. Например, BeeGeek и HelloWorld.

Частным случаем стиля Camel Case является lower Camel Case, когда с заглавной буквы пишутся все слова, кроме первого. Например, beeGeek и helloWorld.

Реализуйте декоратор @snake_case для декорирования класса. Декоратор должен принимать один аргумент:

attrs — булево значение, по умолчанию равняется False
Декоратор должен переименовать все не магические методы в декорируемом классе, меняя их стиль написания c Camel Case и lower Camel Case на Snake Case. Параметр attrs должен определять, будут ли аналогичным образом переименованы атрибуты класса. Если он имеет значение True, стиль написания имен атрибутов класса должен поменяться с Camel Case и lower Camel Case на Snake case, если False — остаться прежним.
'''


import inspect as i

def go_to_snake(atr_name :str) ->str:
    sc_method = ''
    for index,letter in enumerate(atr_name):
        if letter.isupper() and index!=0:
            letter = f'_{letter}'
            sc_method+=letter
        else:
            sc_method+=letter
    if sc_method[:2] =='__':
        return sc_method[1:].lower()
    return sc_method.lower()

def snake_case(attrs = False):
    def decorator(cls):
        # print('class_start: ',*[i for i in dir(cls) if not i.startswith('_')],end = '\n' )
        for old_atr, obj in i.getmembers(cls): # перебор всех методов и атрибутов
        
            if not old_atr.startswith('__'): # отсекаем защищенные методы
                new_metgod = ''
                
                if i.isfunction(obj): # если обьект - это функция, т.е метод, то меняем
                    print('TYT: ',old_atr)
                    new_metgod = go_to_snake(old_atr)
                elif attrs: # если обьект атрибут то меняем только если attrs = True
                    new_metgod = go_to_snake(old_atr)
                else:
                    new_metgod=old_atr
                print('Старое название:>>> '.ljust(30),old_atr.ljust(30), 'Новое название:>>> '.ljust(30),new_metgod.ljust(30))   
                if new_metgod not in cls.__dict__:
                    setattr(cls,new_metgod, getattr(cls,old_atr))
                    delattr(cls,old_atr)
        print('class_end: ',*[i for i in dir(cls) if not i.startswith('_')],end = '\n' )
        return cls
    # print('class_decorator: ',*[i for i in dir(decorator) if not i.startswith('_')],end = '\n' )
    return decorator
                  

'''     
# INPUT DATA:

# TEST_1:
@snake_case()
class MyClass:
    def FirstMethod(self):
        return 1
    
    def superSecondMethod(self):
        return 2

obj = MyClass()

print(obj.__dict__)

print(obj.first_method())
print(obj.super_second_method())

# TEST_2:
@snake_case(attrs=True)
class MyClass:
    FirstAttr = 1
    superSecondAttr = 2

print(MyClass.first_attr)
print(MyClass.super_second_attr)
'''
# TEST_3:
@snake_case()
class MyClass:
    FirstAttr = 1

    def FirstMethod(self):
        return 1


obj = MyClass()
# print(MyClass.__dict__)
print(MyClass.FirstAttr)
print(obj.first_method())
'''
# TEST_4:
@snake_case(attrs=True)
class MyClass:
    FirstAttr = 1
    superSecondAttr = 2

    def __init__(self):
        self.MyName = 'John Doe'


obj = MyClass()
print(obj.MyName)

myclass_attrs = ['FirstAttr', 'superSecondAttr']

for attr in myclass_attrs:
    try:
        print(MyClass.__dict__[attr])
    except KeyError:
        print('атрибут отсутствует')

# TEST_5:
@snake_case()
class MyClass:
    def FirstMethod(self):
        return 1

    def superSecondMethod(self):
        return 2


obj = MyClass()

myclass_attrs = ['FirstMethod', 'superSecondMethod']

for method in myclass_attrs:
    try:
        print(obj.__dict__[method])
    except KeyError:
        print('метод отсутствует')

# TEST_6:
@snake_case()
class MyClass:
    def _FirstMethod(self):
        return 1

    def _superSecondMethod(self):
        return 2


obj = MyClass()

print(obj._first_method())
print(obj._super_second_method())'''