class Lion:

    def feed_lion(self):
        print('Feed the lion with a antelope steak')


class Panda:

    def feed_panda(self):
        print('Feed the panda with bamboo')


class Koala:

    def feed_koala(self):
        print('Feed the koala with eucalyptus leaves')


# Si on souhaitait nourir les animaux

lion = Lion()
lion.feed_lion()

panda = Panda()
panda.feed_panda()

koala = Koala()
koala.feed_koala()

# le problème c'est que si on doit nouroir des centaines d'animaux le processus sera lon et complexe et difficilement maintenable

list_animals = [lion,panda,koala]

for animal in list_animals:
    pass
    # on ne sait pas quelle methode appeler
    # feed_lion ? feed_panda ? feed_koala ?

# la solution sera l'abstraction
# -> elle force les sous classes qui hértient d'une même classe à implémenter les méthodes abstraites de la classe parent