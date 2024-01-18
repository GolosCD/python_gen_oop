import re

class PhoneNumber:
    def __init__(self,num):
        pattern = r'(\d{3})\ ?(\d{3})\ ?(\d{4})'
        self.number = re.findall(pattern,num)[0]
        
    def __repr__(self):
        return f'''PhoneNumber('{"".join(self.number)}')'''
    
    def __str__(self):
        a,b,c = self.number
        return f"({a}) {b}-{c}"
        
        
phone = PhoneNumber('917 396 3385')

print(str(phone))
print(repr(phone))        