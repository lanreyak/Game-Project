#Lanre Yakubu
#Combat Game - 10/24/24

import tbc

def main():
    hero = tbc.Character()
    hero.name = "Valor the Knight"
    hero.HP = 35
    hero.accuracy = 70
    hero.maxDamage = 10
    hero.armor = 0

    monster = tbc.Character("Grimfang the Warlord", 50, 30, 5, 5)

    hero.printStats()
    monster.printStats()

    tbc.punchyPunchy(hero, monster)

if __name__ == "__main__":
    main()