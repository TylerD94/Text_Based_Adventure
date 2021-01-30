import random


class Spells:
    def __init__(self, name, damage, cost):
        self.name = name
        self.dmg = damage
        self.cost = cost

    def generate_matk(self):
        dmg_low = self.dmg - 5
        dmg_high = self.dmg + 5
        return random.randrange(dmg_low, dmg_high)

    def get_cost(self):
        return self.cost
