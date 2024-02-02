class ElectricCar:
    def __init__(self, power_reserve):
        self.power_reserve = power_reserve

    def __bool__(self):
        return self.power_reserve > 0
    
    def __eq__(self,other):
        return self.power_reserve==other.power_reserve


car1 = ElectricCar(400)

# print(id(car1.power_reserve))

car1.power_reserve = 340

# print(id(car1.power_reserve))

print(car1.__hash__)