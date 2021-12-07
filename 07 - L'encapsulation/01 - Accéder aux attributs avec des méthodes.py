class Car:
    def __init__(self):
        self.name = 'Toreador'

    def return_model(self):
        return '250'

car1 = Car()
print(car1.return_model())