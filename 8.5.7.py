'''
Декоратор @limiter🌶️🌶️
Любой пользовательский класс по умолчанию способен создавать бесконечное количество собственных экземпляров. Шаблон проектирования синглтон, напротив, гарантирует, что класс имеет только один собственный экземпляр, и при попытке создать новый, он возвращает уже имеющийся. 

Реализуйте декоратор @limiter для декорирования класса, с помощью которого можно ограничивать количество создаваемых декорируемым классом экземпляров до определенного числа. Декоратор должен принимать три аргумента в следующем порядке:

limit — количество экземпляров, которое может создать декорируемый класс
unique — имя атрибута экземпляра декорируемого класса, значение которого является его идентификатором. Два экземпляра с одинаковыми идентификаторами существовать не могут. Если происходит попытка создать экземпляр, идентификатор которого совпадает с идентификатором одного из ранее созданных экземпляров, должен быть возвращен этот ранее созданный экземпляр
lookup — определяет, какой объект должен быть возвращен, если превышено ограничение limit, а значение атрибута unique ранее не использовалось. При значении FIRST возвращается самый первый созданный экземпляр, при значении LAST — самый последний созданный экземпляр
Примечание 1. Гарантируется, что экземпляры декорируемого класса всегда имеют атрибут, который содержит их идентификатор.
'''
    
    
def limiter(limit, unique, lookup):
    lim = -1
    objects = {}
    lu = {'FIRST': 0, 'LAST': -1}
    def decorator(cls):
        def inner(*args, **kwargs):
            nonlocal lim
            lim += 1
            obj = cls(*args, **kwargs)
            if lim >= limit:
                if getattr(obj, unique) in objects:
                    return objects.setdefault(getattr(obj, unique), obj)
                else:
                    return objects[list(objects.keys())[lu[lookup]]]
            return objects.setdefault(getattr(obj, unique), obj)
        return inner
    return decorator
    