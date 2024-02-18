'''
Контекстный менеджер safe_write
Реализуйте контекстный менеджер safe_write с помощью декоратора @contextmanager, который принимает один аргумент:

filename — имя файла
Контекстный менеджер должен позволять записывать информацию в файл с именем filename. Причем если во время записи в файл было возбуждено какое-либо исключение, контекстный менеджер должен поглотить его, отменить все выполненные ранее записи в файл, если они были, вернуть файл в исходное состояние и проинформировать о возбужденном исключении выводом следующего текста:

Во время записи в файл было возбуждено исключение <тип исключения>
Примечание 1. Наглядные примеры использования контекстного менеджера safe_write продемонстрированы в тестовых данных.

Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный контекстный менеджер используется только с корректными данными.
'''

import io
from contextlib import contextmanager
   
@contextmanager
def safe_write(filename :str):
    tmp_file = None
    flag = True
    try:
        tmp_file = io.StringIO()
        yield tmp_file
    except Exception as err:
        flag = False
        print (f'Во время записи в файл было возбуждено исключение {type(err).__name__}')
    finally:
        if flag:
            write_to_file = open(filename,'w'):
            write_to_file.write(tmp_file)
            write_to_file.close()
        else:
            pass
        

from contextlib import contextmanager


#лучшее решение
@contextmanager
def safe_write(filename):
    file = open(filename, 'a', encoding='u8')
    cursor = file.tell()
    try:
        yield file
    except Exception as err:
        file.truncate(cursor)
        print('Во время записи в файл было возбуждено исключение', type(err).__name__)
    finally:
        file.close()