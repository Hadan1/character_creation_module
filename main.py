from random import randint


class Character():
    RANGE_VALUE_ATTACK = (1, 3)

    def __init__(self, name):
        self.name = name

    def attack(self):
        value_attack = 5 + randint(*self.RANGE_VALUE_ATTACK)
        return (f'{self.name} нанёс противнику урон, равный '
                f'{5 + randint(5, 10)}')

    def defence(self):
        ...

    def special(self):
        ...


class Warrior(Character):
    ...


class Mage(Character):
    ...


class Healer(Character):
    ...
