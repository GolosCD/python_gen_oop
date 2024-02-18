'''
Контекстный менеджер safe_open
Реализуйте контекстный менеджер safe_open с помощью декоратора @contextmanager, который принимает два аргумента в следующем порядке:

filename — имя файла
mode — режим открытия файла (r, w, a и так далее), по умолчанию имеет значение r
Контекстный менеджер должен открывать файл с именем filename в режиме mode и позволять выполнять с ним соответствующие операции. Причем если открытие файла было выполнено без исключений, в качестве значения, используемого в блоке with, контекстный менеджер должен вернуть кортеж из двух элементов, первым из которых является необходимый файловый объект, вторым — значение None. Однако если при открытии файла было возбуждено исключение, то в качестве значения, используемого в блоке with, контекстный менеджер должен вернуть кортеж из двух элементов, первым из которых является значение None, вторым — возбужденное при открытии исключение. Также контекстный менеджер должен закрывать открытый им файл после выполнения кода внутри блока with.

Примечание 1. Наглядные примеры использования контекстного менеджера safe_open продемонстрированы в тестовых данных.

Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный контекстный менеджер используется только с корректными данными.
'''


from contextlib import contextmanager


@contextmanager
def safe_open(filename,mode='r'):
    try:
        open_file = open(filename,mode=mode)
        yield (open_file,None)
    except Exception as err:
        yield (None,err)
    
    finally:
        open_file.close()
    
    
    with open('Ellies_jokes.txt', 'w') as file:
    file.write('Знаешь, кто не прав? Лев\n')
    file.write('Что треугольник сказал кругу? Катись отсюда')
    
with safe_open('Ellies_jokes.txt') as file:
    file, error = file
    print(error)
    print(file.read())