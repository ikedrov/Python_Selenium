

class Car:
    def __init__(self, model, year, engine, price, mileage):
        self.model = model
        self.year = year
        self.engine = engine
        self.price = price
        self.mileage = mileage
        self.weels = 4

class Truck(Car):
    def __init__(self, model, year, engine, price, mileage):
        super().__init__(model, year, engine, price, mileage)
        self.weels = 8

    @property
    def get_info(self):
        return f'Грузовик {self.model} {self.year} года выпуска, объем двигателя - {self.engine}, цена - {self.price}, пробег - {self.mileage}, {self.weels} колес.'


car = Car('Kia', 2005, 1998, 5500, 120000)
truck = Truck('Man', 2010, 5498, 12000, 10000)

print(truck.get_info)