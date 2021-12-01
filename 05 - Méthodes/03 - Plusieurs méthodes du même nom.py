class Animal:

    def __init__(self, age, name):
        print("Un animal vient d'être crée")
        self.age = age
        self.name = name
        self.first_name = ""

    def vieillir(self):
        self.age += 1

    def change_name(self, name, first_name = ""):
        self.name = name
        self.first_name = first_name

    # Exercice faire une méthode où l'animal se présente
    # -> Salut tout le monde c'est Squeezie

    def introduce(self):
        print(f"Salut toute le monde je m'appelle {self.name} et j'ai {self.age} ans")

scooby = Animal(27, 'Scooby')
scooby.introduce()


