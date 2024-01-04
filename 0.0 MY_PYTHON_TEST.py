import itertools as it

iterable = iter('Beegeek')
iterable,copy_iterable =  it.tee(iterable,2)
l = len (list(copy_iterable))
print(l)
print(next(iterable))



