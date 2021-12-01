# un attribut de classe est un attribut partagé par toutes les instance de la classe.
# cad l'espace mémoire d'un attribut de classe esy un espace partagé par toutes les instances / objets de la classe n'ayant pas
# leur prore espace mémoire

class Animal:

    def __init__(self):
        print("Un animal vient d'être crée")
        # définition d'attribut
        self.age = 0  # on appel ça une variable d'instance en Python

# toutes les instances de la class Animal auront l'attribut age
# accessible via le mot clé self

# que tous les objets qui seront crées à partir de la classs Animal auront l'attribut age avec la valeur 0 par défaut

# le constructeur il initalise des variables d'instances stockées en mémoire

scooby = Animal()
print(dir(scooby))