from character import Character


class Hero(Character):

    def __init__(self, name, marbles, loss, gain):
        super().__init__(name, marbles)
        self.__loss = loss
        self.__gain = gain
        self.__scream_war = ''

    @property
    def loss(self):
        return self.__loss

    @property
    def gain(self):
        return self.__gain

    @property
    def scream_war(self):
        return self.__scream_war

    @loss.setter
    def loss(self, loss):
        self.__loss = loss

    @gain.setter
    def gain(self, gain):
        self.__gain = gain

    @scream_war.setter
    def scream_war(self, scream_war):
        self.__scream_war = scream_war

    def win(self):
        print('lennemi gagne')

    def loose(self):
        print('lennemi perd')

    def cheat(self):
        print('je triche ou pas')

    def choose_odd_or_even(self):
        print('je choisi pair ou impair')

    def scream(self):
        print('je gueule')

    def introduce_my_self(self, number_choice):
        print(f'원하는 캐릭터의 원하는 번호를 눌러주세요 {number_choice}'
              f'안녕하세요 성기훈입니다 {self.name}. 나는 {self.marbles} 개의 구슬로 게임을 시작합니다. '
              f'만남에서 이기면 {self.gain} 개의 보너스를, 만남에서 지면 {self.loss} 개의 구슬로 게임을 시작합니다')

    pass