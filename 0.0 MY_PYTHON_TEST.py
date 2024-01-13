class ElectricCar:
    def __init__(self, color):
        self._color = color

    @property
    def color(self):
        raise AttributeError
        
    @color.setter
    def color(self, color):
        self._color = color


car = ElectricCar('black')

car.color = 'yellow'

print(car.color)