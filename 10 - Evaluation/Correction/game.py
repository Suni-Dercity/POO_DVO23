from hero import Hero
from enemy import Enemy
from utils import Utils


class Game(Utils):
    # Attributs de classe
    levels_of_difficulty = {
        "1": 5,
        "2": 10,
        "3": 20
    }

    list_heroes_name = ["성기훈", "강새벽", "조상우"]

    def __init__(self):
        self.__levels = 0
        self.__hero_selected = {}
        self.__current_enemy = {}
        self.__enemy_list = []
        self.__heroes_list = []

    #
    # GETTERS
    #

    @property
    def levels(self):
        return self.__levels

    @property
    def hero_selected(self):
        return self.__hero_selected

    @property
    def current_enemy(self):
        return self.__current_enemy

    @property
    def enemy_list(self):
        return self.__enemy_list

    @property
    def heros_list(self):
        return self.__heros_list

    #
    # SETTERS
    #

    @levels.setter
    def levels(self, levels):
        self.__levels = levels

    @hero_selected.setter
    def hero_selected(self, hero_selected):
        self.__hero_selected = hero_selected

    @current_enemy.setter
    def current_enemy(self, current_enemy):
        self.__current_enemy = current_enemy

    @enemy_list.setter
    def enemy_list(self, enemy_list):
        self.__enemy_list = enemy_list

    @heros_list.setter
    def heros_list(self, heroes_list):
        self.__heroes_list = heroes_list

    #
    # METHODS
    #

    def __create_heroes(self):
        print('Hero creation')
        i = 1
        loss = 2
        while i <= 3:
            hero_name = Game.list_heroes_name[i - 1]
            marbles = i + 15
            malus = loss
            bonus = 1
            self.__heroes_list.append(Hero(hero_name, marbles, malus, bonus))
            i += 1

    def __create_enemies(self):
        print('Enemies creation')
        i = 1
        while i <= 20:
            self.__enemy_list.append(Enemy(f'Enemy n°1 {i}', self.random_values(1, 20), self.random_values(35, 100)))
            i += 1

        print(self.__enemy_list)

    def __ask_level_of_difficulty(self):
        while True:
            level_choice = input('Choose a level between (1) - Easy / (2) - Hard / (3) - Impossible')
            if Game.levels_of_difficulty.get(level_choice) is not None:
                self.__levels = Game.levels_of_difficulty.get(level_choice)
                print(f' You are brave ! You will have to fight {self.__levels} enemies !')
                break

    def __ask_to_choose_hero(self):
        print('Choose a hero')
        for hero in self.__heroes_list:
            hero.introduce_my_self()

        while True:
            hero_choice = input('Which hero will you be ?')
            if hero_choice.isnumeric() and 0 < int(hero_choice) <= len(self.__heroes_list):
                self.__heroes_list = self.__heroes_list[int(hero_choice) - 1]
                break

    def __fights(self):
        i = 1

        while i <= self.levels and not self.hero_selected.dead:
            # Choose a random enemy
            # Introduce the encounter

            i += 1

    def start(self):
        print('Game starting')
        self.__create_heroes()
        self.__create_enemies()
        self.__ask_level_of_difficulty()
        self.__ask_to_choose_hero()  # dans cette méthode on va présenter les héros
        self.__fights()
