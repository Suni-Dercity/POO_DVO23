class Car:
    def __init__(self):
        self._tires = 4

    # Décorateur qui permet de mettre en place une propriété
    @property
    def tires(self):
        print("Recuperation of tires")
        return self._tires

    @tires.setter
    def tires(self,number):
        print('Modification of tires')
        self._tires = number

car1 = Car()
print(car1._tires)
car1.tires = 5
print(car1._tires)