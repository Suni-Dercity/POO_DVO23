from abc import ABC, abstractmethod


class Animal(ABC):

    @property
    @abstractmethod
    def diet(self):
        return self.diet

    @property
    def food(self):
        return self._food

    @food.setter
    def food(self, aliment):
        if aliment in self.diet:
            self._food = aliment
        else:
            raise ValueError(f'Cet animal ne mange pas de {aliment}')

    @abstractmethod
    def feed(self):
        pass


class Panda(Animal):

    @property
    def diet(self):
        return ["leaves", "bamboo"]

    def feed(self, time):
        print(f'Feed the panda with {self.food} at {time}')


# l'idée c'est de définir une propriété abstraite
# diet dans Animal

# et au moment de feed le panda
# vérifier si l'aliment passé rentrer dans la diet du panda

panda = Panda()
panda.food = 'bamboo'  # ça va appeler le setter food
panda.feed('12h00')
