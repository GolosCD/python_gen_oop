'''
Классы ArithmeticProgression и GeometricProgression
Реализуйте класс ArithmeticProgression для генерации членов арифметической прогрессии. При создании экземпляра класса ArithmeticProgression должны указываться первый член последовательности и разность прогрессии:

progression = ArithmeticProgression(0, 1)

for elem in progression:
    if elem > 10:
        break
    print(elem, end=' ')    # 0 1 2 3 4 5 6 7 8 9 10
Обратите внимание, что арифметическая прогрессия должна быть итерируемой, а также бесконечной.

Аналогичным образом реализуйте класс GeometricProgression для генерации членов геометрической прогрессии. При создании экземпляра класса GeometricProgression должны указываться первый член последовательности и знаменатель прогрессии:

progression = GeometricProgression(1, 2)

for elem in progression:
    if elem > 10:
        break
    print(elem, end=' ')    # 1 2 4 8
Геометрическая прогрессия, как и арифметическая, должна быть итерируемой, а также бесконечной.
'''


class ArithmeticProgression:
    def __init__(self, first, difference):
        self.first = first
        self.difference = difference

    def __iter__(self):
        self.current = self.first
        return self

    def __next__(self):
        result = self.current
        self.current += self.difference
        return result


class GeometricProgression:
    def __init__(self, first, ratio):
        self.first = first
        self.ratio = ratio

    def __iter__(self):
        self.current = self.first
        return self

    def __next__(self):
        result = self.current
        self.current *= self.ratio
        return result


# INPUT DATA:

# TEST_1:
progression = ArithmeticProgression(0, 1)

for elem in progression:
    if elem > 10:
        break
    print(elem, end=' ')

# TEST_2:
progression = GeometricProgression(1, 2)

for elem in progression:
    if elem > 10:
        break
    print(elem, end=' ')

# TEST_3:
progression = GeometricProgression(4, -2)
count = 0

for item in progression:
    if count == 20:
        break
    count += 1
    print(item, end=' ')

# TEST_4:
progression = ArithmeticProgression(100, -10)
count = 0

for item in progression:
    if count == 20:
        break
    count += 1
    print(item, end=' ')

# TEST_5:
progression = GeometricProgression(100, 10)
count = 0

for item in progression:
    if count == 20:
        break
    count += 1
    print(item, end=' ')