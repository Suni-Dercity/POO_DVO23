class Animal:

    def __init__(self):
        print("Un animal vient d'être crée")
        self.age = 0

scooby = Animal()
# pour accéder à l'attribut on utilise le point
print(scooby.age)

scooby.age = 27
print(scooby.age)