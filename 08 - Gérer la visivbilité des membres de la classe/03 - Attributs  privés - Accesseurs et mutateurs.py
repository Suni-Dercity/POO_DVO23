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

car1 = Car('Infernus', 'Pegassi')
print(car1.model,car1.brand)

car1.model = 'Dugsta'
print(car1.model)