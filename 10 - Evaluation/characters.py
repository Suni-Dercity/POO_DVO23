from abc import ABC, abstractmethod


class Characters(ABC):

    def __init__(self, name, marbles):
        self._name = name
        self._marbles = marbles

    def is_dead(self):
        return self._is_dead

    def is_dead(self, count_marbles):
        if count_marbles <= 0:
            self._is_dead = True
