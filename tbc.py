#Lanre Yakubu
#Combat Game - 10/24/24
import random

class Character(object):
    def __init__(self, name="", HP=20, accuracy=50, maxDamage=5, armor=1):
        super().__init__()
        self.name = name
        self.hitPoints = HP
        self.accuracy = accuracy
        self.maxDamage = maxDamage
        self.armor = armor

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def hitPoints(self):
        return self.__HP

    @hitPoints.setter
    def hitPoints(self, value):
        value = self.testInt(value, 0, 100, 0)
        self.__HP = value

    def printStats(self):
        print(f"""
{self.name}
    HP: {self.hitPoints}
    Accuracy: {self.accuracy}
    Max Damage: {self.maxDamage}
    Armor: {self.armor}
    """)

    def hit(self, enemy):
        if random.randint(1, 100) < self.accuracy:
            print(f"{self.name} strikes {enemy.name}!")
            damage = random.randint(1, self.maxDamage)
            print(f"Dealing {damage} points of damage...")
            damage -= enemy.armor
            if damage < 0:
                damage = 0
            if enemy.armor > 0:
                print(f"But {enemy.name} blocks {enemy.armor} damage with armor.")
            enemy.hitPoints -= damage
        else:
            print(f"{self.name} misses the attack on {enemy.name}!")

    def testInt(self, value, min=0, max=100, default=0):
        out = default
        if isinstance(value, int):
            if min <= value <= max:
                out = value
            else:
                print("Value out of range.")
        else:
            print("Must be an integer.")
        return out

def punchyPunchy(hero, monster):
    keepGoing = True
    while keepGoing:
        hero.hit(monster)
        if monster.hitPoints > 0:
            monster.hit(hero)

        print(f"""
{hero.name}: {hero.hitPoints} HP
{monster.name}: {monster.hitPoints} HP
""")

        if hero.hitPoints <= 0:
            print("The kingdom mourns as Valor the Knight falls in battle.")
            keepGoing = False
        elif monster.hitPoints <= 0:
            print("Victory! Valor the Knight has slain Grimfang the Warlord. Your legend will echo through the ages.")
            keepGoing = False

        input("Press <ENTER> to continue the fight...")

def main():
    valor = Character(name="Valor the Knight", HP=30, accuracy=60, maxDamage=8, armor=3)
    grimfang = Character(name="Grimfang the Warlord", HP=35, accuracy=55, maxDamage=10, armor=2)

    valor.printStats()
    grimfang.printStats()

    punchyPunchy(valor, grimfang)

if __name__ == "__main__":
    main()