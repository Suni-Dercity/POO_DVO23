from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def feed(self):
        pass


class Lion(Animal):

    def feed(self):
        print('Feed the lion with a antelope steak')

    def lion_method(self):
        print('roar')

    pass


class Panda(Animal):
    def feed(self):
        print('Feed the panda with bamboo')

    pass


class Koala(Animal):

    def feed(self):
        print('Feed the koala with eucalyptus leaves')

    pass


list_animals = [Lion(), Panda(), Koala()]

for animal in list_animals:
    animal.feed()
