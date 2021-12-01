class Car:

    def __init__(self, name, year, model, brand):
        self.name = name
        self.year = year
        self.model = model
        self.brand = brand


class Citroen:

    def __init__(self):
        self.hydraulic_suspension = True
        self.motor = "Architecture à plat"


class Ds3(Car, Citroen):

    def __init__(self, name, year, model, brand):
        super().__init__(name, year, model, brand)

        #Solution
        Car.__init__(self,name,year,model,brand)
        Citroen.__init__(self)
        # je peux même rajouter si je veux un attribut propre a la classe Ds3
        self.options = ['finition so Chic', 'Kit Décor Intérieur Carmen si biton Carmen']

ds3 = Ds3('New DS3', 2018, "DS3", "Citroen")
print(ds3.name)
# c'est cool ça fonctionne par contre si ej fais le code suivant erreur:
print(ds3.hydraulic_suspension)  # ici il me dit que j'ai pas d'attribut hydraulic_suspension

# l'ordre d'execution des constructeurs à executer la premiere classe parent (Car)
# comment je peux lui dire d'exécuter les deux constructeurs des deux classes parents en passant les bonnes valeurs d'attributs