'''
Класс DevelopmentTeam
Реализуйте класс DevelopmentTeam, описывающий команду разработчиков двух уровней: junior (младший) и senior (старший). При создании экземпляра класс не должен принимать никаких аргументов.

Класс DevelopmentTeam должен иметь два метода экземпляра:

add_junior() — метод, принимающий произвольное количество позиционных аргументов, каждый из которых является именем разработчика, и добавляющий их в число junior-разработчиков
add_senior() — метод, принимающий произвольное количество позиционных аргументов, каждый из которых является именем разработчика, и добавляющий их в число senior-разработчиков
Экземпляр класса DevelopmentTeam должен быть итерируемым объектом, элементами которого сперва являются все его junior-разработчики, а затем — все senior-разработчики. Junior-разработчики должны быть представлены в виде кортежей:

(<имя разработчика>, 'junior')
в то время как senior-разработчики — в виде кортежей:

(<имя разработчика>, 'senior')
Примечание 1. Разработчики в группах должны располагаться в том порядке, в котором они были добавлены.

Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 3. Никаких ограничений касательно реализации класса DevelopmentTeam нет, она может быть произвольной.
'''


class DevelopmentTeam:
    def __init__(self):
        self.junior = list()
        self.senior = list()
        
    def add_junior(self,*args):
        self.__dict__['junior'].extend(args)  
            
    def add_senior(self,*args):
        self.__dict__['senior'].extend(args)  
        
    def __iter__(self):
        yield from ((name,'junior') for name in self.junior)
        yield from ((name,'senior') for name in self.senior)
        
beegeek = DevelopmentTeam()

beegeek.add_junior('Timur')
beegeek.add_junior('Arthur', 'Valery')
beegeek.add_senior('Gvido')
# print(beegeek.junior)

print(*beegeek, sep='\n')