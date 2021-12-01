class Car:

    tires = 4
    engine = 1

    def __init__(self, name):
        self.name = name


class SportCar(Car):

    def __init__(self,name,color):
        super().__init__(name)
        self.color = color

Car1 = SportCar('Lamborghini', 'midnight blue')
print(Car1.name)
print(Car1.color)