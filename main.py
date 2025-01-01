from fighter import Fighter
from monster import Monster
from weapon import *
from random import choice


fighter1 = Fighter('Иван')
fighter1.fighter_info()

monster1 = Monster()
monster1.monster_info()
monster2 = Monster(character_type='Орк', lives=35, strength=25)
monster2.monster_info()

fighting_round = 1
while (fighter1.lives > 0 and
    monster1.lives > 0 or monster2.lives > 0):
    print(f'___{fighting_round}-й раунд боя___')
    fighter1.change_weapon(choice([Unarmed(), Sword(), Bow()]))
    if monster1.lives > 0:
        fighter_attack = fighter1.attack(monster1)
        monster1.get_damage(fighter_attack)
    if monster2.lives > 0:
        fighter_attack = fighter1.attack(monster2)
        monster2.get_damage(fighter_attack)

    if monster1.lives > 0:
        monster1_attack = monster1.attack(fighter1)
        fighter1.get_damage(monster1_attack)
    if monster2.lives > 0:
        monster2_attack = monster2.attack(fighter1)
        fighter1.get_damage(monster2_attack)
    fighting_round += 1
    print()



