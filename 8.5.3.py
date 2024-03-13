'''
Декоратор @jsonattr
Реализуйте декоратор @jsonattr для декорирования класса. Декоратор должен принимать один аргумент:

filename — имя json файла, содержимым которого является JSON объект
Декоратор должен открывать файл filename и добавлять в качестве атрибута декорируемому классу каждую пару ключ-значение JSON объекта, содержащегося в этом файле.

Примечание. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input:

with open('test.json', 'w') as file:
    file.write('{"x": 1, "y": 2}')

@jsonattr('test.json')
class MyClass:
    pass
    
print(MyClass.x)
print(MyClass.y)
'''

import json

def jsonattr(json_file_name):
    with open(json_file_name,'r',encoding = 'utf-8') as raw_file:
        data = json.load(raw_file)
        
        def decorator(cls):
            for key in data:
                setattr(cls, key, data.get(key))
            return cls
    return decorator  
    
with open('test.json', 'w') as file:
    file.write('{"x": 1, "y": 2}')

@jsonattr('test.json')
class MyClass:
    pass
    
print(MyClass.x)
print(MyClass.y)    