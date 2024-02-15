import random as r
class Item:
  all_items = {'hands': {1: {'name':'Кирка','dmg':1}, 
                         2: {'name': 'Факел', 'dmg': 2},
                         3: {'name': 'Лом', 'dmg': 2},
                         4: {'name':'Лопата','dmg': 3}},
              'head': {1:{'name':'Шапка ушанка','def': 1}},
              'body': {1:{'name':'Ватник','def': 1}}, 
              'legs': {1:{'name':'Валенки','def': 1}},
              'key':  {1:{'name': 'Большой ржавый ключ от ворот кладбища','def': 0}}
              }

  def get_item(self, monster_name):
    if monster_name == 'Сторож':
      return ('key', Item.all_items.get('key').get(1))
    else:
      type_item = r.choice(['hands','hands','hands', 'head', 'body', 'legs'])
      n_item = r.choice(list(Item.all_items.get(type_item).keys())) 
      return (type_item, Item.all_items.get(type_item).get(n_item))
      
class Monster(Item):
    default_hp  = 9
    
  def __init__(self):
    self.name = self.__get_name()
    self.hp = self.__get_hp
    self.attack = self.__get_attack()
    self.item = self.get_item(self.name)

    
  @staticmethod
  def __get_name():
    return r.choice(['Вампир', 'Скелет', 'Зомби', 'Сторож'])

  @staticmethod
  def __get_hp():
    return default_hp
    
  @staticmethod
  def __get_attack():
    return r.randint(1, 3)      
    
    
test_monster = Monster()

print(test_monster.__dict__)