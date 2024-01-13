'''
Класс CaseHelper 🌶️🌶️
Snake Case — стиль написания составных слов, при котором несколько слов разделяются символом нижнего подчеркивания (_) и не имеют пробелов в записи, причём каждое слово пишется с маленькой буквы. Например, bee_geek и hello_world.

Upper Camel Case — стиль написания составных слов, при котором несколько слов пишутся слитно без пробелов, при этом каждое слово пишется с заглавной буквы. Например, BeeGeek и HelloWorld.

Реализуйте класс CaseHelper, описывающий набор функций для работы со строками в стилях Snake Case и Upper Camel Case. При создании экземпляра класс не должен принимать никаких аргументов.

Класс CaseHelper должен иметь четыре статических метода:

is_snake() — метод, принимающий в качестве аргумента строку и возвращающий True, если переданная строка записана в стиле Snake Case, или False в противном случае
is_upper_camel() — метод, принимающий в качестве аргумента строку и возвращающий True, если переданная строка записана в стиле Upper Camel Case, или False в противном случае
to_snake() — метод, который принимает в качестве аргумента строку в стиле Upper Camel Case, записывает ее в стиле Snake Case и возвращает полученный результат
to_upper_camel() — метод, который принимает в качестве аргумента строку в стиле Snake Case, записывает ее в стиле Upper Camel Case и возвращает полученный результат
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
'''
from copy import copy
import re

class CaseHelper:
    
    @staticmethod
    def is_snake(input_string):
        return bool(re.search(r'[a-z]\B\_\B[a-z]|\b[a-z]{1,}\b',input_string))
        
    @staticmethod
    def is_upper_camel(input_string):
        return bool(re.search(r'\b[A-Z]\w+[a-z]\b',input_string))
        
    @staticmethod
    def to_snake(input_string):
        if not CaseHelper.is_upper_camel(input_string):
            return input_string
        else:    
            my_string = copy(input_string)
            reg = re.findall(r'[A-Z]',input_string)
            # print(f'{input_string}: {reg}')
            
            for index, i in enumerate(my_string[::-1]):
                if i in reg:
                    if index!=0:
                        input_string = input_string.replace(i,f'_{i.lower()}')
                    else:
                        input_string = input_string.replace(i,f'{i.lower()}')
                        
            return input_string[1:] if input_string[0] =='_' else input_string
            
            
    @staticmethod
    def to_upper_camel(input_string):
        
        if not CaseHelper.is_snake(input_string):
            return input_string
        else:
            my_string = ''.join([i[0].upper()+i[1:] for i in input_string.split('_')])
        
            return my_string
        
        
cases = ['AssertEqual', 'SetUp', 'TearDown', 'AddModuleCleanup', 'AssertRaisesRegex', 'AssertAlmostEqual', 'AssertNotAlmostEqual']

for case in cases:
    print(CaseHelper.to_snake(case))
    
    
'''
assert_equal
set_up
tear_down
add_module_cleanup
assert_raises_regex
assert_almost_equal
assert_not_almost_equal
'''