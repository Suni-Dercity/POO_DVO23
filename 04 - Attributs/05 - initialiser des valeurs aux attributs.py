class Animal:

    def __init__(self, age = 1):
        print("Un animal vient d'être crée")
        self.age = age

scooby = Animal(27)
print(scooby.age)

scooby2 = Animal()
print(scooby2.age)

# les variables d'instance sont spécifique à chaque objet
#elles définissent l'état en l'objet

# je peux avoir des valeurs par défaut si un paramètre est manquant
# imaginons qu'on ne connaissait pas l'age de l'animatl par défaut chaque animal sans age aura 1 an

# construteur est une méthode un peu spéciale
# appelée à la construction d'un objet
# et qui permet d'initialiser des valeurs pour cet objet

