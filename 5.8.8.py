'''
Класс ProtectedObject
Будем считать атрибут защищенным, если его имя начинается с символа нижнего подчеркивания (_). Например, _password, __email и __dict__.

Реализуйте класс ProtectedObject. При создании экземпляра класс должен принимать произвольное количество именованных аргументов. Все передаваемые аргументы должны устанавливаться создаваемому экземпляру в качестве атрибутов.

Класс ProtectedObject должен запрещать получать и изменять значения защищенных атрибутов своих экземпляров, а также удалять эти атрибуты. При попытке получить или изменить значение защищенного атрибута, а также попытке удалить атрибут, должно возбуждаться исключение AttributeError с текстом:

Доступ к защищенному атрибуту невозможен
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса ProtectedObject нет, она может быть произвольной.

'''

'''class ProtectedObject:
   
    def __init__(self,**kwargs):
        for key,value in kwargs.items():
            object.__setattr__(self,key,value)
        
        
    def __getattribute__(self,key):
        print(f'Зашли в self.__getattribute__ c key={key}')
        print('-')
        
        if key.startswith('_'): 
            print('+')
            raise AttributeError ('Доступ к защищенному атрибуту невозможен')            
        return object.__getattribute__(self,key) 
            
             

    def __delattr__ (self,key):
        print(f'Зашли в self.__delattr__ c {key}')
        print('-')
        
        if key.startswith('_'): 
            raise AttributeError ('Доступ к защищенному атрибуту невозможен')            
        return object.__delattr__(self,key)    
  
        
    def __setattr__(self,key,value):
        print(f'Зашли в self.__setattr__ c key={key} и value={value}')
        print('-')
        
        if not key.startswith('_'):
            object.__setattr__(self,key,value)
        else:    
            raise AttributeError ('Доступ к защищенному атрибуту невозможен')'''
  

class ProtectedObject:
   
    def __init__(self,**kwargs):
        for key,value in kwargs.items():
            object.__setattr__(self,key,value)
        
        
    def __getattribute__(self,key):
        
        if key.startswith('_'): 
            raise AttributeError ('Доступ к защищенному атрибуту невозможен')            
        return object.__getattribute__(self,key) 
            
             

    def __delattr__ (self,key):

        if key.startswith('_'): 
            raise AttributeError ('Доступ к защищенному атрибуту невозможен')            
        return object.__delattr__(self,key)    
  
        
    def __setattr__(self,key,value):

        if not key.startswith('_'):
            object.__setattr__(self,key,value)
        else:    
            raise AttributeError ('Доступ к защищенному атрибуту невозможен')  
            
# INPUT DATA:

# TEST_1:
user = ProtectedObject(login='PG_kamiya', _password='alreadybanned')

try:
    print(user.login)
    print(user._password)
except AttributeError as e:
    print(e)

# TEST_2:
user = ProtectedObject(login='PG_kamiya', _password='alreadybanned')

try:
    user._password = 'qwerty12345'
except AttributeError as e:
    print(e)

# TEST_3:
user = ProtectedObject(login='PG_kamiya', _password='alreadybanned')

try:
    del user._password
except AttributeError as e:
    print(e)

# TEST_4:
user = ProtectedObject(login='PG_kamiya', _password='alreadybanned')

del user.login
print('Успешное удаление атрибута')

# TEST_5:
user = ProtectedObject(login='PG_kamiya', _password='alreadybanned')
print(object.__getattribute__(user, 'login'))
print(object.__getattribute__(user, '_password'))

# TEST_6:
user = ProtectedObject(login='PG_kamiya', _password='alreadybanned')

try:
    user.__dict__['attr'] = 1
except AttributeError as e:
    print(e)

# TEST_7:
user = ProtectedObject(login='PG_kamiya', _password='alreadybanned')

try:
    print(user.__dict__)
except AttributeError as e:
    print(e)

# TEST_8:
user = ProtectedObject(login='PG_kamiya', _password='alreadybanned')

try:
    del user.__dict__['_password']
except AttributeError as e:
    print(e)

# TEST_9:
user = ProtectedObject(login='PG_kamiya', _password='alreadybanned')

del user.login

try:
    print(user.login)
except AttributeError:
    print('Атрибут отсутствует')

# TEST_10:
user = ProtectedObject(login='PG_kamiya', _password='alreadybanned')

user.login = 'Kamiya'
print(user.login)

user.nickname = 'PG'
print(user.nickname)

# TEST_11:
user = ProtectedObject(login='PG_kamiya', _password='alreadybanned')

try:
    print(user._secret)
except AttributeError as e:
    print(e)

try:
    user._secret = 'PG'
except AttributeError as e:
    print(e)

try:
    del user._secret
except Exception as e:
    print(e)            
            
        
        
'''Лучшее решение
import functools

class ProtectedObject:
    def __init__(self, **kwargs):
        for key, val in kwargs.items():
            object.__setattr__(self, key, val)
    
    @staticmethod
    def check_attr(method):
        @functools.wraps(method)
        def wrapper(*args, **kwargs):
            self, attr, *_ = args
            if attr.startswith('_'):
                raise AttributeError('Доступ к защищенному атрибуту невозможен')
            return method(*args, **kwargs)
        return wrapper
    
    @check_attr
    def __getattribute__(self, attr):
        return object.__getattribute__(self, attr)
    
    @check_attr
    def __getattr__(self, attr):
        return object.__getattribute__(self, attr)
    
    @check_attr
    def __setattr__(self, attr, value):
        return object.__setattr__(self, attr, value)

    @check_attr
    def __delattr__(self, attr):
        object.__delattr__(self, attr)

'''        