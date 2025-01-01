from abc import ABC, abstractmethod
from weapon import *

class Character(ABC):
    def __init__(self, character_type: str, lives: int = 100, strength: int = 10, weapon: Weapon = None):
        self.character_type = character_type
        self.lives = lives
        self.strength = strength
        self.weapon = weapon or Unarmed()

    @abstractmethod
    def attack(self, target: 'Character'):
        pass

    @abstractmethod
    def get_damage(self, damage: int):
        pass