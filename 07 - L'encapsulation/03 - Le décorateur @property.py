class Car:
    def __init__(self):
        self._tires = 4

    # Décorateur qui permet de mettre en place une propriété
    @property
    def tires(self):
        print("Recuperation of tires")
        return self._tires

car1 = Car()
print(car1._tires)