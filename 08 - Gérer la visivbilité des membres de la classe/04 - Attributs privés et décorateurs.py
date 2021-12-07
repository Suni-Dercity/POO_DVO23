class Car:

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model

    @property
    def model(self):
        return self.__model

    @property
    def brand(self):
        return  self.__brand

    @model.setter
    def model(self,model):
        self.__model = model

    @brand.setter
    def brand(self,brand):
        self.__brand = brand

    #
    # Private method
    #
    def __my_private_method(self):
        print('My private method')

    def test(self):
        self.__my_private_method()

car1 = Car('Infernus', 'Pegassi')
print(car1.model,car1.brand)

car1.model = 'Dugsta'
print(car1.model)

class SportCar(Car):
    pass

cSport = SportCar('Vacca','Idk lol')
print(cSport.__dict__)
# {'_Car__brand': 'Vacca', '_Car__model': 'Idk lol'}

# ce que je ne peux pas faire :
#print(cSport.__model)  # je n'y  ai pas accès car privé

print(cSport._Car__model) # t'as accès à la proprité privée

# je peudx ajouter des attributs à la volé... pas terrible
cSport.test = 2
print(cSport.__dict__)

# bien qu'elle soit privée je peux quand même appeler la méthode privée en passant par cette syntaxe
cSport._Car__my_private_method()