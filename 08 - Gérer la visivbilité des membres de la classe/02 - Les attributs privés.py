class Car:

    def __init__(self, name):
        self.__name = name

    def return_name(self):
        return self.__name

car1 = Car('Infernus')
# print(car1.name) # erreur car attribute privée

# pseudo privée

# pour récupérer la valeur de l'attribut privée
print(car1.return_name())

# en repassant par la classe je peux quand même le récupérer
print(car1._Car__name)