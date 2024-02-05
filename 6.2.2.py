'''
Класс SparseArray
Разреженный массив (список) — абстрактное представление обычного массива (списка), в котором данные представлены не непрерывно, а фрагментарно: большинство его элементов принимает одно и то же значение по умолчанию, обычно 0 или None. В разреженном массиве возможен доступ к неопределенным элементам, в этом случае массив вернет некоторое значение по умолчанию.

Реализуйте класс SparseArray, описывающий разреженный массив. При создании экземпляра класс должен принимать один аргумент:

default — значение по умолчанию для неопределенных элементов разреженного массива
Экземпляр класса SparseArray должен позволять получать и изменять значения своих элементов с помощью индексов. При попытке получить значение элемента по несуществующему индексу должно быть возвращено значение по умолчанию.

Примечание 1. Гарантируется, что при доступе к элементам используются только неотрицательные индексы.

Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 3. Никаких ограничений касательно реализации класса SparseArray нет, она может быть произвольной.
'''
            
class SparseArray:
    def __init__(self,default):
        self.sequence = dict()
        self.default = default    
        
    def __getitem__(self,key):
        return self.sequence.get(key,self.default)

    def __setitem__(self,key,value):       
        self.sequence[key] = value
        
        
     

array = SparseArray(None)

indexes = [516, 3610, 2080, 4131, 1583, 3120, 1591, 4674, 3652, 2632, 1609, 2644, 3677, 1118, 3181, 3695, 2685, 3712,
           644, 4230, 4744, 3219, 660, 4759, 1690, 4252, 4258, 4773, 4777, 1710, 2736, 1717, 1212, 705, 4292, 4809,
           3788, 4302, 4315, 4829, 1246, 737, 3814, 743, 4853, 4342, 3837, 3339, 3343, 3346, 1301, 1818, 1819, 2331,
           1307, 4389, 808, 3371, 2860, 819, 1332, 2870, 3382, 4417, 4419, 2373, 2377, 2389, 1372, 2912, 3425, 4970,
           2923, 4462, 1909, 4473, 4487, 1938, 3475, 918, 2455, 2970, 2458, 3995, 1439, 1955, 2468, 1445, 1965, 4536,
           4544, 1985, 4037, 1478, 969, 4052, 4084, 4089, 506]

for ind in indexes:
    array[ind] = 'Мне больно видеть белый свет, мне лучше в полной темноте'
    print(array[ind])