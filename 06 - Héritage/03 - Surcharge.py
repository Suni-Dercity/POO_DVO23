class Car:

    # Attributs de classe
    # Sorte de constantes
    # Communes à toutes les voitures
    tires = 4
    engine = 1

    # Ici on défini des 'constantes' de classe car toutes les voitures auront 4 roues et  1 moteur

    def __init__(self):
        self.name = 'Deluxo'

class SportCar(Car):
    def __init__(self):
        self.name = "Toreador"  # Si t'as la ref, cool


car1 = SportCar()
print(car1.name)
print(car1.tires)

car1.tires = 3
print(car1.tires)
# Le constructeur de la classe enfant a écrasé le constructeur de la classe parent