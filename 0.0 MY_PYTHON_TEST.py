from abc import ABC, abstractmethod


class MyTest(ABC):
    
    @classmethod
    @abstractmethod
    def wtf(cls,self): pass
        
        
        
class Test(MyTest):
    
    def wtf(self):
        print('WTF!!!')
    
    
    
exampl = Test()

exampl.wtf()

    