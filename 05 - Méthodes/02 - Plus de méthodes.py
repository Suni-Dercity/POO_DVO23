# Exercice

# Mettre en place une méthode qui permet de changer de prénom
# un nouvel attribut
# une nouvelle méthode

class Animal:

    def __init__(self, age = 1, name =""):
        print("Un animal vient d'être crée")
        self.age = age
        self.name = name

    def vieillir(self):
        self.age += 1

    def change_name(self,name):
        self.name = name

scooby = Animal(27, 'Scooby')
print(scooby.age,scooby.name)

scooby.vieillir()
scooby.change_name('Jeff')
print(scooby.age,scooby.name)