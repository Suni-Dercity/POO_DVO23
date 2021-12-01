# C'est une fonction qui est appelée lorsqu'un crée un objet

class Animal:

    # le mot clé self fait référence a l'objet crée
    # grâce à ce mot clé on va pouvoir accéder aux attributs et méthodes de la classe
    def __init__(self):
        print("Un animal vient d'être crée")
        pass