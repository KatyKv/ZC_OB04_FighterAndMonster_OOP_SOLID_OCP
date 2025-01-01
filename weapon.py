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
        return 'Кулаки (без оружия)'

    def attack(self):
        print(f'Атака кулаками, без оружия. Сила оружия: {self.power}')
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