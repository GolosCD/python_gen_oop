from enum import auto,Enum

class Seasons(Enum):
    WINTER  = auto()
    SPRING  = auto()
    SUMMER  = auto()
    FALL = auto()
    
    def info(self):
        return self.name, self.value
        
    def text_value(self, lang):
        d = {1: 'зима',
             2: 'весна',
             3: 'лето',
             4: 'осень',}
             
        if lang == 'ru':
            return d.get(self.value)
        return self.name.lower()    
        
print(Seasons.FALL.text_value('ru'))
print(Seasons.FALL.text_value('en'))        