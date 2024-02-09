import functools, time,numpy

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        val = func(*args, **kwargs)
        end = time.perf_counter()
        work_time = end - start
        print(f'Время выполнения {func.__name__}: {round(work_time, 4)} сек.')
        return val
    return wrapper
    
@timer
def pythonsum_book(n):
    a = list(range(n))
    b = list(range(n))
    c = list()
    
    for i in range(len(a)):
        a[i] = i**2
        b[i] = i**3
        c.append(a[i]+b[i])
    return c    
    
@timer
def pythonsum_list(n):
    c = list()
    
    for i in range(n):
        c.append(i**3+i**2)
    return c    

@timer
def pythonsum_dic(n):
    c = dict()
    
    for i in range(n):
        c.setdefault(i**3+i**2,None)
    return c.keys()
    
    
@timer
def numpysum_book(n):
    a = numpy.arange(n) ** 2
    b = numpy.arange(n) ** 3
    c = a+b
    return c

input_num = 1000000

pythonsum_dic(input_num) 
print('================================')  
pythonsum_list(input_num)
print('================================')    
pythonsum_book(input_num)
print('================================')
numpysum_book(input_num)