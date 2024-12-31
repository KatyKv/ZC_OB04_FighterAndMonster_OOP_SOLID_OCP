from abc import ABC, abstractmethod

class Weapon(ABC):
    def __init__(self, power: int = 0):
        self.power = power

    @abstractmethod
    def attack(self):
        pass

class Unarmed(Weapon):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return 'Без оружия'

    def attack(self):
        print(f'Атака без оружия. Сила оружия: {self.power}')
        return self.power

class Sword(Weapon):
    def __init__(self):
        super().__init__(power=10)

    def __str__(self):
        return 'Меч'

    def attack(self):
        print(f'Удар мечом! Сила оружия: {self.power}')
        return self.power

class Bow(Weapon):
    def __init__(self):
        super().__init__(power=5)

    def __str__(self):
        return 'Лук'

    def attack(self):
        print(f'Выстрел из лука. Сила оружия: {self.power}')
        return self.power

class Monster:
    def __init__(self, monster_type: str, lives:int = 50, strength = 5, weapon=None):
        self.type = monster_type
        self.lives = lives
        self.strength = strength

class Fighter:
    def __init__(self, name: str, lives: int = 100, strength: int = 10, weapon: Weapon = None):
        self.name = name
        self.lives = lives
        self.strength = strength
        self.weapon = weapon or Unarmed()

    def fighter_info(self):
        print('Данные воина:')
        print(f'Имя: {self.name}, жизней: {self.lives},')
        print(f'сила: {self.strength}, оружие: {self.weapon} '
              f'с силой атаки {self.weapon.power}')

    def change_weapon(self, new_weapon: Weapon):
        if isinstance(new_weapon, Weapon):
            self.weapon = new_weapon
            print(f'Боец выбирает {new_weapon}')
        else:
            raise ValueError('Новое оружие должно быть объектом'
                             ' подклассов класса Weapon')

    def attack_monster(self, monster: Monster):
        attack_power = self.strength + self.weapon.attack()
        monster.lives -= attack_power
        if monster.lives > 0:
            print(f'Монстр {monster.type} атакован с силой '
                  f'{attack_power}. Осталось {monster.lives} '
                  f'жизней.')
        else:
            print(f'Монстр {monster.type} атакован с силой '
                  f'{attack_power}. {monster.type} мёртв.')

fighter1 = Fighter('Ivan')
monster1 = Monster('Орк')
fighter1.attack_monster(monster1)
fighter1.change_weapon(Sword())
fighter1.attack_monster(monster1)
fighter1.change_weapon(Bow())
fighter1.attack_monster(monster1)
fighter1.attack_monster(monster1)
fighter1.fighter_info()