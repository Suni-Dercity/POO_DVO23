class Animal:

    def __init__(self, age = 1):
        print("Un animal vient d'être crée")
        self.age = age

    def vieillir(self):
        self.age += 1


scooby = Animal()
# pour accéder à l'attribut on utilise le point
print(scooby.age)

# Appeler notre méthode
scooby.vieillir()
print(scooby.age)