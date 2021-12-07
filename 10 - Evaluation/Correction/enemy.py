from character import Character


class Enemy(Character):

    def __init__(self, name, marbles, age):
        super().__init__(name, marbles)
        self.__age = age

    def win(self):
        print('The enemy has won')

    def loose(self):
        print('The enemy has lost')
