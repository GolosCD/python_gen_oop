'''
Декоратор @jsonify
Реализуйте декоратор @jsonify, преобразующий возвращаемое значение декорируемой функции в строку формата JSON.

Также декоратор должен сохранять имя и строку документации декорируемой функции.

Примечание 1. Гарантируется, что возвращаемое значение функции принадлежит типу, который поддерживается форматом JSON.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый декоратор @jsonify, но не код, вызывающий его.
'''

from functools import wraps
import json

def jsonify(func):
    
    @wraps(func)
    def wrapper(*args,**kwargs):
        result = func(*args,**kwargs)
        return json.dumps(result)
    return wrapper