class ElectricCar:
    def __init__(self, color):
        self.color = color


car = ElectricCar('black')


print(str(car)==repr(car))