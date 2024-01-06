'''
Функция pluck()
Реализуйте функцию pluck(), которая принимает три аргумента в следующем порядке:

data — словарь произвольной вложенности
path — строка, представляющая собой ключ или последовательность ключей, перечисленных через точку .
default — произвольный объект, значение по умолчанию; имеет значение None, если не передан явно
Функция должна возвращать значение по ключу path из словаря data. Если path представляет собой последовательность ключей, например, key1.key2, 
то возвращаемым значением функции должно быть значение по ключу key2 из словаря data[key1]. Если указанного ключа или хотя бы одного ключа из последовательности ключей в словаре нет, 
функция должна вернуть значение default.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию pluck(), но не код, вызывающий ее.
'''


def find_key(data, key):
    if key in data:
        return data[key]                # базовый случай

    for v in data.values():
        if type(v) == dict:
            value = find_key(v, key)    # рекурсивный случай
            if value is not None:
                return value
                
                

def pluck(data :dict, path :str, default = None):
    *a,key = path.split('.')
    if len(a)==0 and key not in data.key():
        return default
    else:    
        result = find_key(data,key)
        if result:
            return result
        else:
            return default
    



d = {'a': {'b': 5, 'z': 20}, 'c': {'d': 3}, 'x': 40}

print(pluck(d, 'z', 0))