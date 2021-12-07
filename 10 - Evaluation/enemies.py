from characters import Characters


class Enemies(Characters):

    def __init__(self, name, marbles, age, dead):
        super().__init__(name, marbles)
        self.age = age
        self.dead = dead
