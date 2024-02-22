'''
Класс FieldTracker🌶️🌶️
Реализуйте класс FieldTracker, наследники которого получают возможность отслеживать состояние определенных атрибутов своих экземпляров класса. Дочерние классы должны наследовать четыре метода экземпляра:

base() — метод, принимающий в качестве аргумента имя атрибута и возвращающий либо текущее значение этого атрибута, либо исходное (указанное при определении) значение этого атрибута, если оно было изменено
has_changed() — метод, принимающий в качестве аргумента имя атрибута и возвращающий True, если значение этого атрибута было изменено хотя бы раз, или False в противном случае
changed() — метод, возвращающий словарь, в котором ключами являются имена атрибутов, которые изменяли свои значения, а значениями — их исходные значения
save() — метод, сбрасывающий отслеживание. После вызова метода считается, что все атрибуты ранее не изменяли свои значения, а их текущие значения считаются исходными
Гарантируется, что наследники класса FieldTracker:

всегда имеют атрибут класса fields, содержащий кортеж с атрибутами, которые необходимо отслеживать
в своем инициализаторе всегда вызывают инициализатор класса FieldTracker после установки первичных значений отслеживаемым атрибутам
Примечание 1. Будем считать, что атрибут изменяет свое значение только в том случае, если устанавливаемое значение отличается от текущего.

Примечание 2. Реализация класса FieldTracker может быть произвольной, то есть требований к наличию определенных атрибутов нет.

Примечание 3. Дополнительная проверка данных на корректность в методах не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
'''

# мое решение
class FieldTracker:
    fields = ('x', 'y', 'z')
    
    def __init__(self,*args):
        for attr,value in zip(self.fields,args):
            self.__dict__.setdefault(attr,[]).append(value)
    
    def base(self,attr):
        return self.__dict__[attr][0]
        
    def __setattr__(self,key,value):
        self.__dict__.setdefault(key,[]).append(value)
        
    def __getattribute__(self,key):
        value = object.__getattribute__(self, key)
        if isinstance(value,list):
            return value[-1]
        return value    
        
    def has_changed(self,key):
        if len(self.__dict__[key])==1:
            return False
        return True    
        
    def changed(self):
        result_dict = {}
        for key in self.__dict__:
            if self.has_changed(key):
                result_dict.setdefault(key,self.base(key))
        return result_dict        
                
                
    def save(self):
        for key in self.__dict__:
            if self.has_changed(key):
                self.__dict__[key] = [self.__dict__[key][-1]]
    
# Решение Валерия    
class FieldTracker:
    def __init__(self):
        self._values = {
            field: getattr(self, field)
            for field in self.fields
        }

    def base(self, field):
        return self._values[field]

    def has_changed(self, field):
        return self._values[field] != getattr(self, field)

    def changed(self):
        return {
            field: self.base(field)
            for field in self.fields
            if self.has_changed(field)
        }

    def save(self):
        for field in self.fields:
            self._values[field] = getattr(self, field)    
            
class FieldTracker:
    values = {}

    def __setattr__(self, k, v):
        FieldTracker.values.setdefault(k, []).append(v)
        object.__setattr__(self, k, v)

    def base(self, name):
        return FieldTracker.values[name][0]

    def has_changed(self, name):
        return len(FieldTracker.values[name]) > 1

    def changed(self):
        return {k:v[0] for k, v in FieldTracker.values.items() if len(v) > 1}

    def save(self):
        FieldTracker.values = {k:[v[-1]] for k, v in FieldTracker.values.items()}            

class FieldTracker:
    def __init__(self):
        self._save_dict = __import__("copy").deepcopy(self.__dict__)

    def base(self, name):
        return self._save_dict[name]

    def has_changed(self, name):
        return not (self._save_dict[name] == self.__dict__[name])

    def changed(self):
        return {key: self._save_dict[key] for key in self._save_dict if self.has_changed(key)}

    def save(self):
        del self.__dict__["_save_dict"]
        FieldTracker.__init__(self)

   
# INPUT DATA:

# TEST_1:
class Point(FieldTracker):
    fields = ('x', 'y', 'z')

    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
        super().__init__()

point = Point(1, 2, 3)


print(point.base('x'))
print(point.has_changed('x'))
print(point.changed())

# TEST_2:
class Point(FieldTracker):
    fields = ('x', 'y', 'z')

    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
        super().__init__()

point = Point(1, 2, 3)

print(point.__dict__)
point.x = 0
point.z = 4
point.z = 5
point.z = 7

print(point.__dict__)
print(point.base('x'))
print(point.base('z'))
print(point.has_changed('x'))
print(point.has_changed('z'))
print(point.changed())
'''
# TEST_3:
class Point(FieldTracker):
    fields = ('x', 'y', 'z')

    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
        super().__init__()

point = Point(1, 2, 3)
point.x = 0
point.z = 4
point.save()

print(point.base('x'))
print(point.base('z'))
print(point.has_changed('x'))
print(point.has_changed('z'))
print(point.changed())

# TEST_4:
class Point(FieldTracker):
    fields = ('x', 'y', 'z')

    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
        super().__init__()


p = Point(1, 2, 3)
print(p.changed())
p.x = 4
print(p.changed())
print(p.x)
print()
print(p.__dict__)
print()
p.z = 6
print(p.changed())
p.save()
print(p.changed())
p.y = 8
print(p.changed())
print(p.y)
p.save()
print(p.changed())
p.save()
print(p.changed())

# TEST_5:
class Point(FieldTracker):
    fields = ('x', 'y', 'z')

    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
        super().__init__()


p = Point(1, 2, 3)
print(p.has_changed('x'))
print(p.has_changed('y'))
print(p.has_changed('z'))
p.x = 4
print(p.has_changed('x'))
print(p.has_changed('y'))
print(p.has_changed('z'))
p.z = 6
print(p.has_changed('x'))
print(p.has_changed('y'))
print(p.has_changed('z'))
p.save()
print(p.has_changed('x'))
print(p.has_changed('y'))
print(p.has_changed('z'))
p.y = 8
print(p.has_changed('x'))
print(p.has_changed('y'))
print(p.has_changed('z'))
p.save()
print(p.has_changed('x'))
print(p.has_changed('y'))
print(p.has_changed('z'))

# TEST_6:
class Point(FieldTracker):
    fields = ('x', 'y', 'z')

    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
        super().__init__()


p = Point(1, 2, 3)
print(p.base('x'))
p.x = 4
print(p.base('x'))
print(p.x)
p.z = 6
print(p.base('x'))
print(p.base('y'))
print(p.base('z'))
p.save()
print(p.base('x'))
print(p.base('y'))
print(p.base('z'))
p.y = 8
print(p.base('y'))
print(p.y)
p.save()
print(p.base('y'))'''