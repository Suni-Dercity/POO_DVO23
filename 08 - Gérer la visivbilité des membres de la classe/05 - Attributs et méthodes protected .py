class Car:

    def __init__(self, brand, model):
        self._brand = brand
        self._model = model

    @property
    def model(self):
        return self._model

    @property
    def brand(self):
        return self._brand

    @model.setter
    def model(self, model):
        self._model = model

    @brand.setter
    def brand(self, brand):
        self._brand = brand

    def _method_protected(self):
        print('_method_protected')

class CarSport(Car):
    pass

# j'ai accès aux attributs protected de la classe voiture dans CarSport

cSport = CarSport('Infernus', 'IDK')
print(cSport._brand) # j'ai accès car protected

cSport._method_protected()
