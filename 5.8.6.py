'''
Класс AttrsNumberObject
Реализуйте класс AttrsNumberObject. При создании экземпляра класс должен принимать произвольное количество именованных аргументов. Все передаваемые аргументы должны устанавливаться создаваемому экземпляру в качестве атрибутов.

Экземпляр класса AttrsNumberObject должен иметь один атрибут:

attrs_num — количество атрибутов, которыми обладает экземпляр класса AttrsNumberObject на данный момент, включая сам атрибут attrs_num
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса AttrsNumberObject нет, она может быть произвольной.
'''

class AttrsNumberObject:
    def __init__(self,**kwargs):
        self.attrs_num = 0
        for key,value in kwargs.items():
            setattr(self,key,value)
            
    def __setattr__(self,key,value):
        object.__setattr__(self,key,value)
        self.__dict__['attrs_num']+=1
        
    def __delattr__(self,attr):
        del self.__dict__[attr]
        self.__dict__['attrs_num']-=1
        
music_group = AttrsNumberObject(name='Alexandra Savior', genre='dream pop')

print(music_group.attrs_num)
del music_group.genre
print(music_group.attrs_num)       