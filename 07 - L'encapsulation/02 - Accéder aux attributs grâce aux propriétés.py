class Car:
    def __init__(self):
        self.name = 'Toreador'

    def _get_tires(self):
        print("Recuperation of tires")
        return self._tires

    def _set_tires(self, nb_tires):
        print('Modification of tires')
        self._tires = nb_tires

    # premiere façon de mettre en place des propritété de classe
    tires = property(_get_tires, _set_tires)

car1 = Car()
#print(car1.return_model()) # c'est pas une bonne pratique
car1.tires = 5
print(car1.tires)

# le seul problème c'est que je peux quand même accéder à tires