import random
import init
from characters import Characters
from protagonists import Protagonists
from enemies import Enemies
from abc import ABC, abstractmethod

class SGame(ABC):

    def choose_level(self,nb_encounters):
        list_levels = ['5','10','20']
        while True:
            level_choice = input('Choose a level between (1) - Easy / (2) - Hard / (3) - Impossible')
            if level_choice.get(list_levels) is not None:
                level_choice.get(list_levels)
                break

    def choose_enemy(self, enemy):
            return random.choice(enemy)

    def choose_protagonist(self):
        list_protagonists = ['Seong Gi-hun', 'Kang Sae-byeok', 'Cho Sang-woo']
        current_protagonist = input(
            "Choose a protagonist to play the game ! (1) - Seong Gi-hun / (2) - Kang Sae-byeok / (3) - Cho Sang-woo")
        if current_protagonist.isnumeric() and 0 <= int(current_protagonist) - 1 < len(list_protagonists):
            hero = list_protagonists[int(current_protagonist) - 1]
            return hero

    def cheating(self,enemies):
        init.cheat_answer = False
        if enemies.enemies.age > 70:
            while True:
                cheat_answer = input(f'Your enemy is a old as he is {enemies.enemies.age} '
                                     f'years old hehehe, do you wanna cheat on him? (Y)es or (N)o > ').lower()
                if cheat_answer == 'y' or cheat_answer == 'n':
                    cheat_answer.get(cheat_answer)
                    break

    def check_if_odd_or_even(self, nbr_marbles_of_enemy, choice):
        if nbr_marbles_of_enemy % 2 == 0:  # le chiffre est pair
            if choice == 2:
                return True
        else:  # le chiffre est impair
            if choice == 1:
                return True
        return False

    def encounter(self, win, Protagonists, Enemies, Characters):
        answer = input("What is your answer ? (1) - Odd / (2) - Even")
        init.Init.win = False
        while True:
            if answer.isnumeric() and 0 < int(answer) < 3:
                init.Init.win = self.check_if_odd_or_even()
                break
            if init.Init.win:
                print(f"Well done, you beat this enemy, since he had {Enemies.enemies.marbles} marbles >")
                Protagonists.marbles += (Enemies.marbles + Protagonists.gain)
                print(f"You win {Enemies.marbles} marbles from your enemy plus your bonus of {Protagonists.gain}")
                # identifier l'ennemi comme mort
                Characters.is_dead = True
            else:
                print(f"Too bad, you lost this fight, since your enemy had {Enemies.marbles} marbles >")
                Protagonists.marbles -= (Enemies.marbles + Protagonists.loss)
                print(f"You loose {Enemies.marbles} marbles from your enemy minus your malus of {Protagonists.loss}")
                # si on perds on donne une partie de nos billes à l'ennemi
                Enemies.marbles += Protagonists.marbles

