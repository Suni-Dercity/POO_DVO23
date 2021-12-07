import random


class Utils:

    def check_odd_or_even(self):
        print('I check if odd or even')

    #
    # DEFINE RANDOM MARBLES FOR ENEMY
    #
    def random_values(self,min_value,max_value):
        return random.randint(min_value, max_value)

    pass
