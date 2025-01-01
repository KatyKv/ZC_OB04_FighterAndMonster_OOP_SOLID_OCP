from character import Character


class Monster(Character):
    def __init__(self, character_type='Монстр', lives=50, strength=20):
        super().__init__(character_type, lives, strength)

    def monster_info(self):
        print('-' * 5 + 'Данные монстра:' + '-' * 5)
        print(f'Тип: {self.character_type}, '
              f'жизней: {self.lives}, сила: {self.strength}')
        print('-' * 10)

    def attack(self, man: Character):
        print(f'{self.character_type} с силой {self.strength} '
              f'атакует героя {man.character_type}')
        return self.strength

    def get_damage(self, damage):
        self.lives -= damage
        if self.lives > 0:
            print(f'{self.character_type} атакован. Получил урон '
                  f'{damage}. Осталось {self.lives} жизней.')
        else:
            print(f'{self.character_type} атакован. Получил урон '
                  f'{damage}. {self.character_type} мёртв.')