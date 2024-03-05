'''
Классы LeftParagraph и RightParagraph
Будем называть словом любую последовательность из одной или более латинских букв.

1. Реализуйте класс LeftParagraph, описывающий абзац, выровненный по левому краю. При создании экземпляра класс должен принимать один аргумент:

length — длина строки абзаца
Класс LeftParagraph должен иметь два метода экземпляра:

add() — метод, принимающий в качестве аргумента слово или несколько слов, разделенных пробелом, и добавляющий их в текущий абзац. Если слово не помещается на текущей строке, оно переносится на следующую. Также метод должен автоматически добавлять один пробел после каждого добавленного слова (кроме последнего)
end() — метод, печатающий текущий абзац, выровненный по левому краю. После вызова метода текущий абзац считается пустым, то есть начинается формирование нового
2. Также реализуйте класс RightParagraph, описывающий абзац, выровненный по правому краю. При создании экземпляра класс должен принимать один аргумент:

length — длина строки абзаца
Класс RightParagraph должен иметь два метода экземпляра:

add() — метод, принимающий в качестве аргумента слово или несколько слов, разделенных пробелом, и добавляющий их в текущий абзац. Если слово не помещается на текущей строке, оно переносится на следующую. Также метод должен автоматически добавлять один пробел после каждого добавленного слова (кроме последнего)
end() — метод, печатающий текущий абзац, выровненный по правому краю с учетом длины строки. После вызова метода текущий абзац считается пустым, то есть начинается формирование нового
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованные классы используются только с корректными данными.

Примечание 2. Никаких ограничений касательно реализаций классов нет, они могут быть произвольными.
'''


from abc import ABC, abstractmethod


class Paragraph(ABC):

    def __init__(self, length :int):
        self.length =length
        self.paragraph = []
    
    def add(self, text :str):
        self.paragraph.extend(text.split())
        
    @abstractmethod    
    def end(self):
        pass
            
        
        
class LeftParagraph(Paragraph):
    def end(self):
        empty = ''
        for line in self.paragraph:
            if len(empty)+len(line)<self.length:
                empty+=f'{line} '
            else:
                print(empty[:-1],end = '\n')
                empty = ''
                empty+=f'{line} '
        print(empty[:-1],end = '\n')
        self.paragraph.clear()
            
class RightParagraph(Paragraph):
    def end(self):
        empty = ''
        for line in self.paragraph:
            print(f'0) line: {line}')
            if len(empty)+len(line)<self.length:
                empty=empty +' '+ line
                if empty[0]==' ':
                    empty=empty[1:]
                print(f'1) empty:{empty}, line: {line}')
            else:
                print(f'2)len(empty):{len(empty)} empty:{empty}')
                print(empty.rjust(self.length),end = '\n')
                empty = ''
                empty=empty +' '+ line
                print(f'3) empty:{empty}, line: {line}')
        print(empty.rjust(self.length),end = '\n')
        self.paragraph.clear()
'''        
# INPUT DATA:

# TEST_1:
leftparagraph = LeftParagraph(10)

leftparagraph.add('death')
leftparagraph.add('can have me')
leftparagraph.add('when it earns me')
leftparagraph.end()

# TEST_2:
rightparagraph = RightParagraph(10)

rightparagraph.add('death')
rightparagraph.add('can have me')
rightparagraph.add('when it earns me')
rightparagraph.end()

# TEST_3:
leftparagraph = LeftParagraph(23)

leftparagraph.add('Multiply noise and joy')
leftparagraph.add('Sing songs in a good hour')
leftparagraph.add('Friendship grace and youth')
leftparagraph.add('Our birthday girls')
leftparagraph.end()

leftparagraph.add('Meanwhile the winged child')
leftparagraph.add('friends greeting you')
leftparagraph.add('Secretly thinks sometime')
leftparagraph.add('I will be the birthday boy')
leftparagraph.end()
'''
# TEST_4:
rightparagraph = RightParagraph(28)

rightparagraph.add('I will not regret the roses')
rightparagraph.add('Withered with a light spring')
rightparagraph.add('I love the grapes on the vines')
rightparagraph.add('Ripened in the hands under the mountain')
rightparagraph.end()
print('*******************************************************')
rightparagraph.add('The beauty of my green valley')
rightparagraph.add('Golden joy of autumn')
rightparagraph.add('oblong and transparent')
rightparagraph.add('Like the fingers of a young maiden')
rightparagraph.end()