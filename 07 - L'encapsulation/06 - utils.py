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

# Dir
print(dir(car1))

# l'attribut __dict__ (donne les valeurs des attributs de l'instance
print(car1.__dict__)
print(car1)