class ElectricCar:
    def __init__(self, power_reserve):
        self.power_reserve = power_reserve

    def __bool__(self):
        return self.power_reserve > 0


car1 = ElectricCar(400)
car2 = ElectricCar(350)

print(bool(car1) + bool(car2))