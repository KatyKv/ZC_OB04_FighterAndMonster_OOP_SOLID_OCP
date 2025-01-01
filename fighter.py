from weapon import *
from character import Character

class Fighter(Character):
    def __init__(self, name: str):
        super().__init__(character_type='Боец')
        self.name = name

    def fighter_info(self):
        print('-' * 5 + 'Данные воина:' + '-' * 5)
        print(f'{self.character_type} {self.name}, жизней: {self.lives},')
        print(f'сила: {self.strength}, оружие: {self.weapon} '
              f'с силой атаки {self.weapon.power}')
        print('-' * 10)

    def change_weapon(self, new_weapon: Weapon):
        if isinstance(new_weapon, Weapon):
            self.weapon = new_weapon
            print(f'Боец выбирает {new_weapon}')
        else:
            raise ValueError('Новое оружие должно быть объектом'
                             ' подклассов класса Weapon')

    def attack(self, monster: Character):
        attack_power = self.strength + self.weapon.attack()
        print(f'{self.character_type} {self.name} с силой '
              f'{self.strength} и оружием {self.weapon} '
              f'мощностью {self.weapon.power} атакует монстра '
              f'{monster.character_type} уроном {attack_power}')
        return attack_power

    def get_damage(self, damage):
        self.lives -= damage
        if self.lives > 0:
            print(f'{self.character_type} {self.name} атакован. Получил урон '
                  f'{damage}. Осталось {self.lives} жизней.')
        else:
            print(f'{self.character_type} {self.name} атакован. Получил урон '
                  f'{damage}. {self.character_type} {self.name} мёртв.')