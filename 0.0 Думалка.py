a = '999999999999999'
b = '7777777777777777777'
res = '7778777777777777776'


def my_sum(a :str,b :str) ->int:
    len_a = a.__len__
    len_b = b.__len__
    res = ''
    for index,_ in enumerate(b):
        if index<len_a:
            c = a[~index]+b[~index]
            if c<9:
                res+=str(c)
            else:    
                
        