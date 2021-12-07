from characters import Characters

class Protagonists(Characters):

    def __init__(self, name, marbles, gain, loss, scream_war):
        super().__init__(name, marbles)
        self._gain = gain
        self._loss = loss
        self._scream_war = scream_war
