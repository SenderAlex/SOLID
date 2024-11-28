from abc import ABC, abstractmethod


class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass


class Sword(Weapon):
    def __init__(self, sword):
        self.sword = sword

    def attack(self):
        return f'Боец атакует мечом'


class Bow(Weapon):
    def __init__(self, bow):
        self.bow = bow

    def attack(self):
        return f'Боец атакует луком'


class Fighter():
    def __init__(self, name, weapons: Weapon):
        self.name = name
        self.weapons = weapons

    def change_weapon(self, weapons: Weapon):
        self.weapons = weapons

    def attack_monster(self, monster):
        print(f'{self.weapons.attack()}')
        print(f'{monster.name} побеждён')


class Monster():
    def __init__(self, name):
        self.name = name

ninja_sword = Sword('Black star sword')
ninja_bow = Bow('Black star bow')
ninja_fighter = Fighter('Alexander', ninja_sword)
ninja_monster = Monster('Black Star')

print(f'\n{ninja_fighter.name} выбирает {ninja_sword.sword}')
ninja_fighter.attack_monster(ninja_monster)

print((f'\n{ninja_fighter.name} выбирает {ninja_bow.bow}'))
ninja_fighter.attack_monster(ninja_monster)