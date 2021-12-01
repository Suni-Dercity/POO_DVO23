class Animal:

    # attribut de classe
    class_attribut = 0

    def __init__(self, age = 1):
        print("Un animal vient d'être crée")
        self.age = age

        # Mise en place d'un compteur pour savoir combien de fois ma classe a été instanciée
        Animal.class_attribut += 1

class Cat(Animal):
    # Le constructeur de la classe parents a été appelé implicitement
    # dans l'attribut de classe class_attribut a été incrémenté lors de l'instanciation de la classe Cat
    pass

scooby = Animal(22)
scooby1 = Animal(24)
scooby2 = Animal(23)
print(scooby.age)

# je retrouve à l'intérieur son attribut de classe
print(dir(scooby))

# pour avoir la valeur de l'attribut de classe
print(Animal.class_attribut)

cat1 = Cat()
print(Animal.class_attribut)